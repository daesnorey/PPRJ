"""
elements_controller.py
This file will handle every possible action for the elements
"""

from bottle import request
import sys
sys.path.insert(0, "src/services")
sys.path.insert(1, "src/objects")
from elements_service import ElementsService as es
from element import Element, ElementType, DataType
from object_extend import ObjectExt


class ElementsController(ObjectExt):
    """
    Class ElementsController will handle the CRUD structure
    """

    def __init__(self, action):
        self.__es = es()
        self.elements = []
        self.element = Element()
        self.element_types = []
        self.data_types = []
        self.data = {}
        self.action = action
        self.response = None

    def evaluate(self, id_element=None, req=None):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
        action = self.action

        print action, id_element

        if action == "save":
            self.save_element(id_element, req)
        elif action == 'edit':
            print "action:", id_element
            self.get_elements(id_element)
        elif action == 'delete':
            self.delete_element(id_element)
        else:
            pass

        self.get_data()


    def get_data(self):
        """
        get_data docstring
        """
        self.get_data_types()
        self.get_element_types()
        self.get_elements()

        self.data = {"elements":self.elements, "element_types":self.element_types,
                     "data_types":self.data_types, "element":self.element}


    def get_elements(self, id_element=None):
        """
        get elements in db
        if id_element is not None, then it will filter by id
        """
        e_filter = {}
        if id_element is not None:
            e_filter["ELEMENT_ID"] = self.decrypt(id_element)
            __elements = self.__es.get_elements(e_filter)
            self.element = self.get_element_from_row(__elements[0])
        else:
            __elements = self.__es.get_elements(e_filter)
            elements = []

            for row in __elements:
                c_element = self.get_element_from_row(row)
                elements.append(c_element)

            self.elements = elements

    def get_element_from_row(self, row):
        """
        extract data to a Element object from a given row
        """
        c_element = Element()
        c_element.set_id(row[0])
        c_element.set_name(row[1])
        c_element.set_parent_id(row[2])
        c_element.set_type_id(row[3])
        c_element.set_active(row[4] == 1)
        c_element.set_container(row[5] == 1)
        return c_element

    def get_element_types(self, id_type=None):
        """
        get element_types in db
        if id_element > 0 then it will filter by id
        """
        e_filter = {}
        if id_type is not None:
            e_filter["ELEMENT_TYPE_ID"] = id_type

        __element_types = self.__es.get_element_types(e_filter)

        element_types = []

        for row in __element_types:
            c_element = ElementType()
            c_element.set_id(row[0])
            c_element.set_name(row[1])
            c_element.set_tag(row[2])
            c_element.set_data_type_id(row[3])
            c_element.set_parent(row[4] == 1)
            element_types.append(c_element)

        self.element_types = element_types

    def get_data_types(self, id_type=0):
        """
        get data_types in db
        if id_element > 0 then it will filter by id
        """
        e_filter = {}
        if id_type > 0:
            e_filter["DATA_TYPE_ID"] = id_type

        __data_types = self.__es.get_data_types(e_filter)

        data_types = []

        for row in __data_types:
            c_element = DataType()
            c_element.set_id(row[0])
            c_element.set_name(row[1])
            c_element.set_table(row[2])
            data_types.append(c_element)

        print data_types
        self.data_types = data_types

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

        __element["ELEMENT_ID"] = __id
        __element["ELEMENT_NAME"] = __name
        __element["PARENT_ELEMENT_ID"] = __parent_id
        __element["ELEMENT_TYPE_ID"] = __type_id
        __element["IS_CONTAINER"] = __is_container
        __element["IS_ACTIVE"] = 1

        __response = self.__es.save_element(__element)
        self.response = __response

    def delete_element(self, id_element):
        """
        delete_element
        """
        __id = int(self.decrypt(id_element))

        __response = self.__es.delete_element(__id)
        self.response = __response
