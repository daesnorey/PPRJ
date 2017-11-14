"""
model.py
This file has the structure definition of the model object
"""

from object_extend import ObjectExt

class Model(ObjectExt):
    """
    Model class has the attributes and methods to carrie the information
    """
    ID = "MODEL_ID"
    NAME = "MODEL_NAME"
    ACTIVE = "IS_ACTIVE"

    def __init__(self):
        """
        Constructor
        intialize every attribute
        """
        super(Model, self).__init__()
        self.__id = -1
        self.__name = None
        self.__active = False

    def set_id(self, model_id):
        """
        setter method for id
        """
        self.__id = model_id

    def get_id(self, encrypt=False):
        """
        getter method for id
        returns a number value
        """
        if encrypt is True:
            return self.encrypt("id")
        else:
            return self.__id

    def set_name(self, model_name):
        """
        setter method for name
        """
        self.__name = model_name

    def get_name(self):
        """
        getter method for name
        returns a string value
        """
        return self.__name

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
