import os
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db, models


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()




    def test_create_account(self):

        response = self.app.post('/create_account', data=dict(firstname='Hammad', surname='surname',Username='testuser',
                                                             Password='test', Password2='test', Email='test@gmail.com'), follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.post('/', data=dict(Username='testuser', Password='test'), follow_redirects=True)



        self.assertEqual(response.status_code, 200)

    def test_Change_Password(self):
        response = self.app.post('/Add_Intake/testuser', data=dict(Password='test1', Password2='test1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Add_Intake(self):
        response = self.app.post('/Add_Intake/testuser', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Show_Intake(self):
        response = self.app.post('/Show_Intake/testuser', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Add_Category(self):
        response = self.app.post('/Add_Category/testuser', data=dict(category_title='Vegetables'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_Show_Category(self):
        response = self.app.post('/Show_Category/testuser', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Show_Category(self):
        response = self.app.post('/Show_Category/testuser', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Add_Exercise(self):
        response = self.app.post('/Add_Exercise/testuser', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_Show_Exercise(self):
        response = self.app.post('/Show_Exercise/testuser', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        db.session.remove()
        db.drop_all()