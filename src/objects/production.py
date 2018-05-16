from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_PRODUCCION","date":"FECHA_ALTA","cost":"VALOR"}
TYPES = {"id":"int","date":"date","cost":"float"}

class Production(ObjectExt):

    TABLE = 'PRODUCCION'

    def __init__(self, row=None):
        super(Production, self).__init__(KEYS, TYPES)
        self.id = row[0] if row else None
        self.date = row[1] if row else None
        self.cost = row[2] if row else None
