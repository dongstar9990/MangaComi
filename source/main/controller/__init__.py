from source import app
from source.main.controller.notes import *
from source.main.controller.users import *

from source.main.controller.groups import *
from flask_jwt_extended import create_access_token, get_jwt_identity


@app.route('/')
def reader():
    return '<a href="/docs">/docs</a> to read the documentation'

@app.route('/refresh_token', methods=['POST'])
def refresh_token():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}, 200