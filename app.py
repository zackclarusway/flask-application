from flask import Flask
from flask import request

# http://127.0.0.1:5000/home -> Base URL
# http://127.0.0.1:5000/users/2

app = Flask(__name__)


@app.route('/home')
def index():
    return "Hello Flask"


@app.route('/users/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def parameter(user_id):
    if request.method == 'GET':
        return 'GET Method'

    elif request.method == 'POST':
        data = request.form
        return data
        # return 'POST Method'

    elif request.method == 'PUT':
        return 'PUT Method'

    elif request.method == 'DELETE':
        return 'DELETE Method'

    else:
        return 'Not allowed method'

    # return user_id


app.run()