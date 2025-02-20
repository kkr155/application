import os
import sys


def resource_path(relative_path):
    """ 获取资源绝对路径 """
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return str(os.path.join(base_path, relative_path))


def dispose_pdf_name(filename):
    # 将请求的 filename 转换为对应的实际文件名
    mapping = {
        '近代史': '中国近现代史纲要-重点知识点整理18版.pdf',
        '简历': '张先杰简历(Android开发)4.5.pdf'
    }
    return mapping.get(filename)