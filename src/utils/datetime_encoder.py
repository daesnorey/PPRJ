"""datetime_encoder.py

Encoder solution created to fixed the json.dumps issue when a datetime is presented
"""

import json

class DatetimeEncoder(json.JSONEncoder):

    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)

    @classmethod
    def jsonDefault(self, object):
        try:
            attr = getattr(object, "attr_list", None)
            __response = dict()
            if attr:
                __response = attr(field_name=False)
            else:
                __response = object.__dict__
            return __response
        except Exception:
            return self.default(self, object)