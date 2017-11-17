"""server.py.

Server web appliation, will take the requests and route them to their
controllers
"""


from bottle import route, run, view, request, static_file
from src.controllers.elements_controller import ElementsController as ec
from src.controllers.components_controller import ComponentsController as cc
from src.controllers.models_controller import ModelsController as mc
from src.objects.action import Action as actions


@route("/elements")
@route("/elements/<action>")
@route("/elements/<action>/<id_element>")
@view("elements_template")
def elements(action="view", id_element=None):
    """Metodo que manejara el comportamiento de los elementos."""
    element_controller = ec(action)
    element_controller.evaluate_elements(id_element)

    return dict(action=action, data_e=element_controller.data, cols=6)


@route("/elements/<action>/<id_element>/childs")
@view("elements_template")
def element_childs(action, id_element):
    """element_childs.

    element_childs method will handle every behaviour with the childrens
    of a specific element
    """
    element_controller = ec(action)
    element_controller.evaluate_elements(id_element, is_parent=True)

    return "Hello world" + id_element


@route("/elements/<action>/<id_element>", method='POST')
def elements_action(action, id_element):
    """Metodo que manejara el comportamiento de los elementos."""
    print "elements_action", id_element
    element_controller = ec(action)
    element_controller.evaluate_elements(id_element, request)

    return element_controller.response


@route("/element_types")
@route("/element_types/<action>")
@route("/element_types/<action>/<id_type>")
@view("element_types_template")
def element_types(action="view", id_type=None):
    """Metodo que manejara el comportamiento de los elementos."""
    element_controller = ec(action)
    element_controller.evaluate_element_types(id_type)

    return dict(action=action, data_e=element_controller.data, cols=6)


@route("/element_types/<action>/<id_type>", method='POST')
def element_types_action(action, id_type):
    """Metodo que manejara el comportamiento de los elementos."""
    print "elements_action", id_type
    element_controller = ec(action)
    element_controller.evaluate_element_types(id_type, request)

    return element_controller.response


@route("/data_types")
@route("/data_types/<action>")
@route("/data_types/<action>/<id_type>")
@view("data_types_template")
def data_types(action="view", id_type=None):
    """Metodo que manejara el comportamiento de los elementos."""
    element_controller = ec(action)
    element_controller.evaluate_data_types(id_type)

    return dict(action=action, data_e=element_controller.data, cols=6)


@route("/data_types/<action>/<id_type>", method='POST')
def data_types_action(action, id_type):
    """Metodo que manejara el comportamiento de los elementos."""
    print "elements_action", id_type
    element_controller = ec(action)
    element_controller.evaluate_data_types(id_type, request)

    return element_controller.response


@route("/components")
@route("/components/<action>")
@route("/components/<action>/<id_component>")
@view("components_template")
def components(action="view", id_component=None):
    """Method will handle the component's behaviour."""
    component_controller = cc(action)
    component_controller.evaluate(id_component)

    return dict(action=action, data_e=component_controller.data, cols=6)


@route("/components/<action>/<id_component>", method='POST')
def components_action(action, id_component):
    """Method will handle the component's behaviour."""
    print "component_controller", id_component
    component_controller = cc(action)
    component_controller.evaluate(id_component, request)

    return component_controller.response


@route("/components/<id_component>/elements/<action>")
@view("elements_template")
def component_elements(id_component, action=actions.VIEW):
    """Component elements."""
    __elements = cc(action).get_elements(id_component)

    elements_controller = ec(action)
    elements_controller.evaluate_elements()
    __data = elements_controller.data
    print "__data", __data
    __data["elements"] = __elements

    print __data, action

    return dict(action=action, data_e=__data, cols=12, embed=True, id_component=id_component)


@route("/components/<id_component>/elements/<action>", method='POST')
def component_elements_action(id_component, action):
    """Method component_elements_action."""

    components_controller = cc(action)
    components_controller.evaluate(id_component, request, True)
    return components_controller.response


@route("/models")
@route("/models/<action>")
@route("/models/<action>/<id_model>")
@view("models_template")
def models(action="view", id_model=None):
    """Metodo que manejara el comportamiento de los modelos."""
    model_controller = mc(action)
    model_controller.evaluate(id_model)

    print model_controller.data

    return dict(action=action, data_e=model_controller.data, cols=12)


@route("/models/<action>/<id_model>", method='POST')
def models_action(action, id_model):
    """Metodo que manejara el comportamiento de los modelos."""
    print "models_action", id_model
    model_controller = mc(action)
    model_controller.evaluate(id_model, request)

    return model_controller.response


@route("/")
@view("index_template")
def index():
    """Initial page, it contains links to go in a fast way to other pages."""
    return dict()


@route('/js/<file_name:path>')
def js_loader(file_name):
    """Import js files."""
    print file_name
    return static_file(file_name, root='./scripts')


@route('/css/<file_name:path>')
def css_loader(file_name):
    """Import css files."""
    return static_file(file_name, root='./styles')


run(host='localhost', port=2023, debug=True, reloader=True)
