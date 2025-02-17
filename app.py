# 不使用域名的服务器部署方式
import os
import sys

from flask import Flask, send_from_directory, render_template


def resource_path(relative_path):
    """ 获取资源绝对路径 """
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return str(os.path.join(base_path, relative_path))


app = Flask(__name__,
            template_folder=resource_path('templates'),
            static_folder=resource_path('static'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pdfs/<path:filename>')
def pdf_show(filename):
    actual_filename = dispose_pdf_name(filename)
    if actual_filename:  # 如果找到对应的文件名
        return send_from_directory('static/pdfs', actual_filename)
    else:
        return "File not found", 404


def dispose_pdf_name(filename):
    # 将请求的 filename 转换为对应的实际文件名
    mapping = {
        '近代史': '中国近现代史纲要-重点知识点整理18版.pdf',
        '简历': '张先杰简历(Android开发)4.5.pdf'
    }
    return mapping.get(filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)



