"""
elements_controller.py
This file will handle every possible action for the elements
"""

import sys
sys.path.insert(0, "src/services")
sys.path.insert(1, "src/objects")
from elements_service import ElementsService as es
from element import Element, ElementType, DataType

class ElementsController(object):
    """
    Class ElementsController will handle the CRUD structure
    """

    def __init__(self, action):
        self.__es = es()
        self.elements = []
        self.element_types = []
        self.data_types = []
        self.data = {}
        self.action = action

    def evaluate(self):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
        action = self.action

        print action

        if action == "create":
            pass
        elif action is 'update':
            pass
        elif action is 'delete':
            pass
        else:
            self.get_elements()

        self.get_data()


    def get_data(self):
        self.get_data_types()
        self.get_element_types()

        self.data = {"elements":self.elements, "element_types":self.element_types, "data_types":self.data_types}


    def get_elements(self, id_element=0):
        """
        get elements in db
        if id_element > 0 then it will filter by id
        """
        e_filter = {}
        if id_element > 0:
            e_filter["ELEMENT_ID"] = id_element

        __elements = self.__es.get_elements(e_filter)

        elements = []

        for row in __elements:
            c_element = Element()
            c_element.set_id(row[0])
            c_element.set_name(row[1])
            c_element.set_parent_id(row[2])
            c_element.set_type_id(row[3])
            c_element.set_active(row[4] == 1)
            c_element.set_container(row[5] == 1)
            elements.append(c_element)

        print elements
        self.elements = elements

    def get_element_types(self, id_type=0):
        """
        get element_types in db
        if id_element > 0 then it will filter by id
        """
        e_filter = {}
        if id_type > 0:
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

        print element_types
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

        print data_types
        self.data_types = data_types
