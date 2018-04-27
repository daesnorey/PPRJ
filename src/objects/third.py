from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_TERCERO","document_type":"ID_TIPO_DOCUMENTO","document_number":"NUMERO_DOCUMENTO","names":"NOMBRES","surnames":"APELLIDOS","born_date":"FECHA_NACIMIENTO","marital_status":"ID_ESTADO_CIVIL","start_date":"FECHA_ALTA"}
TYPES = {"id":"int","document_type":"char","document_number":"string","names":"string","surnames":"string","born_date":"date","marital_status":"char","start_date":"date"}

class Third(ObjectExt):

    def __init__(self, row=None, w=-1):
        super(Third, self).__init__(KEYS, TYPES)
        self.id = row[0] if row else None
        self.document_type = row[1] if row else None
        self.document_number = row[2] if row else None
        self.names = row[3] if row else None
        self.surnames = row[4] if row else None
        self.born_date = row[5] if row else None
        self.marital_status = row[6] if row else None
        self.start_date = row[7] if row else None
        self.w = w
