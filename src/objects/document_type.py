from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_TIPO_DOCUMENTO","name":"NOMBRE"}
TYPES = {"id":"char","name":"varchar(30)"}

class DocumentType(ObjectExt):

    def __init__(self, row=None):
        super(DocumentType, self).__init__(KEYS, TYPES)
        self.id = row[0] if row else None
        self.name = row[1] if row else None