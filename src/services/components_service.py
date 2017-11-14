"""
components_service.py
Contain the possible actions on the components
"""

from src.services.db.oracle import Oracle
from src.objects.component import Component
from src.objects.element import Element

class  ComponentsService(object):
    """ComponentsService class."""

    def __init__(self):
        self.__db = Oracle()

    def get_components(self, filters={}):
        """
        get components in DB with the filters
        """
        __query = self.__db.get_query("COMPONENTS", conditions=filters)
        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_component(self, component):
        """
        save_component
        """
        response = self.__db.save("COMPONENTS", component, Component.ID)
        return response

    def get_elements(self, id_component):
        """get_elements method
        @param id_component
        this method returns the elements of a specific component
        """

        filters = {}
        __conditions = {Component.ID:id_component}
        __join_fields = [Element.ID]
        __query = self.__db.get_join_select(filters, __conditions, __join_fields, "COMPONENT_ELEMENTS", "ELEMENTS")
        print __query

        response = self.__db.execute(__query, filters, True).fetchall()
        return response
