"""
models_service.py
file contain the ModelsService class, this will have methods for controling
the crud operation for models
"""

from src.services.db.oracle import Oracle
from src.objects.model import Model
from src.objects.component import Component

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

    def save_model(self, model, table=None, id_name=None):
        """
        save_model
        """
        if not table:
            table = "MODELS"
        if not id_name:
            id_name = Model.ID
        response = self.__db.save(table, model, id_name)
        return response

    def delete_model(self, id_model):
        """
        delete a model with a given id
        """
        response = self.__db.delete("MODELS", {Model.ID : id_model})
        return response

    def get_components(self, id_model):
        """
        @param id_model
        this method returns the elements of a specific component
        """

        __tbl_0 = "MODEL_COMPONENTS"
        __tbl_1 = "COMPONENTS"
        __pre_tb0 = __tbl_0 + "."
        __pre_tb1 = __tbl_1 + "."
        __fields = [__pre_tb1 + Component.ID,
                    __pre_tb1 + Component.NAME,
                    __pre_tb1 + Component.GENERIC,
                    __pre_tb0 + "SORT"]
        filters = {Model.ID: id_model, Component.ACTIVE: 1}
        __join_fields = [[Component.ID]]
        __query = self.__db.get_join_select(__fields, filters, __join_fields,
                                            __tbl_0, __tbl_1)
        print __query
        response = self.__db.execute(__query, filters, True).fetchall()

        components = []
        for row in response:
            __component = Component()
            __component.set_id(row[0])
            __component.set_name(row[1])
            __component.set_generic(row[2])
            components.append(__component)

        return components
