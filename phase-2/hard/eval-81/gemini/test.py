import unittest
# Assuming the function is saved in a file named 'grade_converter.py'
# If not, you might need to adjust the import or include the function definition directly
from generated_code import numerical_letter_grade 

class TestNumericalLetterGrade(unittest.TestCase):

    def test_example_case(self):
        """Tests the example provided in the docstring."""
        gpas = [4.0, 3, 1.7, 2, 3.5]
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_boundary_values(self):
        """Tests exact boundary GPAs."""
        gpas = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
        # Based on the logic: > 3.7 is A, so 3.7 is A-
        # > 3.3 is A-, so 3.3 is B+
        # > 3.0 is B+, so 3.0 is B
        # > 2.7 is B, so 2.7 is B-
        # > 2.3 is B-, so 2.3 is C+
        # > 2.0 is C+, so 2.0 is C
        # > 1.7 is C, so 1.7 is C-
        # > 1.3 is C-, so 1.3 is D+
        # > 1.0 is D+, so 1.0 is D
        # > 0.7 is D, so 0.7 is D-
        # > 0.0 is D-, so 0.0 is E
        expected = ['A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_within_range_values(self):
        """Tests GPAs clearly within each grade range."""
        gpas = [3.85, 3.5, 3.1, 2.8, 2.5, 2.1, 1.8, 1.5, 1.1, 0.8, 0.3]
        expected = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_single_values(self):
        """Tests lists with single GPA values."""
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])
        self.assertEqual(numerical_letter_grade([2.9]), ['B'])
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])
        self.assertEqual(numerical_letter_grade([1.35]), ['C-'])

    def test_empty_list(self):
        """Tests an empty input list."""
        self.assertEqual(numerical_letter_grade([]), [])

# To run the tests if this script is executed directly
if __name__ == '__main__':
    # You would typically run this from the command line using:
    # python -m unittest test_grade_converter.py 
    # (assuming you save this test code as test_grade_converter.py
    # and the function code as grade_converter.py)
    
    # For demonstration purposes, you can run it like this:
    # Create a dummy grade_converter module if it doesn't exist
    import sys
    import types
    if 'grade_converter' not in sys.modules:
        grade_converter = types.ModuleType('grade_converter')
        # Paste the function definition here for self-contained execution
        def numerical_letter_grade(grades):
            """It is the last week of the semester and the teacher has to give the grades
            to students. The teacher has been making her own algorithm for grading.
            The only problem is, she has lost the code she used for grading.
            She has given you a list of GPAs for some students and you have to write 
            a function that can output a list of letter grades using the following table:
                     GPA       |    Letter grade
                      4.0                A+
                    > 3.7                A 
                    > 3.3                A- 
                    > 3.0                B+
                    > 2.7                B 
                    > 2.3                B-
                    > 2.0                C+
                    > 1.7                C
                    > 1.3                C-
                    > 1.0                D+ 
                    > 0.7                D 
                    > 0.0                D-
                      0.0                E
            

            Example:
            numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
            """
            import math
            letter_grades = []
            for gpa in grades:
                if math.isclose(gpa, 4.0):
                    letter_grades.append("A+")
                elif gpa > 3.7:
                    letter_grades.append("A")
                elif gpa > 3.3:
                    letter_grades.append("A-")
                elif gpa > 3.0:
                    letter_grades.append("B+")
                elif gpa > 2.7:
                    letter_grades.append("B")
                elif gpa > 2.3:
                    letter_grades.append("B-")
                elif gpa > 2.0:
                    letter_grades.append("C+")
                elif gpa > 1.7:
                    letter_grades.append("C")
                elif gpa > 1.3:
                    letter_grades.append("C-")
                elif gpa > 1.0:
                    letter_grades.append("D+")
                elif gpa > 0.7:
                    letter_grades.append("D")
                elif gpa > 0.0:
                    letter_grades.append("D-")
                elif math.isclose(gpa, 0.0): 
                    letter_grades.append("E")
                else:
                    pass 
            return letter_grades
        grade_converter.numerical_letter_grade = numerical_letter_grade
        sys.modules['grade_converter'] = grade_converter
        # Re-import after creating the dummy module
        from grade_converter import numerical_letter_grade 

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

