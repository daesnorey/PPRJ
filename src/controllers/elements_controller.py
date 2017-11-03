"""
elements_controller.py
This file will handle every possible action for the elements
"""


class ElementsController(object):
    """
    Class ElementsController will handle the CRUD structure
    """

    def __init__(self, action):
        self.action = action

    def evaluate(self):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
        action = self.action

        print(action)

        if action is 'create':
            pass
        elif action is 'update':
            pass
        elif action is 'delete':
            pass
        else:
            pass

    def evaluate2(self):
        """
        Metodo que evalua la accion a realizar y ejecuta los metodos pertinentes
        """
