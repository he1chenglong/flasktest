#qpy:webapp:<app >
#qpy:fullscreen
#qpy://l27.0.0.1:5000/
from flask import Flask,request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<id>',methods=['GET'])
def hello_user(id):
    return  "hello user: "+id

#http://127.0.0.1:5000/query_user?id=121231
@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query user: '+ str(id)

if __name__ == '__main__':
    app.run()
