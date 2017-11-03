#server.py
#Author: DNR

import sys
<<<<<<< HEAD
sys.path.insert(0, 'src/controller')

from indexController import IndexController
from bottle import route, run

@route("/")
def index():
    controller = IndexController()
    return controller.greeting()
=======

sys.path.insert(0, 'src/controllers')

from bottle import route, run, template
from action_controller import ActionController as ac

@route("/models/<action>")
def model_action(action):
    action_controller = ac(action)
    action_controller.greeting()
    return template('template_action', action = action)

@route("/models")

@route("/")
def index():
    return "<p>Hello World!</p>"

>>>>>>> b1a8e1aa518726541b83ec14ff8752bc76f38e55

if __name__ == "__main__":
    run(host='localhost', port=1993, debug=True, reloader=True)
else:
    run(host='localhost', port=1993, debug=True)