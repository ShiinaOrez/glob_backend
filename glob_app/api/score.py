from sqlalchemy import desc
from flask import jsonify,request,g,url_for,current_app
from .. import db
from ..models import User
from . import api
from .errors import forbidden

@api.route('/postscore/',methods=['POST'])
def update_score():
    new_score=request.get_json().get('score')
    usrname=request.get_json().get('id')
    usr=User.query.filter_by(username=usrname).first()
    token=request.headers.get('token')
    if usr.confirm(token):
        usr.score+=new_score
        db.session.add(usr)
        db.session.commit()
        response=jsonify({})
        response.status_code=200
        return response
    else:
        response=jsonify({})
        response.status_code=401
        return response

@api.route('/getscore/',methods=['GET'])
def get_scoreboard():
    scoreboard=User.query.order_by(desc(User.score)).all()
    board=list([None,None,None,None,None,None,None,None,None,None,None])
    k=1
    for u in scoreboard:
#        print (k)
        board[k]={
            "id": u.username,
            "score": u.score,
        }
        k+=1
        if k>10 : break
    response=jsonify({"board": board})
    response.status_code=200
    return response
