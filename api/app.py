from flask import Flask, jsonify, abort, request
import requests, random, json


app = Flask(__name__)

@app.route('/random', methods=['GET'])
def rand():
    return str(random.randint(1,210000000000000000  ))

@app.route('/api', methods=['POST'])
def string_reverse():
    if not request.json:
        abort(400)
    api_url = 'http://flask-reverse.default.svc.cluster.local:5000/reverse'
    headers = {'Content-Type': 'application/json'}
    payload = request.get_json()
    data = json.dumps(payload)
    response = requests.post(api_url, headers=headers, data=data).json()
    return jsonify( { 'message' : response['message'] , 'rand': str(random.randint(1,2100000000000)) } )



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

