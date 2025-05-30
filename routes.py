import os

from flask import Blueprint, render_template, jsonify, send_file, send_from_directory, request

from werkzeug.utils import secure_filename

from path_util import static_dir

main = Blueprint('main', __name__, )


def response_json_wrapper(func):
    def wrapper(*args, **kwargs):
        # 调用被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 假设函数返回的是一个字典，包含 code, data, message
        if isinstance(result, dict) and 'code' in result and 'data' in result and 'message' in result:
            return jsonify(result), result['code']
        else:
            # 如果不符合预期格式，包装为默认响应
            return jsonify(make_response(data=result)), 200

    return wrapper


def make_response(code=200, data=None, message='success'):
    """
    创建统一的响应格式
    """
    return {
        "code": code,
        "data": data,
        "message": message
    }


@main.before_request
def before_request():
    # 可以在这里添加请求前的处理逻辑，如认证、日志等
    pass


@main.after_request
def after_request(response):
    # 可以在这里添加请求后的处理逻辑
    return response


@main.errorhandler(404)
@response_json_wrapper
def not_found(error):
    print(error)
    return make_response(code=404, data=None, message="资源未找到")


@main.errorhandler(500)
@response_json_wrapper
def internal_error(error):
    print(error)
    return make_response(code=500, data=None, message="服务器内部错误")


# 全局错误处理器
@main.errorhandler(Exception)
@response_json_wrapper
def handle_exception(e):
    if isinstance(e, ValueError):
        return make_response(code=400, data=None, message=str(e))
    print(str(e))
    return make_response(code=500, data=None, message="服务器内部错误")


# 首页
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")


# 简历
@main.route('/resume')
def resume():
    return render_template('resume.html')


# 分发
@main.route('/distribute')
def distribute():
    return render_template("distribute.html")

@main.route('/test')
def test():
    return render_template("test.html")

@main.route('/test_', methods=['GET'])
@response_json_wrapper
def test_():
    return "test"


# 近代史json
@main.route('/json/modern-history')
def new():
    return send_from_directory(
        static_dir,
        'data/modern-history.json',
        mimetype='application/json'
    )

# 近代史word
@main.route('/word/modern-history')
def document_docx():
    return send_file(
        "assets/static/data/modern-history.docx",
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        as_attachment=False  # True 会触发下载，False 直接显示
    )


@main.route('/word/resume')
def document_docx_resume():
    return send_file(
        "assets/static/data/resume.docx",
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        as_attachment=False  # True 会触发下载，False 直接显示
    )

# word文档解析
@main.route('/document/<document_type>')
def document(document_type):
    # 定义合法路径映射
    script_mapping = {
        'modern-history': 'js/modern-history-docx.js',
        'resume': 'js/resume-docx.js',
    }
    script_mapping_css = {
        'modern-history': 'css/modern-history-docx.css',
        'resume': 'css/resume-docx.css',
    }
    # 获取对应的JS路径（默认回退）
    js_path = script_mapping.get(document_type, 'js/default.js')
    css_path = script_mapping_css.get(document_type, 'css/default.css')
    return render_template("document.html", js_path=js_path,css_path=css_path)


# 列表
# @main.route('/table')
# def table():
#     return render_template("table.html")


@main.route('/tables/<table_type>')
def table_show(table_type):
    # 定义合法路径映射
    script_mapping = {
        'modern-history': 'js/modern-history.js',
        'resume': 'js/resume-docx.js',
    }

    # 获取对应的JS路径（默认回退）
    js_path = script_mapping.get(table_type, 'js/default.js')
    # 渲染模板并传递JS路径
    return render_template('tables.html', js_path=js_path)

@main.route('/live2d')
def live2d():
    return render_template("live2d.html")


# 下载补丁
@main.route('/hotfix/<file_name>')
def hotfix(file_name):
    return send_file(
        "assets/static/data/hotfix/"+file_name,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        as_attachment=False  # True 会触发下载，False 直接显示
    )


@main.route('/upload_hotfix', methods=['POST'])
def upload_hotfix():
    # 检查是否有文件部分
    if 'file' not in request.files:
        return jsonify({
            "status": "error",
            "error": "No file part"
        }), 400

    file = request.files['file']

    # 检查是否选择了文件
    if file.filename == '':
        return jsonify({
            "status": "error",
            "error": "No selected file"
        }), 400

    # 确保上传目录存在
    upload_folder = "assets/static/data/hotfix/"
    os.makedirs(upload_folder, exist_ok=True)

    # 处理文件名
    filename = secure_filename(file.filename)
    save_path = os.path.join(upload_folder, filename)

    try:
        file.save(save_path)
        return jsonify({
            "status": "success",
            "path": f"/hotfix/{filename}",
            "size": os.path.getsize(save_path)
        }), 200
    except Exception as e:
        print(str(e))
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500



