import sys
sys.path.insert(0, "src/services/db")
from oracle import Oracle

class ModelsService(object):
    """
    ModelsService class
    """

    def __init__(self):
        self.__db = Oracle()

    def get_models(self, filters):
        """
        get models in data base with filters
        """
        print "filters:", filters
        __query = "SELECT * FROM MODELS"

        if not filters:
            filters = {}
        else:
            __query += " WHERE "
            for key in filters:
                __query += key + " = :" + key

        print __query
        response = self.__db.execute(__query, filters, True).fetchall()
        print ("msResponse", response)
        return response