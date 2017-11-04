"""
elements_service.py
file
"""

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
        if filters is None:
            filters = {}

        __query = "SELECT * FROM ELEMENTS"
        response = self.__db.execute(__query, filters, True).fetchall()
        return response
