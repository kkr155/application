# 不使用域名的服务器部署方式db.init_app(app)
from flask import Flask

from utils import resource_path

from database import db

from routes import main as main_routes

app = Flask(__name__,
            template_folder=resource_path('templates'),
            static_folder=resource_path('static'))


# 配置 SQLite 数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy
db.init_app(app)


# @app.before_first_request 装饰器标记的函数会在服务器接收到第一个 HTTP 请求之前被调用一次
@app.before_request
def create_tables():
    if not app.config['APP_ALREADY_STARTED']:
        db.create_all()
        app.config['APP_ALREADY_STARTED'] = True


app.register_blueprint(main_routes)  # 注册蓝图


if __name__ == '__main__':
    app.config['APP_ALREADY_STARTED'] = False   # 初始化变量
    app.run(host='0.0.0.0', port=5000, debug=True)



