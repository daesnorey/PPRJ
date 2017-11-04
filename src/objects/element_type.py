"""
element_type.py
This file has the structure definition of the element_type object
"""

from object_extend import ObjectExt


class ElementType(ObjectExt):
    """
    ElementType class has the attributes and methods to carrie the information
    """

    def __init__(self):
        """
        Constructor
        intialize every attribute
        """
        self.__id = -1
        self.__name = None
        self.__tag = None
        self.__data_type_id = 0
        self.__parent = False

    def set_id(self, element_type_id):
        """
        setter method for id
        """
        self.__id = element_type_id

    def get_id(self):
        """
        getter method for id
        returns a number value
        """
        return self.__id

    def set_name(self, name):
        """
        setter method for name
        """
        self.__name = name

    def get_name(self):
        """
        getter method for name
        returns a string value
        """
        return self.__name

    def set_tag(self, tag):
        """
        setter method for tag
        """
        self.__tag = tag

    def get_tag(self):
        """
        getter method for tag
        returns a string value
        """
        return self.__tag

    def set_data_type_id(self, data_type_id):
        """
        setter method for data_type_id
        """
        self.__data_type_id = data_type_id

    def get_data_type_id(self):
        """
        getter method for data_type_id
        returns a number value
        """
        return self.__data_type_id

    def set_parent(self, parent):
        """
        setter method for parent
        """
        self.__parent = parent

    def is_parent(self):
        """
        getter method for parent
        returns a boolean value
        """
        return self.__parent
