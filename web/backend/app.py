from flask import app, jsonify, request, Flask
from flask_cors import CORS

from shell import shell

app = Flask(__name__, static_folder='../frontend/')
CORS(app)

@app.route('/')
def HelloWorld():
    result, error = shell('Hello World!')
    print(result)
    return 'Main Page'

@app.route('/api/code', methods = ['POST'], strict_slashes = False)
def api_route():
    code = request.json['code']
    print(code)
    #! You can return the response here after compiling the code
    return jsonify (code)