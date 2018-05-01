"""
ws_service.py
"""
import base64
import re

from src.services.db.oracle import Oracle
from src.objects.client import Client
from src.objects.employee import Employee
from src.objects.third import Third
from src.objects.document_type import DocumentType
from src.objects.purchase import Purchase
from src.objects.purchase_detail import PurchaseDetail
from src.objects.production import Production
from src.objects.inventory import Inventory
from src.objects.production_detail import ProductionDetail, ProductionDetailExt

from src.services.db.db_types import DbTypes

class WsService(object):

    def __init__(self):
        self.__db = Oracle()
    
    def set_data(self, request, __object):
        for key in __object:
            if request.get(key):
                __val = request.get(key)
                if __val == "undefined":
                    continue
                if __object.get_type(key) in ("int", "float", "date"):
                    try:
                        __val = base64.b64decode(__val)
                        if __object.get_type(key) == "int":
                            __val = int(__val)
                        elif __object.get_type(key) == "float":
                            __val = float(__val)
                    except Exception:
                        if __object.get_type(key) == "date":
                            m = re.search('([0-9]{4}\-[0-9]{2}\-[0-9]{2})', __val)
                            if m:
                                __val = m.group(0)
                            else:
                                continue
                    __object.set_value(key, request.get(key))
                
                __object.set_value(key, __val)

        return __object

    def get_third_party(self, option, request):
        op = request.pop("op", None)

        if op:
            op = int(op)
            params = request.pop("q", "").split(" ")
            if op == 1:
                __fields = ["ID_TERCERO", "NUMERO_DOCUMENTO", "NOMBRES", "APELLIDOS", "FECHA_NACIMIENTO", "FECHA_ALTA"]
                return self.__db.search(table="TERCERO", fields=__fields, conditions=params, class_object=Third)
            elif op == 2:
                pass
            else:
                raise Exception("Data corrupted")
        
        if request.get("third_id"):
            __conditions = dict(ID_TERCERO=request.get("third_id"))
            __query = self.__db.get_query("TERCERO", conditions=__conditions)
            __response = self.__db.execute(__query, __conditions).fetchone()
            return Third(__response)


    def get_client(self, request):
        __client = self.set_data(request, Client())

        __conditions = __client.attr_list()
        __query = self.__db.get_query(table=__client.TABLE, conditions=__conditions)
        __response = self.__db.execute(__query, __conditions).fetchone()

        return Client(__response)

    def get_employee(self, request):
        __employee = self.set_data(request, Employee(set_date=False))
        __all = request.pop("all", None)
        __search = request.pop("search", None)

        if not __search:
            __conditions = __employee.attr_list()
            __specials = []

            if not __all:
                __key = __employee.get_key("end_date")
                __conditions[__key] = DbTypes.NULL
                __specials.append(__key)

            __query = self.__db.get_query(table=__employee.TABLE, conditions=__conditions)
            for key in __specials: __conditions.pop(key, 0)
            __response = self.__db.execute(__query, __conditions).fetchone()

            return Employee(__response, False)
        else:
            params = request.pop("q", "").split(" ")
            __fields = ["ID_EMPLEADO", "NUMERO_DOCUMENTO", "NOMBRES", "APELLIDOS"]
            result = self.__db.search(table="V_EMPLEADO", fields=__fields, conditions=params)
            response = []
            for _, value in result.items():
                __w = value[1]
                __third = Third(w=__w)
                __third.id = value[0][1]
                __third.document_number = value[0][2]
                __third.document_type = value[0][3]
                __third.marital_status = value[0][4]
                __third.names = value[0][5]
                __third.surnames = value[0][6]
                __third.born_date = value[0][7]
                __employee = Employee(w=__w,third=__third)
                __employee.third_id = __third.id
                __employee.id = value[0][0]
                __employee.phone = value[0][8]
                __employee.start_date = value[0][9]
                __employee.factor = value[0][10]
                response.append(__employee)
            response.sort(key=lambda x: x.w, reverse=True)
            return response

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

    def get_purchase_detail(self, request, conditions={}):
        __query = self.__db.get_query("DETALLE_COMPRA", conditions=conditions)
        __response = self.__db.execute(__query, conditions)

        response = []
        while True:
            row = __response.fetchone()
            if not row:
                break
            detail = PurchaseDetail(row)
            response.append(detail)

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

    def get_production_chart(self, request):
        __filter = request.get("filter")
        __table = "V_PAGO_EMPLEADOS_DIA" if __filter == "day" else "V_PAGO_EMPLEADOS"
        __query = self.__db.get_query(__table)

        __response = self.__db.execute(__query, {})

        tmp = {}
        while True:
            row = __response.fetchone()
            if not row:
                break
            __key = row[1]
            if not tmp.get(__key):
                __label = "{} {}".format(row[2], row[3])
                __data = {}
                for i in range(31): __data[i + 1] = 0
                tmp[__key] = dict(label=__label, data=__data)
            __c_key = int(row[4])
            tmp[__key]["data"][__c_key] = row[5] if row[5] else 0

        response = []
        for key in tmp.keys():
            response.append(tmp.get(key))

        return response

    def get_production(self, request):
        __production = self.set_data(request, Production())
        __conditions = __production.attr_list()
        
        __query = self.__db.get_query(__production.TABLE, conditions=__conditions)
        __response = self.__db.execute(__query, __conditions)

        response = []
        while True:
            row = __response.fetchone()
            if not row:
                break
            item = Production(row)
            response.append(item)

        return response

    def get_production_detail(self, request):
        __production_detail = self.set_data(request, ProductionDetail())
        __conditions = __production_detail.attr_list()
        
        __query = self.__db.get_query(__production_detail.VIEW, conditions=__conditions)
        __response = self.__db.execute(__query, __conditions)

        response = []
        while True:
            row = __response.fetchone()
            if not row:
                break
            item = ProductionDetailExt(row)
            response.append(item)

        return response

    def save_third_party(self, request):
        __third = self.set_data(request, Third())

        response = self.__db.save("TERCERO", __third.attr_list(True), "ID_TERCERO")
        return response

    def save_client(self, request):
        __client = Client()
        for key in __client:
            if request.get(key):
                __client.set_value(key, request.get(key))

        response = self.__db.save("CLIENTE", __client.attr_list(True), "ID_CLIENTE")
        return response

    def save_employee(self, request):
        __employee = Employee()
        for key in __employee:
            if request.get(key):
                __employee.set_value(key, request.get(key))

        response = self.__db.save("EMPLEADO", __employee.attr_list(True), "ID_EMPLEADO")
        return response

    def save_purchase(self, request, option=0):
        if option == 0:
            __object = Purchase()
        elif option == 1:
            __object = PurchaseDetail()

        __object = self.set_data(request, __object)
        response = self.__db.save(__object.TABLE, __object.attr_list(True), __object.get_key("id"))
        return response
    
    def save_production(self, request):
        __production = self.set_data(request, Production())
        response = self.__db.save(__production.TABLE, __production.attr_list(True), __production.get_key("id"))
        return response

    def save_production_detail(self, request):
        __amount = request.get("amount")

        if not __amount:
            return
        
        response = dict(error=0)
        __amount = int(__amount)
        while True:
            if __amount < 1:
                break
            
            __amount -= 1
            __inventory = self.set_data(request, Inventory())
            __id_field = __inventory.get_key("id")
            __response = self.__db.save(__inventory.TABLE, __inventory.attr_list(True), "ID_INVENTARIO")
            __id = __response.get("id")

            if __id:
                __production_detail = self.set_data(request, ProductionDetail())
                __production_detail.inventory_id = __id
                __response = self.__db.save(__production_detail.TABLE, __production_detail.attr_list(True), __production_detail.get_key("id"))
                if not __response.get("id"):
                    response = __response
            else:
                response = __response

        return response
