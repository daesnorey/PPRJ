# server.py
# Author: DNR

from sys import path
from bottle import route, run, template
path.insert(0, 'src/controllers')
from elements_controller import ElementsController as ec


@route("/elements")
@route("/elements/<action>")
def elements(action="view"):
    """
    Metodo que manejara el comportamiento de los elementos
    """
    element_controller = ec(action)
    element_controller.evaluate()
    return template("elements_template", name="lol")


if __name__ == "__main__":
    run(host='localhost', port=1993, debug=True, reloader=True)
else:
    run(host='localhost', port=1993, debug=True)
