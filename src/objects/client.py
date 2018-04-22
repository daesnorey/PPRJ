from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_CLIENTE","third_id":"ID_TERCERO","factor":"FACTOR","phone":"TELEFONO_CONTACTO","address":"DIRECCION_FACTURACION"}
TYPES = {"id": "number","third_id":"number","factor":"float","phone":"number","address":"varchar"}

class Client(ObjectExt):

    def __init__(self,  row=None):
        super(Client, self).__init__(KEYS, TYPES)
        self.id = row[0] if row else None
        self.third_id = row[1] if row else None
        self.factor = row[2] if row else None
        self.phone = row[3] if row else None
        self.address = row[4] if row else None
