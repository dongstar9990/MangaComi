from source import db,app
from source.main.model.groups import Groups
from source.main.model.members import Members
from flask_jwt_extended import jwt_required
from flask import request, make_response, jsonify
from sqlalchemy import text
import jwt

@jwt_required()
def handleNotesGroup(idNote):
    pass


@jwt_required()
def createGroup():
    try:
        json = request.json
        # giải mã authen
        bearer = request.headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split(' ')[1]
        decoded_data = jwt.decode(jwt=token,
                        key=app.config["SECRET_KEY"],
                        algorithms=["HS256"])
        owner=decoded_data['sub']['id']
        groupFilter = Groups.query.filter_by(idOwner=owner).first()
        if (groupFilter):
            return make_response(jsonify({'status': 200, 'message': 'Group name was exist'}), 400)
        else:
            group = Groups(
                name=json["name_group"], idOwner=owner, describe=json["describe_group"])
            db.session.add(group)
            db.session.commit()
            for mem in json["members"]:
                member = Members(idGroup=group.idGroup,
                                 idUser=mem['id'], role=mem["role"])
                db.session.add(member)
            db.session.commit()
            return {'status': 200, 'message': 'Group was created successfully'}
    except:
        return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)


@jwt_required()
def addMembers(idGr):
    try:
        json = request.json

        def getIdUser(user):
            return {"id": user.id, "role": user["role"]}
        memberId = map(getIdUser, json["member"])
        for mem in memberId:
            member = Members(idGroup=idGr, idUser=mem.id, role=mem.role)
            db.session.add(member)
        db.session.commit()
        return {'status': 200, 'message': 'Member was added successfully'}
    except:
        return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)


@jwt_required()
def quitMembers():
    pass
