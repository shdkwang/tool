#!flask/bin/python
from flask import Flask
from flask import make_response
from flask import abort
from flask import jsonify
from flask import request
import json
import processquery as pq 
import sys
import confparser as cp
import os
import aggtree

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.errorhandler(404)
def not_found (error):
    return make_response (json.dumps ({'error': 'Not found'}), 404)

@app.route('/pathdump', methods=['POST'])
def getpathdumppost():
    if not request.json or not 'api' in request.json:
        abort (404)
    else:
        content = pq.handlerequest (request.json, "pathdump")
        return content

@app.route('/pathdump', methods=['GET'])
def getpathdumpget():
    if not request.json or not 'api' in request.json:
        abort(404)
    else:
        content = pq.handlerequest (request.json, "pathdump")
        return content

def initialize ():
    if len (sys.argv) == 2:
        cp.parse_config (sys.argv[1])

    # create app repository if it doesn't exist
    if not os.path.exists (cp.options['home']+'/'+cp.options['repository']):
        os.makedirs (cp.options['home']+'/'+cp.options['repository'])

    # create flowrecord collection directory if it doesn't exist
    if not os.path.exists (cp.options['home']+'/'+cp.options['collection']):
        os.makedirs (cp.options['home']+'/'+cp.options['collection'])

    aggtree.buildGroupTree (cp.options['home']+'/'+cp.options['grouptree'])

if __name__ == '__main__':
    initialize ()
    app.run (debug = True, host = "0.0.0.0")

    # TODO: Run tests in a host OS
    # app.run (debug = True, host = "0.0.0.0", processes = 2)
