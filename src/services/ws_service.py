"""
ws_service.py
"""

from src.services.db.oracle import Oracle

class WsService(object):

    def __init__(self):
        self.__db = Oracle()

    def get_third_party(self, option, request):
        op = request.pop("op", None)

        if op:
            op = int(op)
            params = request.pop("q", "").split(" ")
            if op == 1:
                __fields = ["ID_TERCERO", "NUMERO_DOCUMENTO", "NOMBRES", "APELLIDOS", "FECHA_NACIMIENTO", "FECHA_ALTA"]
                return self.__db.search(table="TERCERO", fields=__fields, conditions=params)
            elif op == 2:
                pass
            else:
                raise Exception("Data corrupted")
        else:
            p = request.get("p")
        #__query = self.__db.get_join_select()
        #def get_join_select(self, fields=None, conditions=None,
        #                join_fields=None, *table):
        #pass
    