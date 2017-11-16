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

    def get_components(self, filters=None):
        """
        get components in DB with the filters
        """
        if not filters:
            filters = {}
        __query = self.__db.get_query("COMPONENTS", conditions=filters)
        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_component(self, component):
        """
        save_component
        """
        response = self.__db.save("COMPONENTS", component, Component.ID)
        return response

    def delete_component(self, id_component):
        """
        delete an element with a given id if id_component is None then
        it will return an error
        """
        response = self.__db.delete("COMPONENTS", Component.ID, id_component)
        return response

    def get_elements(self, id_component):
        """get_elements method
        @param id_component
        this method returns the elements of a specific component
        """

        __tbl_0 = "COMPONENT_ELEMENTS"
        __tbl_1 = "ELEMENTS"
        __pre_tb0 = __tbl_0 + "."
        __pre_tb1 = __tbl_1 + "."
        __fields = [__pre_tb1 + Element.ID,
                    __pre_tb1 + Element.NAME,
                    __pre_tb1 + Element.CONTAINER,
                    __pre_tb1 + Element.TYPE,
                    __pre_tb0 + "SORT"]
        filters = {Component.ID: id_component, Element.ACTIVE: 1}
        __join_fields = [[Element.ID]]
        __query = self.__db.get_join_select(__fields, filters, __join_fields,
                                            __tbl_0, __tbl_1)

        response = self.__db.execute(__query, filters, True).fetchall()

        elements = []
        for row in response:
            __element = Element()
            __element.set_id(row[0])
            __element.set_name(row[1])
            __element.set_container(row[2])
            __element.set_type_id(row[3])
            elements.append(__element)

        return elements
