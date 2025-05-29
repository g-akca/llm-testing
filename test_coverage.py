# @Authors
# Student Names: Barış Türker, Gökçe Akca, Necip Baha Sağıroğlu  
# Student IDs: 150170113, 150210046, 150220727

#!/usr/bin/env python3
import os
import sys
import unittest
import importlib.util
import json
from coverage import Coverage

def find_test_dirs(root):
    out = []
    for dp, dn, fn in os.walk(root):
        if "test.py" in fn and "generated_code.py" in fn:
            out.append(dp)
    return out

def load_tests_from_dir(test_dir, prefix):
    suite = unittest.TestSuite()
    main_mod = sys.modules["__main__"]
    old_modules = set(sys.modules)
    old_path = sys.path[:]
    try:
        gen_fp = os.path.join(test_dir, "generated_code.py")
        spec_g = importlib.util.spec_from_file_location("__main__", gen_fp)
        mod_g = importlib.util.module_from_spec(spec_g)
        spec_g.loader.exec_module(mod_g)
        sys.modules["__main__"] = mod_g
        sys.modules["generated_code"] = mod_g

        sys.path.insert(0, test_dir)
        test_fp = os.path.join(test_dir, "test.py")
        test_name = f"{prefix}_test"
        sys.modules.pop(test_name, None)
        spec_t = importlib.util.spec_from_file_location(test_name, test_fp)
        mod_t = importlib.util.module_from_spec(spec_t)
        sys.modules[test_name] = mod_t
        spec_t.loader.exec_module(mod_t)

        suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(mod_t))
    finally:
        sys.modules["__main__"] = main_mod
        sys.path[:] = old_path
        for m in set(sys.modules) - old_modules:
            sys.modules.pop(m, None)
    return suite

def main():
    root = os.getcwd()
    cov = Coverage(source=[root])
    cov.start()

    test_dirs = find_test_dirs(root)
    if not test_dirs:
        print("Couldn't find any test.py + generated_code.py pairs!", file=sys.stderr)
        sys.exit(1)

    total_suite = unittest.TestSuite()
    for d in test_dirs:
        prefix = os.path.relpath(d, root).replace(os.sep, "_")
        total_suite.addTests(load_tests_from_dir(d, prefix))

    result = unittest.TextTestRunner(verbosity=2).run(total_suite)
    if not result.wasSuccessful():
        print("Some tests were unsuccessful!", file=sys.stderr)

    cov.stop()
    cov.save()

    json_path = os.path.join(root, "coverage.json")
    cov.json_report(outfile=json_path)
    with open(json_path, encoding="utf-8") as jf:
        data = json.load(jf)

    csv_path = os.path.join(root, "coverage.csv")
    with open(csv_path, "w", encoding="utf-8") as cf:
        cf.write("Filename,Stmts,Miss,Cover,Missing\n")
        for fn, info in sorted(data.get("files", {}).items()):
            if not fn.endswith("generated_code.py"):
                continue
            stmts = info["summary"].get("num_statements", 0)
            missing_list = info.get("missing_lines", [])
            miss = len(missing_list)
            cover = round(info["summary"].get("percent_covered", 0.0), 2)
            missing_str = ",".join(str(x) for x in missing_list)
            cf.write(f"{fn},{stmts},{miss},{cover},\"{missing_str}\"\n")

    print(f"\nLine coverage report has been created: {csv_path}")

if __name__ == "__main__":
    main()
