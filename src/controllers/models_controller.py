"""
elements_controller.py
This file will handle the actions related with models
"""

from src.services.models_service import ModelsService as ms
from src.objects.model import Model
from src.objects.object_extend import ObjectExt
from src.objects.action import Action as actions


class ModelsController(ObjectExt):
    """
    Class for manipulate the actions
    """

    def __init__(self, action):
        super(ModelsController, self).__init__()
        self.__ms = ms()
        self.model = Model()
        self.models = []
        self.action = action
        self.data = {}
        self.response = None

    def evaluate(self, id_model, req=None):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos
        pertinentes
        """
        action = self.action

        print action

        if action == actions.VIEW:
            self.get_models()
        elif action == actions.EDIT:
            self.get_models(id_model)
        elif action == actions.SAVE:
            self.save_model(id_model, req)
        elif action == actions.DELETE:
            self.delete_model(id_model)
        self.set_data()

    def __get_model_by_row(self, row):
        model = Model()
        model.set_id(row[0])
        model.set_name(row[1])
        model.set_active(row[2] == 1)
        return model

    def get_models(self, id_model=None):
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

    def save_model(self, id_model, req):
        """
        save_model
        """
        __name = req.forms.get("name")
        __id = int(self.decrypt(id_model))

        __model = {}

        __model[Model.ID] = __id
        __model[Model.NAME] = __name
        __model[Model.ACTIVE] = 1

        self.response = self.__ms.save_model(__model)

    def delete_model(self, id_model):
        """
        delete_element
        """
        __id = int(self.decrypt(id_model))

        __response = self.__ms.delete_model(__id)
        self.response = __response

    def set_data(self):
        """
        set_data docstring
        """
        self.data = {"models": self.models, "model": self.model}
