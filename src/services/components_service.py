"""
components_service.py
Contain the possible actions on the components
"""

from src.services.db.oracle import Oracle
from src.objects.component import Component
from src.objects.element import Element
from src.services.db.db_types import DbTypes

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

    def save_component(self, component, table=None, id_name=None):
        """
        save_component
        """
        if not table:
            table = "COMPONENTS"
        if not id_name:
            id_name = Component.ID
        response = self.__db.save(table, component, id_name)
        return response

    def delete_component(self, id_component):
        """
        delete an element with a given id if id_component is None then
        it will return an error
        """
        response = self.__db.delete("COMPONENTS", {Component.ID: id_component})
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

    def delete_component_element(self, id_component, id_element):
        """Method delete_component_element."""
        response = self.__db.delete("COMPONENT_ELEMENTS", {Component.ID:id_component,
                                                           Element.ID:id_element})
        return response

    def get_gen_components(self):
        """ get_gen_components """

        __tbl_0 = "COMPONENTS"
        __tbl_1 = "MODEL_COMPONENTS"
        __pre_tb0 = __tbl_0 + "."
        __pre_tb1 = __tbl_1 + "."
        __fields = [__pre_tb0 + Component.ID,
                    __pre_tb0 + Component.NAME,
                    __pre_tb0 + Component.GENERIC,
                    __pre_tb1 + "SORT"]
        filters = {Component.GENERIC: 1, __pre_tb1 + Component.ID: DbTypes.NULL}
        __join_fields = [[Component.ID]]
        __query = self.__db.get_join_select(__fields, filters, __join_fields,
                                            __tbl_0, __tbl_1)

        __query = __query.replace("INNER", "LEFT")
        response = self.__db.execute(__query, filters, True).fetchall()

        return response
