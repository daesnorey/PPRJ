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
            return object.__dict__
        except Exception:
            return self.default(self, object)