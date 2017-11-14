"""components_controller.py."""

from src.objects.object_extend import ObjectExt
from src.objects.component import Component
from src.services.components_services import ComponentsServices as cs


class ComponentsController(ObjectExt):
    """ComponentsController."""

    def __init__(self):
        self.__cs = cs()

    def get_elements(self, id_component):
        __id_component = self.decrypt(id_component)

        e_filter = {Component.ID: __id_component}
        __elements = self.__cs.get_elements(e_filter)
        return __elements
