"""
elements_controller.py
This file will handle the actions related with models
"""

from src.services.models_service import ModelsService as ms
from src.objects.model import Model
from src.objects.component import Component
from src.objects.object_extend import ObjectExt
from src.objects.action import Action as actions
from src.controllers.components_controller import ComponentsController as cc

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
        self.is_embed = True

    def evaluate(self, id_model, req=None, embed=False):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos
        pertinentes
        """
        action = self.action
        self.is_embed = embed

        print action

        if action == actions.VIEW:
            self.get_models()
        elif action == actions.EDIT:
            self.get_models(id_model)
        elif action == actions.SAVE:
            self.save_model(id_model, req)
        elif action == actions.DELETE:
            self.delete_model(id_model)
        elif action == "add":
            self.save_model_component(id_model, req)
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
        __id = int(self.decrypt(id_model))
        if self.is_embed:
            __cc = cc(actions.SAVE)
            __req_id = req.forms.get("id")
            print "req_id", __req_id
            __cc.evaluate(__req_id, req)
            __component_id = __cc.response["id"]

            __model_component = {}
            __model_component[Model.ID] = __id
            __model_component[Component.ID] = __component_id
            __model_component["SORT"] = 99

            self.response = self.__ms.save_model(__model_component,
                                                 table="MODEL_COMPONENTS",
                                                 id_name="MODEL_COMPONENT_ID")
        else:
            __name = req.forms.get("name")

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

    def get_components(self, id_model):
        """
        Method get_components get the components of an specific model.
        """
        if self.action == actions.VIEW:
            __id_model = self.decrypt(id_model)
            __components = self.__ms.get_components(__id_model)
            return __components
        else:
            return None

    def save_model_component(self, id_model, req):
        """
        save_model_component
        """
        __id_model = int(self.decrypt(id_model))
        __req_id = req.forms.get("id")
        __id_component = int(self.decrypt(__req_id))
        print "idComponent", __id_component
        __model_component = {}
        __model_component[Model.ID] = __id_model
        __model_component[Component.ID] = __id_component
        __model_component["SORT"] = 99

        self.response = self.__ms.save_model(__model_component,
                                             table="MODEL_COMPONENTS",
                                             id_name="MODEL_COMPONENT_ID")

    def set_data(self):
        """
        set_data docstring
        """
        self.data = {"models": self.models, "model": self.model}
