# api/v1/views/session_auth.py
from flask import Blueprint, jsonify, request, abort
from models.user import User
from api.v1.app import auth

session_auth_blueprint = Blueprint('session_auth', __name__)


@session_auth_blueprint.route('/auth_session/login', methods=['POST'])
def login():
    """ Handle login with session authentication. """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search(email=email)
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME', '_my_session_id')
    response.set_cookie(session_name, session_id)
    return response
