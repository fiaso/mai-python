import json
import keyword


class ColorizeMixin(object):
    def __repr__(self):
        return f'\033[0;{self.repr_color_code};49m {self.title} | {self.price} ₽\033[0;39;48m'

class Object:
    def __init__(self, json_dict):
        for key, value in json_dict.items():
            if keyword.iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = Object(value)
            else:
                self.__dict__[key] = value


class Advert():
    def __init__(self, json_str):
        json_dict = json.loads(json_str)
        self.__dict__ = Object(json_dict).__dict__
        self.repr_color_code = 32

        title = self.__dict__.get('title', False)
        if not title:
            raise ValueError
        price = self.__dict__.get('price', False)
        if not price:
            self._price = 0
        elif price < 0:
            raise ValueError
        else:
            self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError
        else:
            self._price = new_price

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert_Color(ColorizeMixin, Advert):
    pass


