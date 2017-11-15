"""components_controller.py."""

from src.objects.object_extend import ObjectExt
from src.objects.component import Component
from src.services.components_service import ComponentsService as cs
from src.objects.action import Action as actions


class ComponentsController(ObjectExt):
    """ComponentsController."""

    def __init__(self, action=None):
        super(ComponentsController, self).__init__()
        self.__cs = cs()
        self.component = Component()
        self.components = []
        self.response = {}
        self.action = action
        self.data = {}

    def evaluate(self, id_component, req=None):
        """
        The action will be evaluated and the right method will be call
        """
        action = self.action

        print action

        if action == actions.VIEW:
            self.get_components()
        elif action == actions.EDIT:
            self.get_components(id_component)
        elif action == actions.SAVE:
            self.save_component(id_component, req)
        elif action == actions.DELETE:
            self.delete_component(id_component)
        self.set_data()

    def get_component_from_row(self, row):
        """get_component_from_row returns and Component object maping the data from a row"""
        c_component = Component()
        c_component.set_id(row[0])
        c_component.set_name(row[1])
        c_component.set_generic(row[2])
        c_component.set_active(row[3] == 1)
        return c_component

    def get_components(self, id_component=None):
        """get components in db
        if id_component is not None, then it will filter by id
        """
        e_filter = {}
        if id_component is not None:
            e_filter[Component.ID] = self.decrypt(id_component)
            __elements = self.__cs.get_components(e_filter)
            self.component = self.get_component_from_row(__elements[0])
        else:
            __components = self.__cs.get_components(e_filter)
            components = []

            for row in __components:
                c_component = self.get_component_from_row(row)
                components.append(c_component)

            self.components = components

    def save_component(self, id_component, req):
        """
        save_component
        """
        __is_generic = req.forms.get("is_generic") is not None
        __name = req.forms.get("name")
        __id = int(self.decrypt(id_component))

        if __is_generic:
            __is_generic = 1
        else:
            __is_generic = 0

        __component = {}

        __component[Component.ID] = __id
        __component[Component.NAME] = __name
        __component[Component.GENERIC] = __is_generic
        __component[Component.ACTIVE] = 1

        __response = self.__cs.save_component(__component)
        self.response = __response

    def delete_component(self, id_component):
        """
        delete_component
        """
        __id = int(self.decrypt(id_component))

        __response = self.__cs.delete_component(__id)
        self.response = __response

    def get_elements(self, id_component):
        """get_elements method
        recover all the elements of an specific component.
        """
        __id_component = self.decrypt(id_component)
        __elements = self.__cs.get_elements(__id_component)
        return __elements

    def set_data(self):
        """
        set_data docstring
        """
        self.data = {"components": self.components,
                     "component": self.component}
