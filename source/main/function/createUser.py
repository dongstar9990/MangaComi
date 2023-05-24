from source import db
from source.main.model.users import Users

from passlib.hash import pbkdf2_sha256



def createUser(data):
    json = data
    user_name=Users(user_name=json['user_name'],name=json['name'], gmail=json['gmail'], password_hash=pbkdf2_sha256.hash(json["password"]))
    db.session.add(user_name)
    db.session.commit()
