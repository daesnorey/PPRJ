"""
among other things
"""

import base64

class ObjectExt(object):
    """
    methods extended
    """

    def __init__(self):
        pass

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
        string = self.get(item)
        key = "encrypt1231dasd52"
        encoded_chars = []
        for i in xrange(len(string)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = "".join(encoded_chars)
        return base64.urlsafe_b64encode(encoded_string)
