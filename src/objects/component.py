"""
Component.py
this file contain the structure definition of the element component
"""
from src.objects.object_extend import ObjectExt

class Component(ObjectExt):
    """
    Component class has the attributes and methods to control the information
    @attribute id
    @attribute name
    @attribute model_id
    @attribute is_generic
    @attribute is_active
    """

    ID = "COMPONENT_ID"
    NAME = "COMPONENT_NAME"
    GENERIC = "IS_GENERIC"
    ACTIVE = "IS_ACTIVE"

    def __init__(self):
        """
        Constructor
        Initialize every attribute
        """
        super(Component, self).__init__()

        self.__id = -1
        self.__name = ""
        self.__generic = False
        self.__active = False
        self.__model_id = -1
        self.__order = -1

    def set_id(self, component_id):
        """
        setter method for id
        """
        self.__id = component_id

    def get_id(self, encrypt=False):
        """
        getter method for id
        returns a number value
        """
        if encrypt is True:
            return self.encrypt("id")
        else:
            return self.__id

    def set_name(self, component_name):
        """
        setter method for name
        """
        self.__name = component_name

    def get_name(self):
        """
        getter method for name
        returns a string value
        """
        return self.__name

    def set_model_id(self, model_id):
        """
        setter method for model_id
        """
        self.__model_id = model_id

    def get_model_id(self):
        """
        getter method for model_id
        returns a number value
        """
        return self.__model_id

    def set_generic(self, generic):
        """
        setter method for generic
        """
        self.__generic = generic

    def is_generic(self):
        """
        getter method for generic
        returns a boolean value
        """
        return self.__generic

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

    def get_from_row(self, row):
        """
        get_from_row
        """
        self.set_id(row[0])
        self.set_name(row[1])
        self.set_generic(row[2])
        self.set_active(row[3] == 1)
