import pytest
from advert import Advert, Advert_Color

corgi_advert = """{
      "title": "Вельш-корги",
      "price": 1000,
      "class": "dogs",
      "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
      }
    }"""


def test_nested_object():
    object_advert = Advert(corgi_advert)
    assert object_advert.location.address == "сельское поселение Ельдигинское, поселок санатория Тишково, 25"


def test_bad_price():
    with pytest.raises(ValueError):
        Advert("""{"title": "Вельш-корги", "price": -1000}""")


def test_iphone_no_price():
    object_advert = Advert("""{"title": "Вельш-корги"}""")
    assert object_advert.price == 0


def test_keyword():
    object_advert = Advert(corgi_advert)
    assert object_advert.class_ == 'dogs'


def test_no_title():
    with pytest.raises(ValueError):
        Advert("""{"price": 1000, "class": "dogs"}""")


def test_color():
    object_advert = Advert_Color(corgi_advert)
    assert object_advert.__repr__() == f'\033[0;32;49m Вельш-корги | 1000 ₽\033[0;39;48m'
