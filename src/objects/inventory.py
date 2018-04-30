from src.objects.object_extend import ObjectExt

C_KEYS = {"id":"ID_INVENTARIO","batch":"LOTE","presentation_id":"ID_PRESENTACION","product_id":"ID_PRODUCTO","inventory_state_id":"ID_ESTADO_INVENTARIO","start_date":"FECHA_ALTA","expiration_date":"FECHA_VENCIMIENTO"}
C_TYPES = {"id":"int","batch":"string","presentation_id":"int","product_id":"int","inventory_state_id":"char","start_date":"date","expiration_date":"date"}

class Inventory(ObjectExt):

    TABLE = 'INVENTARIO'

    def __init__(self, row=None, KEYS=None, TYPES=None):
        if KEYS:
            for key in KEYS: C_KEYS[key] = KEYS[key]
        if TYPES:
            for key in TYPES: C_TYPES[key] = TYPES[key]
        super(Inventory, self).__init__(KEYS=C_KEYS, TYPES=C_TYPES)
        self.id = row[0] if row else None
        self.batch = row[1] if row else None
        self.presentation_id = row[2] if row else None
        self.product_id = row[3] if row else None
        self.inventory_state_id = row[4] if row else 'A'
        self.start_date = row[5] if row else None
        self.expiration_date = row[6] if row else None

    def draft(self, draft):
        self.id = draft.id
        self.batch = draft.batch
        self.presentation_id = draft.presentation_id
        self.product_id = draft.product_id
        self.inventory_state_id = draft.inventory_state_id
        self.start_date = draft.start_date
        self.expiration_date = draft.expiration_date