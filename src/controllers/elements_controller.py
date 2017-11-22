"""
elements_controller.py
This file will handle every possible action for the elements
"""

from src.services.elements_service import ElementsService as es
from src.objects.element import Element, ElementType, DataType
from src.objects.object_extend import ObjectExt
from src.objects.action import Action as actions


class ElementsController(ObjectExt):
    """
    Class ElementsController will handle the CRUD structure
    """

    def __init__(self, action):
        super(ElementsController, self).__init__()
        self.__es = es()
        self.elements = []
        self.element = Element()
        self.element_types = []
        self.data_types = []
        self.element_type = ElementType()
        self.data_type = DataType()
        self.data = {}
        self.action = action
        self.response = None

    def set_data(self):
        """
        set_data docstring
        """
        self.data = {"elements": self.elements, "element_types": self.element_types,
                     "data_types": self.data_types, "element": self.element,
                     "data_type": self.data_type,
                     "element_type":self.element_type}

    def evaluate_elements(self, id_element=None, req=None, is_parent=False):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
        action = self.action

        print action, id_element

        if action == actions.SAVE:
            self.save_element(id_element, req)
        elif action == actions.DELETE:
            self.delete_element(id_element)
        else:
            if action == actions.EDIT:
                self.get_elements(id_element)
            self.get_elements(parent=is_parent)

        self.get_element_types()
        self.set_data()

    def evaluate_element_types(self, id_element_type=None, req=None):
        """
        evaluate_element_types
        """
        action = self.action

        print action, id_element_type

        if action == actions.SAVE:
            self.save_element_type(id_element_type, req)
        elif action == actions.EDIT:
            print "action:", id_element_type
            self.get_element_types(id_element_type)
        elif action == actions.DELETE:
            self.delete_element_type(id_element_type)
        else:
            self.get_element_types()

        self.get_data_types()
        self.set_data()

    def evaluate_data_types(self, id_data_type=None, req=None):
        """
        evaluate_data_types
        """
        action = self.action

        print action, id_data_type

        if action == actions.SAVE:
            self.save_data_type(id_data_type, req)
        elif action == actions.EDIT:
            print "action:", id_data_type
            self.get_data_types(id_data_type)
        elif action == actions.DELETE:
            self.delete_data_type(id_data_type)
        else:
            self.get_data_types()

        self.set_data()

    def get_elements(self, id_element=None, parent=False):
        """
        get elements in db
        if id_element is not None, then it will filter by id
        """
        e_filter = {}
        if id_element is not None and parent is False:
            e_filter[Element.ID] = self.decrypt(id_element)
            __elements = self.__es.get_elements(e_filter)
            self.element = Element()
            self.element.get_from_row(__elements[0])
        else:
            if parent is True:
                e_filter[Element.PARENT] = self.decrypt(id_element)

            __elements = self.__es.get_elements(e_filter)
            elements = []

            for row in __elements:
                c_element = Element()
                c_element.get_from_row(row)
                elements.append(c_element)

            self.elements = elements

    def save_element(self, id_element, req):
        """
        save_element
        """
        __is_container = req.forms.get("is_container") is not None
        __parent_id = req.forms.get("parent_id")
        __type_id = req.forms.get("type_id")
        __name = req.forms.get("name")
        __id = int(self.decrypt(id_element))

        if __is_container:
            __is_container = 1
        else:
            __is_container = 0

        __element = {}

        __element[Element.ID] = __id
        __element[Element.NAME] = __name
        __element[Element.PARENT] = __parent_id
        __element[Element.TYPE] = __type_id
        __element[Element.CONTAINER] = __is_container
        __element[Element.ACTIVE] = 1

        __response = self.__es.save_element(__element)
        self.response = __response

    def delete_element(self, id_element):
        """
        delete_element
        """
        __id = int(self.decrypt(id_element))

        __response = self.__es.delete_element(__id)
        self.response = __response

    def get_element_types(self, id_type=None):
        """
        get element_types in db
        if id_element > 0 then it will filter by id
        """
        e_filter = {}
        if id_type is not None:
            e_filter[ElementType.ID] = self.decrypt(id_type)
            __element_type = self.__es.get_element_types(e_filter)
            self.element_type = ElementType()
            self.element_type.get_from_row(__element_type[0])
        else:
            __element_types = self.__es.get_element_types(e_filter)

            element_types = []

            for row in __element_types:
                __element_type = ElementType()
                __element_type.get_from_row(row)
                element_types.append(__element_type)

            self.element_types = element_types

    def save_element_type(self, id_type, req):
        """
        save_element_type
        """
        __id = int(self.decrypt(id_type))
        __name = req.forms.get("name")
        __tag = req.forms.get("tag")
        __data_type_id = req.forms.get("data_type_id")
        __is_parent = req.forms.get("is_parent") is not None

        if __is_parent:
            __is_parent = 1
        else:
            __is_parent = 0

        __element = {}

        __element[ElementType.ID] = __id
        __element[ElementType.NAME] = __name
        __element[ElementType.TAG] = __tag
        __element[ElementType.DATA_TYPE] = __data_type_id
        __element[ElementType.PARENT] = __is_parent

        __response = self.__es.save_element_type(__element)
        self.response = __response

    def delete_element_type(self, id_type):
        """
        delete_element_type
        """
        __id = int(self.decrypt(id_type))

        __response = self.__es.delete_element_type(__id)
        self.response = __response

    def get_data_types(self, id_type=None):
        """
        get data_types in db
        if id_element > 0 then it will filter by id
        """
        e_filter = {}
        if id_type is not None:
            e_filter[DataType.ID] = self.decrypt(id_type)
            __data_type = self.__es.get_data_types(e_filter)
            self.data_type = DataType()
            self.data_type.get_from_row(__data_type[0])
        else:
            __data_types = self.__es.get_data_types(e_filter)
            data_types = []
            print __data_types
            for row in __data_types:
                __data_type = DataType()
                __data_type.get_from_row(row)
                data_types.append(__data_type)

            self.data_types = data_types

    def save_data_type(self, id_data_type, req):
        """
        save_element
        """
        __id = int(self.decrypt(id_data_type))
        __name = req.forms.get("name")
        __table = req.forms.get("table")

        __data_type = {}

        __data_type[DataType.ID] = __id
        __data_type[DataType.NAME] = __name
        __data_type[DataType.TABLE] = __table

        __response = self.__es.save_data_type(__data_type)
        self.response = __response


    def delete_data_type(self, id_data_type):
        """
        delete_data_type
        """
        __id = int(self.decrypt(id_data_type))

        __response = self.__es.delete_data_type(__id)
        self.response = __response
