"""
elements_service.py
file contain the ElementsService class, this will have methods for controling
the crud operation for elements, element_types and data_types
"""

from src.services.db.oracle import Oracle
from src.objects.element import Element, ElementType, DataType

class ElementsService(object):
    """
    ElementsService class
    """

    def __init__(self):
        self.__db = Oracle()

    def get_elements(self, filters=None):
        """
        get elements in data base with filters
        """
        if not filters:
            filters = {}
        __query = self.__db.get_query("ELEMENTS", conditions=filters)
        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_element(self, element):
        """
        save_element
        """
        response = self.__db.save("ELEMENTS", element, Element.ID)
        return response

    def delete_element(self, id_element):
        """
        delete an element with a given id if id_element is None then I will return an error
        """
        response = self.__db.delete("ELEMENTS", {Element.ID: id_element})
        return response

    def get_element_types(self, filters=None):
        """
        get element_types in data base with filters
        """
        if not filters:
            filters = {}
        __query = self.__db.get_query("ELEMENT_TYPES", conditions=filters)
        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_element_type(self, element_type):
        """
        save_element_type
        """
        response = self.__db.save("ELEMENT_TYPES", element_type, ElementType.ID)
        return response

    def delete_element_type(self, id_element_type):
        """
        delete an element with a given id if id_element_type is None then
        it will return an error
        """
        response = self.__db.delete("ELEMENT_TYPES", {ElementType.ID: id_element_type})
        return response

    def get_data_types(self, filters=None):
        """
        get data_types in data base with filters
        """
        if not filters:
            filters = {}
        __query = self.__db.get_query("DATA_TYPES", conditions=filters)
        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_data_type(self, data_type):
        """
        save_data_type
        """
        response = self.__db.save("DATA_TYPES", data_type, DataType.ID)
        return response


    def delete_data_type(self, id_data_type):
        """
        delete an element with a given id if id_data_type is None then I will return an error
        """
        response = self.__db.delete("DATA_TYPES", {DataType.ID: id_data_type})
        return response
