#-*-coding:utf-8-*-
#qpy:webapp:<app >
#qpy:fullscreen
#qpy://localhost:18080/index
from bottle import route, run, template, request
import bottle

#用户登录页面的
@route("/index")
def index():
    bottle.TEMPLATE_PATH.insert(0,'/storage/emulated/legacy/com.hipipal.qpyplus/projects/bottletest')
    return template('index')

run(host='localhost', port=18080)