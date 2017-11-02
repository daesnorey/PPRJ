#server.py
#Author: DNR

import sys

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


run(host='localhost', port=1993, debug=True)