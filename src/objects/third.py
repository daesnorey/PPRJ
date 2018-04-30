from src.objects.object_extend import ObjectExt

C_KEYS = {"id":"ID_TERCERO","document_type":"ID_TIPO_DOCUMENTO","document_number":"NUMERO_DOCUMENTO","names":"NOMBRES","surnames":"APELLIDOS","born_date":"FECHA_NACIMIENTO","marital_status":"ID_ESTADO_CIVIL","start_date":"FECHA_ALTA"}
C_TYPES = {"id":"int","document_type":"char","document_number":"string","names":"string","surnames":"string","born_date":"date","marital_status":"char","start_date":"date"}

class Third(ObjectExt):

    def __init__(self, row=None, w=-1, KEYS=None, TYPES=None):
        if KEYS:
            for key in KEYS: C_KEYS[key] = KEYS[key]
        if TYPES:
            for key in TYPES: C_TYPES[key] = TYPES[key]
        super(Third, self).__init__(KEYS=C_KEYS, TYPES=C_TYPES)
        self.id = row[0] if row else None
        self.document_type = row[1] if row else None
        self.document_number = row[2] if row else None
        self.names = row[3] if row else None
        self.surnames = row[4] if row else None
        self.born_date = row[5] if row else None
        self.marital_status = row[6] if row else None
        self.start_date = row[7] if row else None
        self.w = w
    
    def draft(self, draft):
        self.id = draft.id
        self.document_type = draft.document_type
        self.document_number = draft.document_number
        self.names = draft.names
        self.surnames = draft.surnames
        self.born_date = draft.born_date
        self.marital_status = draft.marital_status
        self.start_date = draft.start_date
        self.w = draft.w
