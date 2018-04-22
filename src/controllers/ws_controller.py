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
        if option == "third-party":
            return self.__get_service().get_third_party(option, request)
        elif option == "third-party_client":
            return self.__get_service().get_client(request)
        elif option == "third-party_employee":
            return self.__get_service().get_employee(request)
        elif option == "document_type":
            return self.__get_service().get_document_type(request)
        else:
            raise Exception("wrong option")
    
    def save(self, option, request, files=None, is_ajax=False, is_xhr=False):
        if option == "third-party":
            return self.__get_service().save_third_party(request)
        elif option == "third-party_client":
            return self.__get_service().save_client(request)
        elif option == "third-party_employee":
            return self.__get_service().save_employee(request)
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