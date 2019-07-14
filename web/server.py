# server.py
# 从wsgiref模块导入:
# import sys
# sys.path.append('.')
from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

if __name__=="__main__":
    try:
        # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
        httpd = make_server('', 8000, application)
        print('Serving HTTP on port 8000...')
        # 开始监听HTTP请求:
        httpd.serve_forever()
    except:
        exit()
