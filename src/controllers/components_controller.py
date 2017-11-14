"""components_controller.py."""

from src.objects.object_extend import ObjectExt
from src.objects.component import Component
from src.services.components_service import ComponentsService as cs


class ComponentsController(ObjectExt):
    """ComponentsController."""

    def __init__(self):
        """Constructor."""
        self.__cs = cs()

    def get_elements(self, id_component):
        """Metthod get_elements.

        will get the elements of an specific component.
        """
        __id_component = self.decrypt(id_component)

        e_filter = {Component.ID: __id_component}
        __elements = self.__cs.get_elements(e_filter)
        return __elements
