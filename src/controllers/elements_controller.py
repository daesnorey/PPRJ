"""
elements_controller.py
This file will handle every possible action for the elements
"""

import sys
sys.path.insert(0, "src/services")
sys.path.insert(1, "src/objects")
from elements_service import ElementsService as es
from element import Element

class ElementsController(object):
    """
    Class ElementsController will handle the CRUD structure
    """

    def __init__(self, action):
        self.__es = es()
        self.elements = []
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
            self.__get_elements()

    def __get_elements(self, id_element=0):
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
