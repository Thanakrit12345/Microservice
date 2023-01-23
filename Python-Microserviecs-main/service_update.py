from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    # Get the user's login information from the request
    user = request.form.get('username')
    passwd = request.form.get('password')
    name = request.form.get('name')

    _user = us.user_name()
    data = [x for x in _user if x["user"]==user]
    # return jsonify(_user)
    #Get Data
    if not data:
        return {"error": "User not found"}, 404

    user = request.form.get('username')
    passwd = request.form.get('password')
    name = request.form.get('name')

    if user:
        data['username'] = user
    if passwd:
        data['password'] = passwd 
    if name:
        data['name'] = name
    return {"message": "User updated successfully"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1