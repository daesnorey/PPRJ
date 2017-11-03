#server.py
#Author: DNR

import sys
sys.path.insert(0, 'src/controller')

from indexController import IndexController
from bottle import route, run

@route("/")
def index():
    controller = IndexController()
    return controller.greeting()

if __name__ == "__main__":
    run(host='localhost', port=1993, debug=True, reloader=True)
else:
    run(host='localhost', port=1993, debug=True)