from flask import jsonify,request,current_app,url_for
from . import api
from .. import db
from ..models import User

@api.route('/signup/',methods=['POST'])
def signup():
    usrname=request.get_json().get('id')
    pasword=request.get_json().get('password')
    usr=User.query.filter_by(username=usrname).first()
    if usr is None:
        usr=User(username=usrname,password=pasword,score=0)
        db.session.add(usr)
        db.session.commit()
        response=jsonify({"msg": "successful!"})
        response.status_code=200
        return response
    else :
        response=jsonify({})
        response.status_code=401
        return response

@api.route('/signin/',methods=['POST'])
def signin():
    usrname=request.get_json().get('id')
    pasword=request.get_json().get('password')
    usr=User.query.filter_by(username=usrname).first()
    if usr.verify_password(pasword) :
        token=usr.generate_confirmation_token()
        response=jsonify({"token": token})
        response.status_code=200
        return response
    else:
        response=jsonify({})
        response.status_code=400
        return response

