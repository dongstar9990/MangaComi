from datetime import datetime
from flask import jsonify, make_response, request
from passlib.hash import pbkdf2_sha256
from sqlalchemy import text

from source import db
from source.main.model.datas import Datas
from source.main.model.notes import Notes


def getNotes(notes):
    data = []
    for note in notes:
        note_parse = {}
        if (note.type == 'checklist'):
            flag = False
            if (len(data) > 0):
                for item in data:
                    if (item['type'] == 'checklist' and item['idNote'] == note.idNote):
                        flag = True
                        item['data'].append(
                            {'content': note.content, 'status': note.doneContent, 'id': note.idData})
            if (flag == False):
                note_parse["idNote"] = note.idNote
                note_parse["type"] = note.type
                note_parse["data"] = [{'content': note.content, 'status': note.doneContent, 'id': note.idData}]
                note_parse["title"] = note.title
                note_parse["doneNote"] = note.doneNote
                note_parse["createAt"] = str(note.createAt)
                note_parse["dueAt"] = str(note.dueAt) if (
                    note.dueAt) else note.dueAt
                note_parse["remindAt"] = str(note.remindAt) if (
                    note.remindAt) else note.remindAt
                note_parse["lock"] = note.lock
                note_parse["pinned"] = note.pinned
                note_parse["idUser"] = note.idUser
                note_parse["color"] = {'r': note.r,
                                       'g': note.g, 'b': note.b, 'a': note.a}
        if (note.type == 'text'):
            note_parse["idNote"] = note.idNote
            note_parse["type"] = note.type
            note_parse["data"] = note.content
            note_parse["title"] = note.title
            note_parse["doneNote"] = note.doneNote
            note_parse["createAt"] = str(note.createAt)
            note_parse["dueAt"] = str(note.dueAt) if (
                note.dueAt) else note.dueAt
            note_parse["remindAt"] = str(note.remindAt) if (
                note.remindAt) else note.remindAt
            note_parse["lock"] = note.lock
            note_parse["pinned"] = note.pinned
            note_parse["idUser"] = note.idUser
            note_parse["color"] = {'r': note.r,
                                   'g': note.g, 'b': note.b, 'a': note.a}
        if (note.type == 'image' or note.type=="screenshot"):
            note_parse["idNote"] = note.idNote
            note_parse["type"] = note.type
            note_parse["data"] = note.content
            note_parse["title"] = note.title
            note_parse["doneNote"] = note.doneNote
            note_parse["createAt"] = str(note.createAt)
            note_parse["dueAt"] = str(note.dueAt) if (
                note.dueAt) else note.dueAt
            note_parse["remindAt"] = str(note.remindAt) if (
                note.remindAt) else note.remindAt
            note_parse["lock"] = None
            note_parse["metaData"] = note.metaData
            note_parse["pinned"] = note.pinned
            note_parse["idUser"] = note.idUser
            note_parse["color"] = {'r': note.r,
                                   'g': note.g, 'b': note.b, 'a': note.a}
        if (bool(note_parse)):
            data.append(note_parse)
    freshData = []
    for note_parse in data:
        if (note_parse['lock']):
            note_parse['lock'] = "*******"
            note_parse['data'] = "Locked"
        freshData.append(note_parse)
    return freshData


