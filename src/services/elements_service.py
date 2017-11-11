"""
elements_service.py
file
"""

from src.services.db.oracle import Oracle

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

    def get_element_types(self, filters=None):
        """
        get element_types in data base with filters
        """
        __query = "SELECT * FROM ELEMENT_TYPES"

        if not filters:
            filters = {}
        else:
            __query += " WHERE "
            for key in filters:
                __query += key + " = :" + key

        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_element_type(self, element_type):
        """
        save_element_type
        """
        __update_query = """UPDATE ELEMENT_TYPES
                            SET ELEMENT_TYPE_NAME = :ELEMENT_TYPE_NAME,
                                ELEMENT_TAG = :ELEMENT_TAG,
                                DATA_TYPE_ID = :DATA_TYPE_ID,
                                IS_PARENT = :IS_PARENT
                            WHERE ELEMENT_TYPE_ID = :ELEMENT_TYPE_ID
        """

        __insert_query = """INSERT INTO
                            ELEMENT_TYPES(ELEMENT_TYPE_NAME, ELEMENT_TAG, DATA_TYPE_ID, IS_PARENT)
                            VALUES (:ELEMENT_TYPE_NAME, :ELEMENT_TAG, :DATA_TYPE_ID, :IS_PARENT)
        """

        response = None

        print element_type

        try:
            if element_type["ELEMENT_TYPE_ID"] > 0:
                print "Update", __update_query
                self.__db.execute(__update_query, element_type, True)
            else:
                del element_type["ELEMENT_TYPE_ID"]
                print "Insert", element_type
                self.__db.execute(__insert_query, element_type, True)
            response = dict(error=0, text="success")
        except Exception as e:
            print e
            response = dict(error=0001, text="There was an error saving")

        return response

    def delete_element_type(self, id_element_type):
        """
        delete an element with a given id if id_element_type is None then I will return an error
        """
        if not id_element_type:
            return dict(error=0002, text="There was an error deleting")

        __delete_query = """DELETE FROM ELEMENT_TYPES
                            WHERE ELEMENT_TYPE_ID = :ELEMENT_TYPE_ID
                         """

        response = {}

        try:
            self.__db.execute(__delete_query, dict(
                ELEMENT_TYPE_ID=id_element_type), True)
            response = dict(error=0, text="success")
        except Exception:
            response = dict(error=0002, text="There was an error deleting")

        return response


    def get_data_types(self, filters=None):
        """
        get data_types in data base with filters
        """
        __query = "SELECT * FROM DATA_TYPES"

        if not filters:
            filters = {}
        else:
            __query += " WHERE "
            for key in filters:
                __query += key + " = :" + key

        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_data_type(self, data_type):
        """
        save_data_type
        """
        __update_query = """UPDATE DATA_TYPES
                            SET DATA_TYPE_NAME = :DATA_TYPE_NAME,
                                TABLE_ELEMENT = :TABLE_ELEMENT
                            WHERE DATA_TYPE_ID = :DATA_TYPE_ID
        """

        __insert_query = """INSERT INTO
                            DATA_TYPES(DATA_TYPE_NAME, TABLE_ELEMENT) 
                            VALUES (:DATA_TYPE_NAME, :TABLE_ELEMENT)
        """

        response = None

        try:
            if data_type["DATA_TYPE_ID"] > 0:
                print "Update", __update_query
                self.__db.execute(__update_query, data_type, True)
            else:
                print "Insert", __insert_query
                del data_type["DATA_TYPE_ID"]
                self.__db.execute(__insert_query, data_type, True)
            response = dict(error=0, text="success")
        except Exception as e:
            print e
            response = dict(error=0001, text="There was an error saving")

        return response


    def delete_data_type(self, id_data_type):
        """
        delete an element with a given id if id_data_type is None then I will return an error
        """
        if not id_data_type:
            return dict(error=0002, text="There was an error deleting")

        __delete_query = """DELETE FROM DATA_TYPES
                            WHERE DATA_TYPE_ID = :DATA_TYPE_ID
                         """

        response = {}

        try:
            self.__db.execute(__delete_query, dict(DATA_TYPE_ID=id_data_type), True)
            response = dict(error=0, text="success")
        except Exception:
            response = dict(error=0002, text="There was an error deleting")

        return response
