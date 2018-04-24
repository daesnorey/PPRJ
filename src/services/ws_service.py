"""
ws_service.py
"""

from src.services.db.oracle import Oracle
from src.objects.client import Client
from src.objects.employee import Employee
from src.objects.third import Third
from src.objects.document_type import DocumentType
from src.objects.purchase import Purchase

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

    def get_client(self, request):
        third_id = request.get("third_id")

        __conditions = dict(ID_TERCERO=third_id)
        __query = self.__db.get_query(table="CLIENTE", conditions=__conditions)
        __response = self.__db.execute(__query, __conditions).fetchone()

        return Client(__response)

    def get_employee(self, request):
        third_id = request.get("third_id")

        __conditions = dict(ID_TERCERO=third_id)
        __query = self.__db.get_query(table="EMPLEADO", conditions=__conditions)
        __response = self.__db.execute(__query, __conditions).fetchone()

        return Employee(__response)

    def get_document_type(self, request):
        __query = self.__db.get_query("TIPO_DOCUMENTO")
        __response = self.__db.execute(__query, {})

        response = []
        while True:
            row = __response.fetchone()
            if not row:
                break
            document_type = DocumentType(row)
            response.append(document_type)

        return response
    
    def get_purchase(self, request, conditions={}):
        __query = self.__db.get_query("COMPRA", conditions=conditions)
        __response = self.__db.execute(__query, conditions)

        response = []
        while True:
            row = __response.fetchone()
            if not row:
                break
            purchase = Purchase(row)
            response.append(purchase)

        return response
   
    def get_domain(self, request):
        __query = self.__db.get_query(request.get("table"))
        __response = self.__db.execute(__query, {})

        response = []
        while True:
            row = __response.fetchone()
            if not row:
                break
            response.append(row)

        return response

    def save_third_party(self, request):
        __third = Third()
        for key in Third.__dict__.keys():
            if request.get(key):
                __third.set_value(key, request.get(key))

        response = self.__db.save("TERCERO", __employee.attr_list(True), "ID_TERCERO")
        return response

    def save_client(self, request):
        __client = Client()
        for key in __client:
            if request.get(key):
                __client.set_value(key, request.get(key))

        response = self.__db.save("CLIENTE", __employee.attr_list(True), "ID_CLIENTE")
        return response

    def save_employee(self, request):
        __employee = Employee()
        for key in __employee:
            if request.get(key):
                __employee.set_value(key, request.get(key))

        response = self.__db.save("EMPLEADO", __employee.attr_list(True), "ID_EMPLEADO")
        return response
