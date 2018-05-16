"""ws.py.

web service application, will take the requests and route them to their
controllers
"""

import json
import logging
from waitress import serve

from bottle import Bottle, route, run, view, request, response, static_file
from src.controllers.ws_controller import WsController
from src.utils.datetime_encoder import DatetimeEncoder

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Bottle()

ws_controller = WsController()

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route("/<method>")
@app.route("/<method>/<ext>")
def get(method="all",ext=None):
    if ext: method += "_{}".format(ext)
    result = ws_controller.get(method, request.query)
    return json.dumps(result, cls=DatetimeEncoder, default=DatetimeEncoder.jsonDefault)

@app.route("/<method>", method="POST")
@app.route("/<method>", method="OPTIONS")
@app.route("/<method>/<ext>", method="POST")
@app.route("/<method>/<ext>", method="OPTIONS")
def save(method, ext=None):
    if not request.json:
        print(response.status)
        response.status = 200
        return

    if ext: method += "_{}".format(ext)
    result = ws_controller.save(method, request.json, request.files, request.is_ajax, request.is_xhr)
    return result

@app.route("/<method>", method="DELETE")
@app.route("/<method>/<ext>", method="DELETE")
def delete(method, ext=None):
    if ext: method += "_{}".format(ext)
    result = ws_controller.delete(method, request.query)
    return result

if __name__ == "__main__":
    #from paste import httpserver
    #httpserver.serve(app, host='0.0.0.0', port=2900)
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost",
                      help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=2900,
                      help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port), workers=8)
    #run(host='localhost', port=2900, debug=True, server='paste', threaded=True)
    #serve(app, listen='0.0.0.0:2900')
    #run(host='0.0.0.0', port=2900, server='waitress', workers=4)