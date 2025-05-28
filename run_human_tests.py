#!/usr/bin/env python3
"""
Test runner for all human-generated tests in the LLM testing project.
This script discovers and runs all human-generated test.py files against both GPT and Gemini generated code.

@Authors
Student Names: Barış Türker, Gökçe Akca, Necip Baha Sağıroğlu  
Student IDs: 150170113, 150210046, 150220727
"""

import os
import sys
import subprocess
import glob
from pathlib import Path
from collections import defaultdict
import time


class TestResult:
    def __init__(self, test_path, model, success, output, runtime):
        self.test_path = test_path
        self.model = model
        self.success = success
        self.output = output
        self.runtime = runtime


class HumanTestRunner:
    def __init__(self):
        self.results = []
        self.stats = defaultdict(lambda: defaultdict(int))
        
    def find_human_tests(self):
        """Find all human-generated test.py files."""
        human_tests = []
        for root, dirs, files in os.walk('.'):
            if 'human' in root and 'test.py' in files:
                human_tests.append(os.path.join(root, 'test.py'))
        return sorted(human_tests)
    
    def run_single_test(self, test_path, model):
        """Run a single test file for a specific model."""
        print(f"Running {test_path} with {model}...")
        
        start_time = time.time()
        try:
            # Change to the test directory
            test_dir = os.path.dirname(test_path)
            result = subprocess.run(
                [sys.executable, 'test.py', model],
                cwd=test_dir,
                capture_output=True,
                text=True,
                timeout=30  # 30 second timeout
            )
            runtime = time.time() - start_time
            
            success = result.returncode == 0
            output = result.stdout if success else result.stderr
            
            return TestResult(test_path, model, success, output, runtime)
            
        except subprocess.TimeoutExpired:
            runtime = time.time() - start_time
            return TestResult(test_path, model, False, "Test timed out (30s)", runtime)
        except Exception as e:
            runtime = time.time() - start_time
            return TestResult(test_path, model, False, f"Error running test: {str(e)}", runtime)
    
    def run_all_tests(self):
        """Run all human-generated tests for both models."""
        human_tests = self.find_human_tests()
        models = ['gpt', 'gemini']
        
        print(f"Found {len(human_tests)} human-generated test files")
        print("=" * 60)
        
        total_tests = len(human_tests) * len(models)
        current_test = 0
        
        for test_path in human_tests:
            for model in models:
                current_test += 1
                print(f"[{current_test}/{total_tests}] ", end="")
                
                result = self.run_single_test(test_path, model)
                self.results.append(result)
                
                # Update statistics
                phase = 'phase-1' if 'phase-1' in test_path else 'phase-2'
                difficulty = 'easy' if '/easy/' in test_path else 'medium' if '/medium/' in test_path else 'hard'
                
                self.stats[phase][f"{model}_total"] += 1
                self.stats[phase][f"{difficulty}_total"] += 1
                self.stats[f"{model}_{difficulty}"]["total"] += 1
                
                if result.success:
                    self.stats[phase][f"{model}_passed"] += 1
                    self.stats[phase][f"{difficulty}_passed"] += 1
                    self.stats[f"{model}_{difficulty}"]["passed"] += 1
                    print(f"PASSED")
                else:
                    self.stats[phase][f"{model}_failed"] += 1
                    self.stats[phase][f"{difficulty}_failed"] += 1
                    self.stats[f"{model}_{difficulty}"]["failed"] += 1
                    print(f"FAILED")
        
        print("\n" + "=" * 60)
    
    def print_summary(self):
        """Print a comprehensive summary of test results."""
        print("\nTEST SUMMARY")
        print("=" * 60)
        
        # Overall statistics
        total_tests = len(self.results)
        total_passed = sum(1 for r in self.results if r.success)
        total_failed = total_tests - total_passed
        
        print(f"Total Tests Run: {total_tests}")
        print(f"Total Passed: {total_passed} ({total_passed/total_tests*100:.1f}%)")
        print(f"Total Failed: {total_failed} ({total_failed/total_tests*100:.1f}%)")
        print()
        
        # Model comparison
        print("MODEL COMPARISON")
        print("-" * 30)
        for model in ['gpt', 'gemini']:
            model_results = [r for r in self.results if r.model == model]
            model_passed = sum(1 for r in model_results if r.success)
            model_total = len(model_results)
            print(f"{model.upper()}: {model_passed}/{model_total} ({model_passed/model_total*100:.1f}%)")
        print()
        
        # Difficulty breakdown
        print("DIFFICULTY BREAKDOWN")
        print("-" * 30)
        for difficulty in ['easy', 'medium', 'hard']:
            diff_results = [r for r in self.results if f'/{difficulty}/' in r.test_path]
            if diff_results:
                diff_passed = sum(1 for r in diff_results if r.success)
                diff_total = len(diff_results)
                print(f"{difficulty.capitalize()}: {diff_passed}/{diff_total} ({diff_passed/diff_total*100:.1f}%)")
        print()
        
        # Performance stats
        avg_runtime = sum(r.runtime for r in self.results) / len(self.results)
        print(f"Average Test Runtime: {avg_runtime:.2f}s")
        print()
    
    def print_failures(self):
        """Print details of failed tests."""
        failures = [r for r in self.results if not r.success]
        
        if not failures:
            print("No test failures!")
            return
        
        print(f"\nFAILED TESTS ({len(failures)} total)")
        print("=" * 60)
        
        for result in failures:
            print(f"\nTest: {result.test_path}")
            print(f"Model: {result.model}")
            print(f"Runtime: {result.runtime:.2f}s")
            print("Output:")
            print("-" * 40)
            print(result.output)
            print("-" * 40)
    
    def save_results(self, filename="human_test_results.txt"):
        """Save detailed results to a file."""
        with open(filename, 'w') as f:
            f.write("Human-Generated Test Results\n")
            f.write("=" * 50 + "\n\n")
            
            for result in self.results:
                f.write(f"Test: {result.test_path}\n")
                f.write(f"Model: {result.model}\n")
                f.write(f"Status: {'PASSED' if result.success else 'FAILED'}\n")
                f.write(f"Runtime: {result.runtime:.2f}s\n")
                if not result.success:
                    f.write(f"Output:\n{result.output}\n")
                f.write("-" * 40 + "\n\n")
        
        print(f"\nDetailed results saved to {filename}")


def main():
    """Main function to run all human-generated tests."""
    print("Testing LLM-generated code with human-written tests")
    print("=" * 60)
    
    runner = HumanTestRunner()
    
    try:
        runner.run_all_tests()
        runner.print_summary()
        
        # Ask if user wants to see failure details
        if input("\nShow detailed failure information? (y/N): ").lower().startswith('y'):
            runner.print_failures()
            
    except KeyboardInterrupt:
        print("\n\nTest run interrupted by user")
        if runner.results:
            print("Partial results:")
            runner.print_summary()
    except Exception as e:
        print(f"\nError running tests: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
