from flask import Flask, jsonify, request, Response

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)


@app.route("/users/newuser", methods=['POST'])
def newuser():
    if request.method == 'POST':
        USERS.update(name=request.json['name'])
        return jsonify(USERS.get('name'))
    else:
        return Response(status=404)

@app.route("/users/update", methods=['PUT'])
def updateuser():
    if request.method == 'PUT':
        user = request.json['name1']
        USERS.update('name1', user)
    else:
        return Response(status=404)

@app.route("/users/delete", methods=['DELETE'])
def deleteuser():
    if request.method == 'DELETE':
        user = request.json['name']
        USERS.delete(user)
    else:
        return Response(status=404)

if __name__ == "__main__":
    app.run()