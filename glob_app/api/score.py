from flask import jsonify,request
from sqlalchemy import desc
from .. import db
from ..models import User
from . import api
from .errors import forbidden

@api.route('/postscore/',methods=['POST'])
def update_score():
    new_score=request.get_json().get('score')
    username=request.get_json().get('id')
    token=request.headers.get('token')
    current_user=User.query.filter_by(username=username).first_or_404()
    if  current_user.verify_auth_token(token):
        current_user.score+=int(new_score)
        db.session.add(current_user)
        db.session.commit()
        response=jsonify({"ok"})
        response.status_code=200
        return response
    else:return forbidden("forbidden")

@api.route('/getscore/',methods=['GET'])
def get_scoreboard():
    topUsers = User.query.order_by(desc(User.score), User.username).limit(10)
    board=[{"id": u.username,"score": u.score} for u in topUsers]
    return jsonify({"board": board}),200


