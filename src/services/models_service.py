"""
models_service.py
file contain the ModelsService class, this will have methods for controling
the crud operation for models
"""

from src.services.db.oracle import Oracle
from src.objects.model import Model

class ModelsService(object):
    """
    ModelsService class
    """

    def __init__(self):
        self.__db = Oracle()

    def get_models(self, filters=None):
        """
        get models in data base with filters
        """
        if not filters:
            filters = {}
        __query = self.__db.get_query("MODELS", conditions=filters)
        print __query

        response = self.__db.execute(__query, filters, True).fetchall()
        print ("msResponse", response)
        return response

    def save_model(self, model):
        """
        save_model
        """
        response = self.__db.save("MODELS", model, Model.ID)
        return response

    def delete_model(self, id_model):
        """
        delete a model with a given id
        """
        response = self.__db.delete("MODELS", Model.ID, id_model)
        return response
