import time
from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_COMPRA","third_party_id":"ID_TERCERO","date":"FECHA","sub_cost":"VALOR_NETO","total_cost":"VALOR_TOTAL","state":"ESTADO"}
TYPES = {"id":"int","third_party_id":"int","date":"date","sub_cost":"float","total_cost":"float","state":"int"}

class Purchase(ObjectExt):

    TABLE = 'COMPRA'

    def __init__(self, row=None):
        super(Purchase, self).__init__(KEYS, TYPES)
        self.id = row[0] if row and row[0] else None
        self.third_party_id = row[1] if row and row[1] else None
        self.date = row[2] if row and row[2] else time.strftime("%Y-%m-%d")
        self.sub_cost = row[3] if row and row[3] else 0
        self.total_cost = row[4] if row and row[4] else 0
        self.state = row[5] if row and row[5] else 0