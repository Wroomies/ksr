import json
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


def get_response(status, body):
    response = make_response(str(body), status)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/auth/tokens', methods=['POST'])
def login():
    req_body = request.get_data()
    req_body = json.loads(req_body)
    return get_response(200, json.dumps(req_body))


if __name__ == '__main__':
    app.run('0.0.0.0', 18080, debug=True, threaded=True)
