from source import db
from source.main.model.users import Users
from flask import jsonify, request, make_response
from passlib.hash import pbkdf2_sha256
from source import app
from flask_jwt_extended import create_access_token
from sqlalchemy import or_

def loginUser():
    if (request.method == 'POST'):
        json = request.json
        try:
            User = Users.query.filter(
                or_(Users.user_name == json["user_name"],Users.gmail == json["user_name"])).first()
            if (User):
                if (pbkdf2_sha256.verify(json["password"], User.password_hash)):
                    return {'status': 200, 'message': 'Login successfully', 'user': {'id': User.id, 'name': User.name, 'gmail': User.gmail,"password_2":User.password_hash_2, 'df_color': {'r': User.r,
                                                                                                                                                         'g': User.g, 'b': User.b, 'a': User.a},
                                                                                     'df_screen': User.df_screen}, 'jwt': create_access_token(identity={'id': User.id, 'gmail': User.gmail})}, 200
            return make_response(jsonify({'status': 400, 'message': 'Password or user name has some wrong'}), 400)
        except:
            return make_response(jsonify({'status': 400, 'message': 'Password or user name has some wrong'}), 400)