def getNote(param, lock=False, babel=False):
    notes = db.session.execute(text(
        'Select * from (select * from notes where notes.idNote={}) as b inner join datas on b.idNote=datas.idNote'.format(param)))
    note_parse = {}

    flag = False

    for note in notes:
        if (note.type == 'checklist'):
            if (flag == False):
                flag = True
                note_parse["idNote"] = note.idNote
                note_parse["type"] = note.type
                note_parse["data"] = []
                note_parse["title"] = note.title
                note_parse["doneNote"] = note.doneNote
                note_parse["createAt"] = str(note.createAt)
                note_parse["dueAt"] = str(note.dueAt) if (
                    note.dueAt) else note.dueAt
                note_parse["remindAt"] = str(note.remindAt) if (
                    note.remindAt) else note.remindAt
                note_parse["lock"] = None
                note_parse["pinned"] = note.pinned
                note_parse["idUser"] = note.idUser
                note_parse["color"] = {'r': note.r,
                                       'g': note.g, 'b': note.b, 'a': note.a}
            if (flag == True):
                note_parse["data"].append(
                    {'content': note.content, 'status': note.doneContent, 'id': note.idData})

        if (note.type == 'text'):
            note_parse["idNote"] = note.idNote
            note_parse["type"] = note.type
            note_parse["data"] = note.content
            note_parse["title"] = note.title
            note_parse["doneNote"] = note.doneNote
            note_parse["createAt"] = str(note.createAt)
            note_parse["dueAt"] = str(note.dueAt) if (
                note.dueAt) else note.dueAt
            note_parse["remindAt"] = str(note.remindAt) if (
                note.remindAt) else note.remindAt
            note_parse["lock"] = None
            note_parse["pinned"] = note.pinned
            note_parse["idUser"] = note.idUser
            note_parse["color"] = {'r': note.r,
                                   'g': note.g, 'b': note.b, 'a': note.a}
        if (note.type == 'image' or note.type == "screenshot"):
            note_parse["idNote"] = note.idNote
            note_parse["type"] = note.type
            note_parse["data"] = note.content
            note_parse["title"] = note.title
            note_parse["doneNote"] = note.doneNote
            note_parse["createAt"] = str(note.createAt)
            note_parse["dueAt"] = str(note.dueAt) if (
                note.dueAt) else note.dueAt
            note_parse["remindAt"] = str(note.remindAt) if (
                note.remindAt) else note.remindAt
            note_parse["lock"] = None
            note_parse["metaData"] = note.metaData
            note_parse["pinned"] = note.pinned
            note_parse["idUser"] = note.idUser
            note_parse["color"] = {'r': note.r,
                                   'g': note.g, 'b': note.b, 'a': note.a}
    if (note.lock):
        if (lock == True or babel == True):
            note_parse['data'] = "Locked"
        note_parse['lock'] = "*******"
    return note_parse


def getOnlyNote(idNote):
    if (request.method == "GET"):
        return {"note": getNote(idNote, babel=True)}


