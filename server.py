"""
File server.py
Server web appliation, will take the requests and route them to their controllers
"""

from bottle import route, run, view
from sys import path

path.insert(0, 'src/controllers')
from elements_controller import ElementsController as ec


@route("/elements")
@route("/elements/<action>")
@view("elements_template")
def elements(action="view"):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    element_controller = ec(action)
    element_controller.evaluate()

    return dict({"action": action, "data_e": element_controller.data})

@route("/components")
@route("/components/<action>")
def components(action="view"):
    return "Hello World!" + action

run(host='localhost', port=1010, debug=True, reloader=True)
