from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_PROCESO_PRODUCCION","production_id":"ID_PRODUCCION","product_id":"ID_PRODUCTO","presentation_id":"ID_PRESENTACION","process_id":"ID_PROCESO","employee_id":"ID_EMPLEADO","quantity":"CANTIDAD"}
TYPES = {"id":"int","production_id":"int","product_id":"int","presentation_id":"int","process_id":"char","employee_id":"int","quantity":"int"}

class ProductionProcess(ObjectExt):

    TABLE = 'PROCESO_PRODUCCION'

    def __init__(self, row=None):
        super(ProductionProcess, self).__init__(KEYS, TYPES)
        self.id = row[0] if row else None
        self.production_id = row[1] if row else None
        self.product_id = row[2] if row else None
        self.presentation_id = row[3] if row else None
        self.process_id = row[4] if row else None
        self.employee_id = row[5] if row else None
        self.quantity = row[6] if row else None