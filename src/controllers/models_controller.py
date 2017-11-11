"""
elements_controller.py
This file will handle the actions related with models
"""

import sys
sys.path.insert(0, "src/services")
sys.path.insert(1, "src/objects")
from models_service import ModelsService as ms
from model import Model

class ModelsController(object):
    """
    Class for manipulate the actions
    """

    def __init__(self, action):
        self.__ms = ms()
        self.models = []
        self.action = action

    def evaluate(self):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
        action = self.action

        print action

        if action == "view":
            self.__get_models()

    def __get_models(self, id_model=0):
        """
        Metodo que obtiene los modelos de bd
        if id_model > 0 then it will filter by id
        """
        m_filter = {}
        if id_model > 0:
            m_filter["MODEL_ID"] = id_model

        __models = self.__ms.get_models(m_filter)

        models = []

        for row in __models:
            model = Model()
            model.set_id(row[0])
            model.set_name(row[1])
            model.set_active(row[2] == 1)
            models.append(model)

        print ("modelos", models)
        self.models = models
