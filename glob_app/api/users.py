from flask import jsonify,request,current_app,url_for
from . import api
from .. import db
from ..models import User

@api.route('/signup/',methods=['POST'])
def signup():
    """register api"""
    username=request.get_json().get('id')
    pasword=request.get_json().get('password')
    user=User.query.filter_by(username=username).first()
    if user is None:
        user=User(username=username,password=pasword)
        db.session.add(user)
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
    """login api"""
    username=request.get_json().get('id')
    password=request.get_json().get('password')
    user=User.query.filter_by(username=username).first()
    if user.verify_password(password) :
        token=user.generate_confirmation_token()
        response=jsonify({"token": token})
        response.status_code=200
        return response
    else:
        response=jsonify({})
        response.status_code=400
        return response

