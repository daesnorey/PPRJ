"""
File server.py
Server web appliation, will take the requests and route them to their controllers
"""

from bottle import route, run, view, request
from sys import path

path.insert(0, 'src/controllers')
from elements_controller import ElementsController as ec
from models_controller import ModelsController as mc


@route("/elements")
@route("/elements/<action>")
@route("/elements/<action>/<id_element>")
@view("elements_template")
def elements(action="view", id_element=None):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    element_controller = ec(action)
    element_controller.evaluate(id_element)

    return dict(action=action, data_e=element_controller.data,cols=6)


@route("/elements/<action>/<id_element>", method='POST')
def elements_action(action, id_element):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    print "elements_action", id_element
    element_controller = ec(action)
    element_controller.evaluate(id_element, request)

    return element_controller.response

@route("/models")
@route("/models/<action>")
def models(action="view"):
    """
    Metodo que manejara el comportamiento de los modelos
    """
    model_controller = mc(action)
    model_controller.evaluate()

run(host='localhost', port=1993, debug=True, reloader=True)
