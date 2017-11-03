#server.py
#Author: DNR

from sys import path
from bottle import route, run, template
path.insert(0, 'src/controller')
from action_controller import ActionController as ac


@route("/models/<action>")
def model_action(action):
    """
    Metodo ejecutado cuando se entra por models
    """
    action_controller = ac(action)
    action_controller.greeting()
    return template('template_action', action=action)

if __name__ == "__main__":
    run(host='localhost', port=1993, debug=True, reloader=True)
else:
    run(host='localhost', port=1993, debug=True)
