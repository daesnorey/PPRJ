import sys
sys.path.insert(0, "src/services/db")
from oracle import Oracle

class ModelsService(object):
    """
    ModelsService class
    """

    def __init__(self):
        self.__db = Oracle()

    def get_models(self, filters=None):
        """
        get elements in data base with filters
        """
        if filters is None:
            filters = {}
        else:
            pass

        __query = "SELECT * FROM MODELS"
        response = self.__db.execute(__query, filters, True).fetchall()
        print ("msResponse", response)
        return response