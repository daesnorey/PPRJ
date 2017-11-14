from src.services.components_service import ComponentsService as cs
from src.objects.object_extend import ObjectExt
from src.objects.component import Component


class ComponentsController(ObjectExt):

    def __init__(self):
        self.__cs = cs()
        pass

    def get_elements(self, id_component):
        __id_component = self.decrypt(id_component)

        e_filter = {Component.ID:__id_component}
        __elements = self.__cs.get_elements(e_filter)
        return __elements
