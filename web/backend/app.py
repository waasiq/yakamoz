from xml.etree.ElementTree import tostring
from flask import app, jsonify, request, Flask
from flask_cors import CORS

import json as js
import re 

from shell           import shell, fixIf, removeYazdir

app = Flask(__name__, static_folder='../frontend/')
CORS(app)

@app.route('/')
def HelloWorld():
    return 'Main Page'

@app.route('/api/code', methods = ['POST'], strict_slashes = False)
def api_route():
    code = request.json['code']
    code = removeYazdir(code)
    
    result, error = shell(code)

    if result: 
        distilledRes = []

        for element in result.elements:
            if element != None:
                distilledRes.append(element)

        print(distilledRes)
        resultStr = "\n".join(str(x) for x in distilledRes)
        print(jsonify(resultStr))
        return jsonify(resultStr)
    else: 
        print(error)
        return jsonify('Error in program')