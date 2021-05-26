#!/usr/bin/env python3
"""
SQLAlchemy model User
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
app.url_map.strict_slashes = False
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello():
    """ GET /  Return: welcome message """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def register():
    """ POST /users """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ POST /sessions """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ DELETE /sessions """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """ GET /profile  """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """ POST /reset_password  """
    try:
        email = request.form.get('email')
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ PUT /reset_password  """
    try:
        email = request.form.get('email')
        reset_token = request.form.get('reset_token')
        new_password = request.form.get('new_password')
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
