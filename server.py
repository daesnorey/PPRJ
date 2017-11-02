#server.py
#Author: DNR

from bottle import route, run, template, request
import sys

sys.path.insert(0, 'src/controllers')

from action_controller import ActionController as ac

@route("/models")
@route("/models/<action>")
def model_action(action = "view"):
    request.get("attr")
    action_controller = ac(action)
    action_controller.greeting()
    return template('template_action', action = action)

@route("/")
def index():
    return "<p>Hello World!</p>"


run(host='localhost', port=1993, debug=True)