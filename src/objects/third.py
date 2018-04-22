from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_EMPLEADO","third_id":"ID_TERCERO","factor":"FACTOR","phone":"TELEFONO","start_date":"FECHA_INGRESO","end_date":"FECHA_RETIRO"}
TYPES = {"id": "number","third_id":"number","factor":"float","phone":"number","start_date":"date","end_date":"date"}

class Third(ObjectExt):

    def __init__(self, row=None, w=-1):
        super(Third, self).__init__(KEYS, TYPES)
        self.id = row[0] if row else None
        self.document_type = row[1] if row else None
        self.document_number = row[2] if row else None
        self.names = row[3] if row else None
        self.surnames = row[4] if row else None
        self.third_type = row[5] if row else None
        self.born_date = row[6] if row else None
        self.marita_status = row[7] if row else None
        self.start_date = row[8] if row else None
        self.w = w
