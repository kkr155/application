from flask import Blueprint
from database import db


# 定义一个模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.username}


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # multiple-choice 选择题 multiple-choice 填空题 multiple-choice 判断题
    type = db.Column(db.String(80), unique=True, nullable=False)
    question = db.Column(db.String(80), unique=True, nullable=False)
    options = db.Column(db.String(80), unique=True, nullable=False)
    answer = db.Column(db.String(80), unique=True, nullable=False)
