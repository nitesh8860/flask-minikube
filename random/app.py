from flask import Flask, jsonify, abort, request
import random


app = Flask(__name__)


@app.route('/random', methods=['GET'])
def rand():
    return str(random.randint(1,210000000000000000  ))

@app.route('/api', methods=['POST'])
def string_reverse():
    if not request.json:
        abort(400)
    return jsonify({'message': str(request.get_json()['message'])[::-1], 'random': str(random.randint(1,2100000000000)) })



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

