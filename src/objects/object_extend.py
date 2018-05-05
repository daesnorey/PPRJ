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

    def set_value(self, attr, value, find_key=False):
        if find_key:
            for __key, __value in self.__KEYS.items():
                if __value == attr:
                    attr = __key
                    break

        __type = self.get_type(attr)

        if not __type:
            return

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

    def attr_list(self, with_type=False, field_name=True):
        items = dict()
        for key, value in self.__dict__.items():
            __type = self.get_type(key)
            if not value or str(key).startswith("_") or not __type:
                continue
            __key = self.get_key(key) if field_name else key
            items[__key] = value if not with_type else dict(value=value, type=__type)

        return items

    def get_key(self, key):
        return self.__KEYS.get(key)
    
    def get_fields_names(self):
        keys = []
        for key in self.__KEYS:
            keys.append(self.__KEYS.get(key))

    def get_type(self, key):
        return self.__TYPES.get(key)

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key
