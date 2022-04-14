from flask      import app, jsonify, request, Flask
from flask_cors import CORS, cross_origin
from shell      import shell, removeYazdir

app = Flask(__name__, static_folder='../frontend/')
CORS(app)

@app.route('/')
def HelloWorld():
    return 'Main Page'

@app.route('/api/code', methods = ['POST'])
@cross_origin()
def api_route():
    code = request.json['code']
    code = removeYazdir(code)
    
    result, error = shell(code)

    if result: 
        distilledRes = []

        for element in result.elements:
            if element != None:
                distilledRes.append(element)

        resultStr = "\n".join(str(x) for x in distilledRes)
        return jsonify(resultStr)
    else: 
        return jsonify(error)