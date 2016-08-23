# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
import  threading
import random
import time

app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    print 'call _add_numbers ...'
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/')
def index():
    return render_template('index.html')

def randomthread():
    # time.sleep(5)
    print 'call randomthread'
    randomnum=random.randint(1,100)
    # return  jsonify(randomnum)

if __name__ == '__main__':
    t=threading.Thread(target=randomthread)
    t.start()
    t.join()
    app.run(threaded=True)