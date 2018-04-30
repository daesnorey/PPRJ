from src.objects.object_extend import ObjectExt
from src.objects.inventory import Inventory

KEYS = {"id":"ID_DETALLE_PRODUCCION","production_id":"ID_PRODUCCION","inventory_id":"ID_INVENTARIO","cost":"VALOR","date":"FECHA_ALTA","amount":"CANTIDAD"}
TYPES = {"id":"int","production_id":"int","inventory_id":"int","cost":"float","date":"date","amount":"int"}

class ProductionDetail(ObjectExt):

    TABLE = 'DETALLE_PRODUCCION'
    VIEW = 'V_DETALLE_PRODUCCION'

    def __init__(self, row=None, KEYS=KEYS, TYPES=TYPES):
        super(ProductionDetail, self).__init__(KEYS=KEYS, TYPES=TYPES)
        self.id = row[0] if row else None
        self.production_id = row[1] if row else None
        self.inventory_id = row[2] if row else None
        self.cost = row[3] if row else None
        self.date = row[4] if row else None

class ProductionDetailExt(Inventory, ProductionDetail):

    def __init__(self, row):
        super(ProductionDetailExt, self).__init__(KEYS=KEYS, TYPES=TYPES)
        self.id = row[0]
        self.product_id = row[1]
        self.presentation_id = row[2]
        self.batch = row[3]
        self.cost = row[4]
        self.amount = row[5]
        self.date = row[6]

