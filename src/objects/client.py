from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_CLIENTE","third_id":"ID_TERCERO","factor":"FACTOR","phone":"TELEFONO","address":"DIRECCION","start_date":"FECHA_ALTA"}
TYPES = {"id": "int","third_id":"number","factor":"float","phone":"number","address":"string","start_date":"date"}

class Client(ObjectExt):

    TABLE = 'CLIENTE'

    def __init__(self,  row=None):
        super(Client, self).__init__(KEYS, TYPES)
        self.id = row[0] if row else None
        self.third_id = row[1] if row else None
        self.factor = row[2] if row else None
        self.phone = row[3] if row else None
        self.address = row[4] if row else None
