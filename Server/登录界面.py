#coding=utf-8
#File home.html
#### 0_***为临时前端界面代码
from bottle import *

app = Bottle(__name__)
##########主页面#########
@app.route('/', methods=['GET', 'POST'])
def home():
    return template('/Users/mac/XOJ/Server/0_home.html')

##########登录界面#########

@app.route('/signin', methods=['GET'])
def signin_forms():
    return template('/Users/mac/XOJ/Server/0_login.html')
#
##########验证登录#########
#@app.route('/signin', methods='POST')
def signin():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=='admin' and password=='password':
        return template('/Users/mac/XOJ/Server/0_login_success.html', username=username)
    return template('/Users/mac/XOJ/Server/0_login.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8888')
