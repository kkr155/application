# 不使用域名的服务器部署方式db.init_app(app)
from flask import Flask


from routes import main as main_routes
from path_util import template_dir, static_dir, project_path
from flask_cors import CORS  # 添加这行

app = Flask(__name__,
            template_folder=str(template_dir),
            static_folder=str(static_dir))

app.register_blueprint(main_routes)  # .\.venv\Scripts\activate注册蓝图
CORS(app)

# def run_flask():
#     app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
