import time
from src.objects.third import Third
from src.objects.object_extend import ObjectExt

KEYS = {"id":"ID_EMPLEADO","third_id":"ID_TERCERO","factor":"FACTOR","phone":"TELEFONO","start_date":"FECHA_INGRESO","end_date":"FECHA_RETIRO"}
TYPES = {"id": "number","third_id":"number","factor":"float","phone":"number","start_date":"date","end_date":"date"}

class Employee(Third):

    TABLE = 'EMPLEADO'
    VIEW = 'V_EMPLEADO'

    def __init__(self, row=None, w=-1, set_date=True, third=None):
        super(Employee, self).__init__(KEYS=KEYS, TYPES=TYPES)
        self.id = row[0] if row else None
        self.third_id = row[1] if row else None
        self.factor = row[2] if row else None
        self.phone = row[3] if row else None
        self.start_date = row[4] if row and row[4] else time.strftime("%Y-%m-%d") if set_date else None
        self.end_date = row[5] if row else None
        if third:
            self.draft(third)
