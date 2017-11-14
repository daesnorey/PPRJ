"""
models_service.py
file contain the ModelsService class, this will have methods for controling
the crud operation for models
"""

from src.services.db.oracle import Oracle

class ModelsService(object):
    """
    ModelsService class
    """

    def __init__(self):
        self.__db = Oracle()

    def get_models(self, filters={}):
        """
        get models in data base with filters
        """
               
        __query = self.__db.get_query("ELEMENTS", conditions=filters)
        print __query
        
        response = self.__db.execute(__query, filters, True).fetchall()
        print ("msResponse", response)
        return response

    def save_model(self, model):
        """
        save_model
        """
        response = self.__db.save("MODELS", model, "MODEL_ID")
        return response