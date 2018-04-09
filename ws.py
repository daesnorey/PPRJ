"""ws.py.

web service application, will take the requests and route them to their
controllers
"""

import json

from bottle import Bottle, route, run, view, request, response, static_file
from src.controllers.ws_controller import WsController
from src.utils.datetime_encoder import DatetimeEncoder

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

@app.route("/third-party")
@app.route("/third-party/<ext>")
def third_party(ext="third"):
    result = ws_controller.get(ext, request.query)
    return json.dumps(result, cls=DatetimeEncoder, default=DatetimeEncoder.jsonDefault)


if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost",
                      help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=2900,
                      help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port))
    #run(host='localhost', port=2900, debug=True, reloader=True)