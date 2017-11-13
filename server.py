"""
File server.py
Server web appliation, will take the requests and route them to their controllers
"""

from bottle import route, run, view, request, static_file
from src.controllers.elements_controller import ElementsController as ec
from src.controllers.models_controller import ModelsController as mc

@route("/elements")
@route("/elements/<action>")
@route("/elements/<action>/<id_element>")
@view("elements_template")
def elements(action="view", id_element=None):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    element_controller = ec(action)
    element_controller.evaluate_elements(id_element)

    return dict(action=action, data_e=element_controller.data, cols=6)

@route("/elements/<action>/<id_element>", method='POST')
def elements_action(action, id_element):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    print "elements_action", id_element
    element_controller = ec(action)
    element_controller.evaluate_elements(id_element, request)

    return element_controller.response

@route("/element_types")
@route("/element_types/<action>")
@route("/element_types/<action>/<id_type>")
@view("element_types_template")
def element_types(action="view", id_type=None):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    element_controller = ec(action)
    element_controller.evaluate_element_types(id_type)

    return dict(action=action, data_e=element_controller.data, cols=6)


@route("/element_types/<action>/<id_type>", method='POST')
def element_types_action(action, id_type):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    print "elements_action", id_type
    element_controller = ec(action)
    element_controller.evaluate_element_types(id_type, request)

    return element_controller.response

@route("/data_types")
@route("/data_types/<action>")
@route("/data_types/<action>/<id_type>")
@view("data_types_template")
def data_types(action="view", id_type=None):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    element_controller = ec(action)
    element_controller.evaluate_data_types(id_type)

    return dict(action=action, data_e=element_controller.data, cols=6)


@route("/data_types/<action>/<id_type>", method='POST')
def data_types_action(action, id_element):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    print "elements_action", id_element
    element_controller = ec(action)
    element_controller.evaluate_data_types(id_element, request)

    return element_controller.response

@route("/models")
@route("/models/<action>")
@route("/models/<action>/<id_model>")
@view("models_template")
def models(action="view", id_model=None):
    """
    Metodo que manejara el comportamiento de los modelos
    """
    model_controller = mc(action)
    model_controller.evaluate(id_model)

    print model_controller.data

    return dict(action=action, data_e=model_controller.data, cols=12)


@route('/js/<file_name:path>')
def js_loader(file_name):
    """
    import js files
    """
    print file_name
    return static_file(file_name, root='./scripts')


@route('/css/<file_name:path>')
def css_loader(file_name):
    """
    import css files
    """
    return static_file(file_name, root='./styles')

run(host='localhost', port=1991, debug=True, reloader=True)
