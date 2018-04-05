from flask import jsonify,request,g,url_for,current_app
from .. import db
from ..models import User
from . import api
from .errors import forbidden

@api.route('/postscore/',methods=['POST'])
def update_score():
    new_score=request.get_json().get('score')
    usrname=request.get_json().get('id')
    token=request.headers.get('token')
    if usr.confirm(token):
        usr=User.query.filter_by(username=usrname)
        usr.score+=new_score
        db.session.add(usr)
        db.session.commit()
        response=jsonify({})
        response.status_code=200
    else:
        response=jsonify({})
        response.status_code=401
        return response

@api.route('/getscore/',methods=['GET'])
def get_scoreboard():
    scoreboard=db.session.query(User).order_by(User.score).all()
    board=list([None,None,None,None,None,None,None,None,None,None,None])
    k=1
    for u in scoreboard:
        board[k]={
            "id": u.username,
            "score": u.score,
            "rank": k
        }
        k++
    response=jsonify({"board": board})
    response.status_code=200
    return response
