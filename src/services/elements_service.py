"""
elements_service.py
file
"""

import re
import sys
sys.path.insert(0, "src/services/db")
from oracle import Oracle

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
        __query = "SELECT * FROM ELEMENTS"

        if not filters:
            filters = {}
        else:
            __query += " WHERE "
            for key in filters:
                __query += key + " = :" + key

        print __query

        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def get_element_types(self, filters=None):
        """
        get element_types in data base with filters
        """
        if filters is None:
            filters = {}
        else:
            pass

        __query = "SELECT * FROM ELEMENT_TYPES"
        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def get_data_types(self, filters=None):
        """
        get data_types in data base with filters
        """
        if filters is None:
            filters = {}
        else:
            pass

        __query = "SELECT * FROM DATA_TYPES"
        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_element(self, element):
        """
        save_element
        """
        __update_query = """UPDATE ELEMENTS
                            SET ELEMENT_NAME = :ELEMENT_NAME,
                                PARENT_ELEMENT_ID = :PARENT_ELEMENT_ID,
                                ELEMENT_TYPE_ID = :ELEMENT_TYPE_ID,
                                IS_ACTIVE = :IS_ACTIVE,
                                IS_CONTAINER = :IS_CONTAINER
                            WHERE ELEMENT_ID = :ELEMENT_ID
        """


        __insert_query = """INSERT INTO
                            ELEMENTS(ELEMENT_NAME, PARENT_ELEMENT_ID, ELEMENT_TYPE_ID, IS_ACTIVE, IS_CONTAINER) 
                            VALUES (:ELEMENT_NAME, :PARENT_ELEMENT_ID, :ELEMENT_TYPE_ID, :IS_ACTIVE, :IS_CONTAINER)
        """

        response = None

        try:
            if element["ELEMENT_ID"] > 0:
                print "Update", __update_query
                self.__db.execute(__update_query, element, True)
            else:
                print "Insert"
                del element["ELEMENT_ID"]
                self.__db.execute(__insert_query, element, True)
            response = dict(error=0, text="success")
        except Exception as e:
            print e
            response = dict(error=0001, text="There was an error saving")

        return response

    def get_update_query(self, table, fields, conditions):
        """
        get_update_query
        """

        __query = "UPDATE :table SET :instructions WHERE :conditions"

        __inst = ""
        __cond = ""

        for field in fields:
            if __inst:
                __inst += ","
            __inst += field + "=:" + field

        for condition in conditions:
            if __cond:
                __cond += " AND "
            __cond += condition + "=:" + condition

        dic = dict(table=table, instructions=__inst, conditions=__cond)

        pattern = re.compile(r'\b(' + '|:'.join(dic.keys()) + r')\b')
        result = pattern.sub(lambda x: dic[x.group()], __query)

        return result

    def delete_element(self, id_element):
        """
        delete an element with a given id if id_element is None then I will return an error
        """
        if not id_element:
            return dict(error=0002, text="There was an error deleting")

        __delete_query = """DELETE FROM ELEMENTS
                            WHERE ELEMENT_ID = :ELEMENT_ID
                         """

        response = {}

        try:
            self.__db.execute(__delete_query, dict(ELEMENT_ID=id_element), True)
            response = dict(error=0, text="success")
        except Exception:
            response = dict(error=0002, text="There was an error deleting")

        return response
