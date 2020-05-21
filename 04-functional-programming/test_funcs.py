import funcs
import pytest


@pytest.mark.parametrize('iterable, expected', [
    ((x for x in range(10)), 10),
])
def test_ilen(iterable, expected):
    assert funcs.ilen(iterable) == expected


@pytest.mark.parametrize('iterable, expected', [
    ([0, [1, [2, 3]]], [0, 1, 2, 3]),
])
def test_flatten(iterable, expected):
    assert list(funcs.flatten(iterable)) == expected


@pytest.mark.parametrize('iterable, expected', [
    ([1, 2, 0, 1, 3, 0, 2], [1, 2, 0, 3]),
])
def test_distinct(iterable, expected):
    assert list(funcs.distinct(iterable)) == expected


@pytest.mark.parametrize('iterable, key, expected', [
    (
         [
             {'gender': 'female', 'age': 33},
             {'gender': 'male', 'age': 20},
             {'gender': 'female', 'age': 21}
         ],
         'gender',
         {
             'female': [
                   {'gender': 'female', 'age': 33},
                   {'gender': 'female', 'age': 21}
             ],
             'male': [
                {'gender': 'male', 'age': 20}
             ]
         }
    ),
    (
         [
             {'gender': 'female', 'age': 33},
             {'gender': 'male', 'age': 20},
             {'gender': 'female', 'age': 21}
         ],
         'age',
         {
             33: [{'gender': 'female', 'age': 33}],
             20: [{'gender': 'male', 'age': 20}],
             21: [{'gender': 'female', 'age': 21}]
         }
    )
])
def test_groupby(iterable, key, expected):
    assert funcs.groupby(key, iterable) == expected


@pytest.mark.parametrize('iterable, size, expected', [
    ([0, 1, 2, 3, 4], 3, [(0, 1, 2), (3, 4, None)]),
])
def test_chunks(iterable, size, expected):
    assert list(funcs.chunks(size, iterable)) == expected


@pytest.mark.parametrize('iterable, expected', [
    ((x for x in range(10)), 0),
    (range(0), None)
])
def test_first(iterable, expected):
    assert funcs.first(iterable) == expected


@pytest.mark.parametrize('iterable, expected', [
    ((x for x in range(10)), 9),
    (range(0), None)
])
def test_last(iterable, expected):
    assert funcs.last(iterable) == expected
