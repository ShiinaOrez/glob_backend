import unittest
import os
from glob_app import  create_app,db
from flask import current_app, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import json
class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(os.getenv('FLASK_CONFIG') or 'default')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)


    #----------API FILE NAME:/home/shiina/glob_backend/glob_app/api//score.py-------------------

    #Test update_score
    def test_c_update_score(self):
        response = self.client.post(
            url_for('api.update_score',_external=True),
            data = json.dumps({
                "score":50,
                "id":'shiina',
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    #Test get_scoreboard
    def test_d_get_scoreboard(self):
        response = self.client.get(
            url_for('api.get_scoreboard',_external=True),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)


    #----------API FILE NAME:/home/shiina/glob_backend/glob_app/api//__init__.py-------------------


    #----------API FILE NAME:/home/shiina/glob_backend/glob_app/api//errors.py-------------------


    #----------API FILE NAME:/home/shiina/glob_backend/glob_app/api//users.py-------------------

    #Test signup
    def test_a_signup(self):
        response = self.client.post(
            url_for('api.signup',_external=True),
            data = json.dumps({
                "id":'shiina',
                "password":'mashiro',
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    #Test signin
    def test_b_signin(self):
        response = self.client.post(
            url_for('api.signin',_external=True),
            data = json.dumps({
                "id":'shiina',
                "password":'mashiro',
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

