"""
elements_controller.py
This file will handle the actions related with models
"""

import sys
sys.path.insert(0, "src/services")
sys.path.insert(1, "src/objects")
from model import Model

class ModelsController(object):
    """
    Class for manipulate the actions
    """

    def __init__(self, action):
        self.models = []
        self.action = action

    def evaluate(self):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
        action = self.action

        print action

        if action is "view":
            self.__get_models()

    def __get_models(self):
        """
        Metodo que obtiene los modelos
        """
