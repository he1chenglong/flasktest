#-*-coding:utf-8-*-
#qpy:webapp:<app >
#qpy:fullscreen
#qpy://localhost:18080/index
from bottle import route, run, template, request

#登录
@route("/login",method="post")
def login():

    username = request.forms.get("username");
    password = request.forms.get("password");

    print(username,password)

    if username =='admin' and password =='admin':
        return username+'登录成功';
    else :
        return username+'登录失败';

#用户登录页面的
@route("/index")
def index():

    return template("index")

#@route('/hello/:name')
#def index(name='World'):
#    return '<b>Hello %s!</b>' % name

run(host='localhost', port=18080)