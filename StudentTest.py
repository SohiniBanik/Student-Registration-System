import unittest
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import Student
#Test Cases
class TestStudent(unittest.TestCase):
    def app_mock(self):
        app_mock=Flask(__name__)
        db=SQLAlchemy(app_mock)
        db.init_app(app_mock)
        return app_mock
    def Testadd(self):
        x=Student()
        t=x.add_Students("1,abc,abc@,male,2000-04-09,0123456789,india")
        self.assertEquals(t,"Success","Record has been inserted")

if __name__=='__main__':
    unittest.main()