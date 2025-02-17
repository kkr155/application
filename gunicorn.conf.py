# gunicorn.conf.py
import multiprocessing

# 绑定的ip与端口
bind = "0.0.0.0:5000"

# 工作进程数
workers = multiprocessing.cpu_count() * 2 + 1

# 工作模式
worker_class = 'sync'  # 'gevent' 用于异步

# 日志级别
loglevel = 'info'

# 访问日志和错误日志
accesslog = "./logs/access.log"
errorlog = "./logs/error.log"

# 后台运行 将guncorn放在后台运行，会消失并没有任何输出
daemon = False

# 进程文件
pidfile = "./logs/gunicorn.pid"

# 使用配置文件启动
# gunicorn -c gunicorn.conf.py app:app

# pyinstaller --onefile app.py