def handleNotes(param):
    if (request.method == "GET"):
        notes = db.session.execute(text(
            'Select * from (select * from notes where notes.idUser={} and notes.inArchived=1) as b inner join datas on b.idNote=datas.idNote'.format(param)))
        return {"notes": getNotes(notes)}

    if (request.method == "POST"):
        try:
            json = request.json
            note_lock = False
            print(json)
            color = json['color']
            date_dueAt = None
            if (json['dueAt']):
                date_dueAt = datetime.strptime(
                    json['dueAt'], "%d/%m/%Y %H:%M %p %z")
            date_rmAt = None
            if (json['remindAt']):
                date_rmAt = datetime.strptime(
                    json['remindAt'], "%d/%m/%Y %H:%M %p %z")
            lockPass = None

            if (json['lock']):
                lockPass = pbkdf2_sha256.hash(json["lock"])

            if (lockPass):
                note_lock = True

            note = {}
            if ("metaData" in json):

                note = Notes(idUser=param, type=json['type'], title=json['title'], pinned=json['pinned'], dueAt=date_dueAt,
                             remindAt=date_rmAt, lock=lockPass, r=color['r'], g=color['g'], b=color['b'], a=color['a'], metaData=json['metaData'])
            else:
                note = Notes(idUser=param, type=json['type'], title=json['title'], pinned=json['pinned'], dueAt=date_dueAt,
                             remindAt=date_rmAt, lock=lockPass, r=color['r'], g=color['g'], b=color['b'], a=color['a'])

            db.session.add(note)

            db.session.commit()
            if (json['type'] == 'checklist'):
                for each in json['data']:
                    data = Datas(idNote=note.idNote,
                                 content=each['content'], doneContent=each['status'])
                    db.session.add(data)
            else:
                data = Datas(idNote=note.idNote, content=json['data'])
                db.session.add(data)
            db.session.commit()
            return {'status': 200, 'message': 'Note was created successfully', 'note': getNote(note.idNote, note_lock)}
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)
    if (request.method == "PATCH"):
        try:
            json = request.json

            note_query = Notes.query.get(param)

            for key in list(json.keys()):
                if (key == 'dueAt'):
                    date_dueAt = None
                    if (json['dueAt']):
                        date_dueAt = datetime.strptime(
                            json['dueAt'], "%d/%m/%Y %H:%M %p %z")

                    note_query.dueAt = date_dueAt
                if (key == 'remindAt'):
                    date_rmAt = None
                    if (json['remindAt']):
                        date_rmAt = datetime.strptime(
                            json['remindAt'], "%d/%m/%Y %H:%M %p %z")
                    note_query.dueAt = date_rmAt
                if (key == 'color'):
                    color = json['color']
                    note_query.r = color['r']
                    note_query.g = color['g']
                    note_query.b = color['b']
                    note_query.a = color['a']
                if (key == 'title'):
                    note_query.title = json['title']
                if (key == 'data'):

                    if (json['type'] == 'text'):
                        note_data = Datas.query.filter(
                            Datas.idNote == param).first()

                        note_data.content = json['data']
                        db.session.add(note_data)

                    if (json['type'] == 'checklist'):
                        trunc_data = Datas.query.filter(
                            Datas.idNote == param).all()
                        for item in trunc_data:
                            db.session.delete(item)
                        db.session.commit()
                        for edit in json['data']:
                            data = Datas(idNote=param,
                                         content=edit['content'], doneContent=edit['status'])
                            db.session.add(data)

                if (key == 'pinned'):
                    note_query.pinned = json['pinned']
                if (key == 'lock'):
                    lockPass = None

                    if (json['lock']):
                        lockPass = pbkdf2_sha256.hash(json["lock"])
                    note_query.lock = lockPass

            db.session.add(note_query)
            db.session.commit()
            return {'status': 200, 'message': 'Note was updated successfully', 'note': getNote(note_query.idNote, False)}
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)
    if (request.method == 'DELETE'):
        try:

            note_query = db.session.query(
                Notes).filter_by(idNote=param).first()
            note_query.inArchived = False
            note_lock = False
            if (note_query.lock):
                note_lock = True
            db.session.add(note_query)
            db.session.commit()
            return {'status': 200, 'message': 'Note was deleted successfully', 'note': getNote(note_query.idNote, note_lock)}
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)


def tickerBox(idData):
    if (request.method == 'PATCH'):
        try:
            data = Datas.query.filter(Datas.idData == idData).first()
            data.doneContent = not data.doneContent
            db.session.add(data)
            db.session.commit()
            return {'status': 200, 'message': 'Note was update successfully'}
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)


def delTruncNote(id):
    if (request.method == 'DELETE'):
        try:
            note_query = db.session.query(Notes).filter_by(idNote=id).first()
            print(note_query)
            db.session.delete(note_query)
            db.session.commit()
            return {'status': 200, 'message': 'Note was deleted successfully', }
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)


def trashGet(idUser):
    if (request.method == "GET"):
        notes = db.session.execute(text(
            'Select * from (select * from notes where notes.idUser={} and notes.inArchived=0) as b inner join datas on b.idNote=datas.idNote'.format(idUser)))

        return {"notes": getNotes(notes)}


def trashRestore(id):
    if (request.method == "POST"):
        try:
            note_query = db.session.query(Notes).filter_by(idNote=id).first()
            note_query.inArchived = True
            db.session.add(note_query)
            db.session.commit()
            return {'status': 200, 'message': 'Note was restore successfully', "note": getNote(note_query.idNote)}
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)


def getLastNote():
    try:
        if (request.method == "GET"):

            sql = db.session.execute(text(
                'select max(idNote) as MaxId  from notes'))
            for note in sql:
                return {'status': 200,  "idNoteLast": note.MaxId}
    except:
        return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)


def openLock(idNote):
    try:
        if (request.method == "POST"):
            json = request.json
            Note = Notes.query.filter(
                Notes.idNote == idNote).first()
            if (pbkdf2_sha256.verify(json["pass_lock"], Note.lock)):
                return {'status': 200, 'note': getNote(idNote, False), "pass_lock": json["pass_lock"]}
            else:
                return make_response(jsonify({'status': 400, 'message': 'Password not true'}), 400)

    except:
        return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)
