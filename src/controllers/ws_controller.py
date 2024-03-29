"""ws_controller.py.

ws controller will do the necesary task in order to satisty the
client requirements
"""
from src.services.ws_service import WsService

class WsController(object):
    
    def __init__(self):
        self.__service = None

    def __get_service(self):
        if not self.__service:
            self.__service = WsService()

        return self.__service

    def get(self, option, request):
        if option == "domain":
            return self.__get_service().get_domain(request)
        elif option == "third-party":
            return self.__get_service().get_third_party(option, request)
        elif option == "third-party_client":
            return self.__get_service().get_client(request)
        elif option == "third-party_employee":
            return self.__get_service().get_employee(request)
        elif option == "employee":
            return self.__get_service().get_employee_view(request)
        elif option == "document_type":
            return self.__get_service().get_document_type(request)
        elif option == "purchase":
            pass
        elif option == "purchase_open":
            return self.__get_service().get_purchase(request, dict(ESTADO=0))
        elif option == "purchase_detail":
            return self.__get_service().get_purchase_detail(request, dict(ID_COMPRA=request.get("purchase_id")))
        elif option == "production_chart":
            return self.__get_service().get_production_chart(request)
        elif option == "production":
            return self.__get_service().get_production(request)
        elif option == "production_process":
            return self.__get_service().get_production_process(request)
        elif option == "production_detail":
            return self.__get_service().get_production_detail(request)
        elif option == "process_presentation":
            return self.__get_service().get_process_presentation(request)
        elif option == "inventory":
            return self.__get_service().get_inventory(request)
        else:
            raise Exception("wrong option {}".format(option))
    
    def save(self, option, request, files=None, is_ajax=False, is_xhr=False):
        if option == "third-party":
            return self.__get_service().save_third_party(request)
        elif option == "third-party_client":
            return self.__get_service().save_client(request)
        elif option == "third-party_employee":
            return self.__get_service().save_employee(request)
        elif option == "purchase":
            return self.__get_service().save_purchase(request)
        elif option == "purchase_detail":
            return self.__get_service().save_purchase(request, 1)
        elif option == "production":
            return self.__get_service().save_production(request)
        elif option == "production_process":
            return self.__get_service().save_production_process(request)
        elif option == "production_detail":
            return self.__get_service().save_production_detail(request)
        else:
            raise Exception("wrong option")
    
    def delete(self):
        if option == "third-party":
            return self.__get_service().delete_third_party(request)
        elif option == "third-party_client":
            return self.__get_service().delete_client(request)
        elif option == "third-party_employee":
            return self.__get_service().delete_employee(request)
        else:
            raise Exception("wrong option")