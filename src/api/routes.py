"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)


@api.route("/token", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email, password=password).first()

    if user is None:
        return jsonify({"msg": "Bad email or password"}), 401

    id = user.id

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token, id=id, email=email)


@api.route("/signup", methods=['POST'])
def sign_up():
    data = request.get_json()

    if data['email'] is None:
        return jsonify({"msg": "email not entered"}), 401
    elif data['password'] is None:
        return jsonify({"msg": "password not entered"}), 401
    else: 
        new_user = User(email = data['email'], password = data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.serialize()), 200

@api.route("/user/<int:id>", methods=["GET"])
@jwt_required()
def get_a_user(id):

   userInfo= User.query.get(id)
   if userInfo is None:
    return 'User not found', 404

   return jsonify({'user': [userInfo.serialize()]}), 200
