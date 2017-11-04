"""
element.py
This file has the structure definition of the element object
"""

from object_extend import ObjectExt

class Element(ObjectExt):
    """
    Element class has the attributes and methods to carrie the information
    """

    def __init__(self):
        """
        Constructor
        intialize every attribute
        """
        self.__id = -1
        self.__name = None
        self.__parent_id = 0
        self.__type_id = 0
        self.__active = False
        self.__container = False

    def set_id(self, element_id):
        """
        setter method for id
        """
        self.__id = element_id

    def get_id(self, encrypt=False):
        """
        getter method for id
        returns a number value
        """
        if encrypt is True:
            return str(self.__id) + "ss"
        else:
            return self.__id

    def set_name(self, element_name):
        """
        setter method for name
        """
        self.__name = element_name

    def get_name(self):
        """
        getter method for name
        returns a string value
        """
        return self.__name

    def set_parent_id(self, element_id):
        """
        setter method for parent_id
        """
        self.__parent_id = element_id

    def get_parent_id(self):
        """
        getter method for parent_id
        returns a number value
        """
        return self.__parent_id

    def set_type_id(self, type_id):
        """
        setter method for type_id
        """
        self.__type_id = type_id

    def get_type_id(self):
        """
        getter method for type_id
        returns a number value
        """
        return self.__type_id

    def set_active(self, active):
        """
        setter method for active
        """
        self.__active = active

    def is_active(self):
        """
        getter method for active
        returns a boolean value
        """
        return self.__active

    def set_container(self, is_container):
        """
        setter method for container
        """
        self.__container = is_container

    def is_container(self):
        """
        getter method for container
        returns a boolean value
        """
        return self.__container


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


class DataType(ObjectExt):
    """
    DataType class has the attributes and methods to carrie the information
    """

    def __init__(self):
        """
        Constructor
        intialize every attribute
        """
        self.__id = -1
        self.__name = None
        self.__table = None

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

    def set_table(self, table):
        """
        setter method for table
        """
        self.__table = table

    def get_table(self):
        """
        getter method for table
        returns a string value
        """
        return self.__table
