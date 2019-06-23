from flask import Flask, jsonify, abort, request
import random


app = Flask(__name__)



@app.route('/reverse', methods=['POST'])
def string_reverse():
    if not request.json:
        abort(400)
    return jsonify({'message': str(request.get_json()['message'])[::-1] })



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

