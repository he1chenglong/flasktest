# -*- coding: utf-8 -*-
#qpy:webapp:<app >
#qpy:fullscreen
#qpy://l27.0.0.1:5050/
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request,flash,json
import  threading
import  thread
import random
import time

app = Flask(__name__)
app.secret_key = '123'

@app.route('/_add_numbers')
def add_numbers():
    print 'call _add_numbers ...'
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    flash("hello jikexueyuan")
    # thread.start_new_thread(randomthread,(1,1))
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_data():
    print 'call get_data'
    data = json.loads(request.form.get('data'))
    ss = data['value']
    print str(ss)
    return str(ss)

@app.route("/postjson", methods=['POST','GET'])
def getpostjson_data():
    print 'call postjson'
    data = json.loads(request.form.get('data'))
    ss = data['value']
    print str(ss)
    return str(ss)

@app.route("/polling",methods=['POST','GET'])
def polldata():
    print 'call polldata...'
    data = request.form.get('data')
    randomnum=random.randint(1,100)
    return  jsonify(result=randomnum)

def randomthread(no, interval):
    # time.sleep(5)
    print 'call randomthread'
    time.sleep(interval)
    randomnum=random.randint(1,100)
    # return  jsonify(randomnum)

if __name__ == '__main__':
    # t=threading.Thread(target=randomthread)
    # t.start()
    # # t.join()

    # app.run(threaded=True)
    app.run(port=5050)