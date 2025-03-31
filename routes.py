from flask import Blueprint, render_template, jsonify, send_file

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
    print(e)
    return make_response(code=500, data=None, message="服务器内部错误")


# 首页
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")


# 简历
@main.route('/resume')
def resume():
    return render_template('resume.html')


# 列表
@main.route('/table')
def table():
    return render_template("table.html")


@main.route('/document')
def document():
    return render_template("document.html")


@main.route('/document.docx')
def document_docx():
    return send_file(
        "assets/document.docx",
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        as_attachment=False  # True 会触发下载，False 直接显示
    )


# 分发
@main.route('/distribute')
def distribute():
    return render_template("distribute.html")


@main.route('/distribute.css')
def distribute_css():
    return render_template("distribute.css")


@main.route('/distribute.js')
def distribute_js():
    return render_template("distribute.js")


@main.route('/test', methods=['GET'])
@response_json_wrapper
def test():
    raise ValueError("测试")
    return "test"


@main.route('/new')
def new():
    return render_template("new.html")
