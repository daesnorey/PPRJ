"""
components_service.py
Contain the possible actions on the components
"""

from src.services.db.oracle import Oracle

class  ComponentsService(object):
    """
    ComponentsService class
    """

    def __init__(self):
        self.__db = Oracle()

    def get_components(self, filters=None):
        """
        get components in DB with the filters
        """
        __query = "SELECT * FROM COMPONENTS"

        if not filters:
            filters = {}
        else:
            __query += " WHERE "
            for key in filters:
                __query += key + " = :" + key
        
        print __query

        response = self.__db.execute(__query, filters, True).fetchall()
        return response

    def save_component(self, component):
        """
        save_component
        """
        __update_query = """UPDATE COMPONENTS
                            SET COMPONENT_NAME = :COMPONENT_NAME,
                                IS_GENERIC = :IS_GENERIC,
                                IS_ACTIVE = :IS_ACTIVE
                            WHERE COMPONENT_ID = :COMPONENT_ID
        """    

        __insert_query = """INSERT INTO
                            COMPONENTS(COMPONENTS_NAME, IS_ACTIVE, IS_CONTAINER)
                            VALUES (:COMPONENTS_NAME, :IS_ACTIVE, :IS_GENERIC)
        """

        response = None

        try:
            if component["COMPONENT_ID"] > 0:
                print "Update", __update_query
                self.__db.execute(__update_query, component, True)
            else:
                print "Insert"
                del component["COMPONENT_ID"]
                self.__db.execute(__insert_query, component, True)
            response = dict(error=0, text="success")
        except Exception as e:
            print e
            response = dict(error=0010, text="An error took event while it was saving a component")

        return response

    