#server.py
#Author: DNR

from bottle import route, run

@route("/")
def index():
    return "<p>Hello World!"


run(host='localhost', port=1993, debug=True)