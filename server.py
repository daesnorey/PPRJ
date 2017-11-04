"""
File server.py
Server web appliation, will take the requests and route them to their controllers
"""

from bottle import route, run, view
from sys import path

path.insert(0, 'src/controllers')
from elements_controller import ElementsController as ec
from models_controller import ModelsController as mc


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

<<<<<<< HEAD
run(host='localhost', port=1010, debug=True, reloader=True)
=======
@route("/models")
@route("/models/<action>")
def models(action="view"):
    """
    Metodo que manejara el comportamiento de los modelos
    """
    model_controller = mc(action)
    model_controller.evaluate()

run(host='localhost', port=1993, debug=True, reloader=True)
>>>>>>> b68b8872ae71a933a494c97866048c719c03f60c
