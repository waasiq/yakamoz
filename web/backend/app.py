from flask import app, jsonify, request, Flask
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend/')
CORS(app)

@app.route('/')
def HelloWorld():
    return 'Hello World'

@app.route('/api/code', methods = ['POST'], strict_slashes = False)
def api_route():
    code = request.json['code']
    print(code)
    #! You can return the response here after compiling the code
    return jsonify (code)