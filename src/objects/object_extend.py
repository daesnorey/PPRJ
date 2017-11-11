"""
among other things
"""

import base64

class ObjectExt(object):
    """
    methods extended
    """

    def __init__(self):
        self.__secret_key = '1234567890123456'

    def get(self, item):
        """
        get lol
        """

        value = getattr(self, "get_" + item)
        return value()

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
