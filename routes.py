from flask import send_from_directory, render_template, jsonify, request, Blueprint
from utils import dispose_pdf_name
from database import db
from models import User

main = Blueprint('main', __name__,)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/study')
def study():
    return render_template('study.html')


@main.route('/study/data')
def questions():
    return render_template('questions.json')


@main.route('/pdfs/<path:filename>')
def pdf_show(filename):
    actual_filename = dispose_pdf_name(filename)
    if actual_filename:  # 如果找到对应的文件名
        return send_from_directory('static/pdfs', actual_filename)
    else:
        return "File not found", 404


# 获取所有用户接口
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# 添加用户接口
@main.route('/users/add', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'username is required'}), 400
    # 检查用户名是否已存在
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'username already exists'}), 400
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201
