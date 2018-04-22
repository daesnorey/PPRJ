"""
among other things
"""

import base64

class ObjectExt(object):
    """
    methods extended
    """

    def __init__(self, KEYS={}, TYPES={}):
        self.__secret_key = '1234567890123456'
        self.__KEYS = KEYS
        self.__TYPES = TYPES

    def get(self, item):
        """
        get lol
        """

        value = getattr(self, "get_" + item)
        return value()

    def set_value(self, attr, value):
        __type = self.get_type(attr)

        if __type == "number":
            value = int(value)
        elif __type == "float":
            value = float(value)
        
        setattr(self, attr, value)

    def encrypt(self, item):
        """
        encrypt
        """
        string = str(self.get(item))
        encoded = base64.b64encode(string)
        return encoded

    def decrypt(self, encoded):
        """
        decrypt
        """
        decoded = base64.b64decode(encoded)
        return decoded

    def attr_list(self, with_type=False):
        items = dict()
        for key, value in self.__dict__.items():
            if not value or str(key).startswith("_"):
                continue
            items[self.get_key(key)] = value if not with_type else dict(value=value, type=self.get_type(key))
        print(items)
        return items

    def get_key(self, key):
        return self.__KEYS.get(key)

    def get_type(self, key):
        return self.__TYPES.get(key)

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key
