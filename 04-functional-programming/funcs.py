import doctest
import itertools
from typing import Iterable


def ilen(iterable: Iterable):
    """
    Получение размера генератора
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return sum(1 for _ in iterable)


def flatten(iterable: Iterable):
    """
    Получение одноуровневого массива из многоуровневого
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten(element)
        else:
            yield element


def distinct(iterable: Iterable):
    """
    Удаление дубликатов из массива с сохранением порядка
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    return list(dict.fromkeys(iterable))


def groupby(key, iterable: Iterable):
    """
    Получение словаря, сгруппированного по ключу
    из неупорядоченной последовательности словарей
    >>> users = [{'gender': 'female', 'age': 33}, {'gender': 'male', 'age': 20}, {'gender': 'female', 'age': 21}]
    >>> groupby('gender', users)
    {'female': [{'gender': 'female', 'age': 33}, {'gender': 'female', 'age': 21}], 'male': [{'gender': 'male', 'age': 20}]}

    Или так:
    >>> groupby('age', users)
    {33: [{'gender': 'female', 'age': 33}], 20: [{'gender': 'male', 'age': 20}], 21: [{'gender': 'female', 'age': 21}]}
    """
    def grouper(item):
        return item[key]

    result = {}
    for prop, items in itertools.groupby(iterable, key=grouper):
        result.setdefault(prop, []).extend(list(items))
    return result


def chunks(size: int, iterable: Iterable):
    """
    Разбиение последовательности на куски заданного размера
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, None)]
    """
    if len(iterable) > 0:
        result = list(iterable[:size])
        if len(result) < size:
            result.extend([None for _ in range(size - len(iterable))])
        yield tuple(result)
        yield from chunks(size, iterable[size:])


def first(iterable: Iterable):
    """
    Получение первого элемента или None
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(-1)) == None
    True
    """
    return next(iter(iterable), None)


def last(iterable: Iterable):
    """
    Получение последнего элемента или None
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0)) == None
    True
    """
    result = None
    for _ in iterable:
        element = next(iter(iterable), None)
        if element is None:
            break
        result = element
    return result


if __name__ == "__main__":
    doctest.testmod()
