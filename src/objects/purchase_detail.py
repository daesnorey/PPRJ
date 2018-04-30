from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_DETALLE_COMPRA","purchase_id":"ID_COMPRA","product_id":"ID_PRODUCTO","presentation_id":"ID_PRESENTACION","amount":"CANTIDAD","unitary_cost":"VALOR_UNITARIO","total_cost":"VALOR_TOTAL"}
TYPES = {"id":"int","purchase_id":"int","product_id":"int","presentation_id":"int","amount":"float","unitary_cost":"int","total_cost":"int"}

class PurchaseDetail(ObjectExt):

    TABLE = 'DETALLE_COMPRA'

    def __init__(self, row=None):
        super(PurchaseDetail, self).__init__(KEYS, TYPES)
        self.id = row[0] if row and row[0] else None
        self.purchase_id = row[1] if row and row[1] else None
        self.product_id = row[2] if row and row[2] else None
        self.presentation_id = row[3] if row and row[3] else None
        self.amount = row[4] if row and row[4] else None
        self.unitary_cost = row[5] if row and row[5] else None
        self.total_cost = row[6] if row and row[6] else None