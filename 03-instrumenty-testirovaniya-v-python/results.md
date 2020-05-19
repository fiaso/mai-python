##Results
###Issue-1
`python3 -m doctest -v -o NORMALIZE_WHITESPACE i1_morse.py`

```commandline
Trying:
    encode('SOS')
Expecting:
    '...
    ---
    ...'
ok
Trying:
    encode('МАИ-ПИТОН-2020') # doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 'М'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   2 tests in morse.encode
2 tests in 3 items.
2 passed and 0 failed.
Test passed.
```

###Issue-2
`python3 -m pytest -v i2_morse.py` 

```commandline
============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /media/sofia/disk/Study/Master/sem2/Python/mai-python/03-instrumenty-testirovaniya-v-python
collected 3 items                                                                                                                                                                                                

morse.py::test_decode[-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- ..--- ------MAI-PYTHON-2020] PASSED                                                                                       [ 33%]
morse.py::test_decode[... --- ...-SOS] PASSED                                                                                                                                                              [ 66%]
morse.py::test_decode[.--. .- .-. .. ...-PARIS] PASSED                                                                                                                                                     [100%]

=============================================================================================== 3 passed in 0.02s ================================================================================================
```

###Issue-3
`python3 -m unittest -v i3_one_hot_encoder.py`

```commandline
test_empty (one_hot_encoder.TestFitTransform) ... ok
test_equal (one_hot_encoder.TestFitTransform) ... ok
test_exception (one_hot_encoder.TestFitTransform) ... ok
test_notin (one_hot_encoder.TestFitTransform) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
###Issue-4
`python3 -m pytest -v i4_one_hot_encoder.py `

```commandline
============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /media/sofia/disk/Study/Master/sem2/Python/mai-python/03-instrumenty-testirovaniya-v-python
collected 8 items / 4 deselected / 4 selected                                                                                                                                                                    

one_hot_encoder.py::test_pytest_equal PASSED                                                                                                                                                               [ 25%]
one_hot_encoder.py::test_pytest_empty PASSED                                                                                                                                                               [ 50%]
one_hot_encoder.py::test_pytest_notin PASSED                                                                                                                                                               [ 75%]
one_hot_encoder.py::test_pytest_exception PASSED                                                                                                                                                           [100%]

======================================================================================== 4 passed, 4 deselected in 0.03s =========================================================================================
```

###Issue-5
`python3 -m pytest -v i5_what_is_year_now.py`

```commandline
============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /media/sofia/disk/Study/Master/sem2/Python/mai-python/03-instrumenty-testirovaniya-v-python
collected 3 items                                                                                                                                                                                                

what_is_year_now.py::test_format_ymd PASSED                                                                                                                                                                [ 33%]
what_is_year_now.py::test_format_dmy PASSED                                                                                                                                                                [ 66%]
what_is_year_now.py::test_format_err PASSED                                                                                                                                                                [100%]

=============================================================================================== 3 passed in 0.06s ================================================================================================
```

`coverage report -m i5_what_is_year_now.py`

```commandline
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
what_is_year_now.py      37      4    89%   62-66
```
