"""
elements_controller.py
This file will handle the actions related with models
"""

import sys
sys.path.insert(0, "src/services")
sys.path.insert(1, "src/objects")
from models_service import ModelsService as ms
from model import Model
from object_extend import ObjectExt

class ModelsController(ObjectExt):
    """
    Class for manipulate the actions
    """

    def __init__(self, action):
        self.__ms = ms()
        self.model = Model()
        self.models = []
        self.action = action
        self.data = {}

    def evaluate(self, id_model):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
        action = self.action

        print action

        if action == "view":
            self.__get_models()
        elif action == 'edit':
            print "action:", id_model
            self.__get_models(id_model)
        self.__set_data()

    def __get_model_by_row(self, row):
        model = Model()
        model.set_id(row[0])
        model.set_name(row[1])
        model.set_active(row[2] == 1)
        return model

    def __get_models(self, id_model=None):
        """
        get the models from the db
        if id_model is not None then it will filter by id
        """
        m_filter = {}
        if id_model is not None:
            m_filter["MODEL_ID"] = self.decrypt(id_model)
        
        __models = self.__ms.get_models(m_filter)
        models = []

        for row in __models:
            self.model = self.__get_model_by_row(row)
            models.append(self.model)

        self.models = models

    def __set_data(self):
        """
        set_data docstring
        """
        self.data = {"models": self.models, "model":self.model}
