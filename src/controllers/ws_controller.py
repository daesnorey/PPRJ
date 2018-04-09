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
        if option == "third":
            return self.__get_service().get_third_party(option, request)
        elif option == "product":
            self.__get_service().get_product(option)
        else:
            raise Exception("wrong option")
    
    def save(self):
        pass
    
    def delete(self):
        pass