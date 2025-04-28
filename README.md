FAILED TESTS ON PHASE 1

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/medium/eval-6/gpt/test.py
F....
======================================================================
FAIL: test_deep_nesting (__main__.TestParseNestedParens.test_deep_nesting)
Verify correct depth for a deeply-nested group.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/medium/eval-6/gpt/test.py", line 19, in test_deep_nesting
    self.assertEqual(parse_nested_parens('(((((())))))'), [5])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [6] != [5]

First differing element 0:
6
5

- [6]
+ [5]

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/medium/eval-125/gemini/test.py
F....
======================================================================
FAIL: test_count_odd_lowercase (__main__.TestSplitWords.test_count_odd_lowercase)
Tests counting odd-ordered lowercase letters when no delimiters are present.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/medium/eval-125/gemini/test.py", line 21, in test_count_odd_lowercase
    self.assertEqual(split_words("Programming"), 4) # r(17), g(6 - even), r(17), m(12 - even), m(12 - even), n(13), g(6 - even) -> r, r, n -> 3? No, P(15), r(17), o(14), g(6), r(17), a(0), m(12), m(12), i(8), n(13), g(6) -> P, r, r, n -> 4
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 3 != 4

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (failures=1)
```

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/medium/eval-144/gemini/test.py
.F...
======================================================================
FAIL: test_large_numbers_fractional (__main__.TestSimplifyFunction.test_large_numbers_fractional)
Tests with larger numerators/denominators resulting in a fraction.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/medium/eval-144/gemini/test.py", line 29, in test_large_numbers_fractional
    self.assertFalse(simplify("99/17", "17/3"), "Test Case 10 Failed: 99/17 * 17/3 = 1683/51 = 33/1 should be True, but the simplified form is 33. Oh wait, 1683/51 is exactly 33. Let's fix this test.")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: True is not false : Test Case 10 Failed: 99/17 * 17/3 = 1683/51 = 33/1 should be True, but the simplified form is 33. Oh wait, 1683/51 is exactly 33. Let's fix this test.

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/easy/eval-91/gemini/test.py
.F...
======================================================================
FAIL: test_leading_trailing_spaces (__main__.TestIsBored.test_leading_trailing_spaces)
Test strings with extra whitespace around sentences.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/easy/eval-91/gemini/test.py", line 33, in test_leading_trailing_spaces
    self.assertEqual(is_bored("   I am happy.  But I am also tired. "), 2)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 2

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/hard/eval-99/gemini/test.py
.F...
======================================================================
FAIL: test_invalid_input (__main__.TestClosestInteger.test_invalid_input)
Test that invalid number strings raise ValueError.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/hard/eval-99/gemini/test.py", line 44, in test_invalid_input
    with self.assertRaises(ValueError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/hard/eval-99/gpt/test.py
....F
======================================================================
FAIL: test_round_up (__main__.TestClosestInteger.test_round_up)
Fractional part > 0.5 should round away from zero.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/hard/eval-99/gpt/test.py", line 17, in test_round_up
    self.assertEqual(closest_integer("-2.51"), -3)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -2 != -3

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/easy/eval-22/gpt/test.py
..F.
======================================================================
FAIL: test_integers_and_bools (__main__.TestFilterIntegers.test_integers_and_bools)
Booleans must be excluded even though isinstance(True, int) is True.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/easy/eval-22/gpt/test.py", line 16, in test_integers_and_bools
    self.assertEqual(filter_integers([True, False, 7, 0, -3]), [7, -3])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [7, 0, -3] != [7, -3]

First differing element 1:
0
-3

First list contains 1 additional elements.
First extra element 2:
-3

- [7, 0, -3]
?     ---

+ [7, -3]

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
```

```sh
necipsagiroglu@Necips-MacBook-Air llm-testing % python3 phase-1/easy/eval-29/gemini/test.py
F.....
======================================================================
FAIL: test_all_matches (__main__.TestFilterByPrefix.test_all_matches)
Test when all strings match the prefix.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/necipsagiroglu/projects/personal/llm-testing/phase-1/easy/eval-29/gemini/test.py", line 22, in test_all_matches
    self.assertEqual(filter_by_prefix(strings, prefix), strings)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: ['apple', 'application'] != ['apple', 'apricot', 'application']

First differing element 1:
'application'
'apricot'

Second list contains 1 additional elements.
First extra element 2:
'application'

- ['apple', 'application']
+ ['apple', 'apricot', 'application']
?          +++++++++++


----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (failures=1)
```
