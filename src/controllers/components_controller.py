"""components_controller.py."""

from src.objects.object_extend import ObjectExt
from src.objects.component import Component
from src.objects.element import Element
from src.services.components_service import ComponentsService as cs
from src.objects.action import Action as actions

from src.controllers.elements_controller import ElementsController as ec


class ComponentsController(ObjectExt):
    """ComponentsController."""

    def __init__(self, action=None):
        """Constructor."""
        super(ComponentsController, self).__init__()
        self.__cs = cs()
        self.component = Component()
        self.components = []
        self.response = {}
        self.action = action
        self.data = {}
        self.is_embed = False

    def evaluate(self, id_component, req=None, embed=False):
        """
        The action will be evaluated and the right method will be call
        """
        self.is_embed = embed
        action = self.action

        if action == actions.VIEW:
            self.get_components()
        elif action == actions.EDIT:
            self.get_components(id_component)
        elif action == actions.SAVE:
            self.save_component(id_component, req)
        elif action == actions.DELETE:
            self.delete_component(id_component, req)
        elif action == "create":
            if embed is True:
                self.get_components()
        self.set_data()

    def get_components(self, id_component=None):
        """get components in db
        if id_component is not None, then it will filter by id
        """
        e_filter = {}
        if id_component is not None:
            e_filter[Component.ID] = self.decrypt(id_component)
            __components = self.__cs.get_components(e_filter)
            self.component = Component()
            self.component.get_from_row(__components[0])
        else:
            if self.action == "create":
                __components = self.__cs.get_gen_components()
            else:
                __components = self.__cs.get_components(e_filter)
            components = []

            for row in __components:
                c_component = Component()
                c_component.get_from_row(row)
                components.append(c_component)

            self.components = components

    def save_component(self, id_component, req):
        """
        save_component
        """
        __id = int(self.decrypt(id_component))
        __response = {}
        print self.is_embed

        if self.is_embed:
            __ec = ec(actions.SAVE)
            __req_id = req.forms.get("id")
            __req_pos = int(req.forms.get("position"))
            __ec.evaluate_elements(__req_id, req)
            __element_id = __ec.response["id"]

            __component_element = {}
            __component_element[Component.ID] = __id
            __component_element[Element.ID] = __element_id
            __component_element["POSITION"] = __req_pos
            __component_element["SORT"] = 99

            __response = self.__cs.save_component(__component_element,
                                                  table="COMPONENT_ELEMENTS",
                                                  id_name="COMPONENT_ELEMENT_ID")
        else:
            __is_generic = req.forms.get("is_generic") is not None
            __name = req.forms.get("name")

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

    def delete_component(self, id_component, req=None):
        """
        delete_component
        """

        __id = int(self.decrypt(id_component))

        if self.is_embed:
            __req_id = req.forms.get("id")
            __id_e = int(self.decrypt(__req_id))
            __response = self.__cs.delete_component_element(__id, __id_e)
        else:
            __response = self.__cs.delete_component(__id)
        self.response = __response

    def get_elements(self, id_component):
        """Metthod get_elements.

        will get the elements of an specific component.
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
