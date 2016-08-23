#-*-coding:utf-8-*-
#qpy:webapp:<app >
#qpy:fullscreen
#qpy://l27.0.0.1:5050/
from flask import Flask, flash, render_template, request,abort

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def hello_world():
    flash("hello jikexueyuan")
    return render_template("index.html")

@app.route('/getuser', methods=['POST'])
def getuser():
    # flash(" glz ")
# return render_template("index.html")
    print 'getuser...'
    # return render_template('user.html')
    return  "hello user: "



@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash("please input username")
        return render_template("index.html")
    if not password:
        flash("please input password")
        return render_template("index.html")

    if username == 'jikexueyuan' and password == '123456':
        flash("login success")
        return render_template("index.html")
    else:
        flash("username or password is wrong")
        return render_template("index.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id) == 1:
        return render_template("user.html")
    else:
        abort(404)



if __name__ == '__main__':
    app.run(port=5050)
