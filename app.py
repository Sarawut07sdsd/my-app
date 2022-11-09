import json
import collections
import numpy as np
from datetime import datetime
from datetime import date
from flask import Flask, jsonify, request,render_template
import os
import logging
app = Flask(__name__)


@app.route('/Ex1')
def index():
    Example1 = "abcde"
    Example2 = "aabbcde"
    Example3 = "aabBcde"
    Example4 = "indivisibility"
    Example5 = "lndivisibilities"
    Example6 = "aA11"
    Example7 = "ABBA"
    showArrays = [
        Example1, "return", collections.Counter(Example1),
        Example2, "return", collections.Counter(Example2),
        Example3, "return", collections.Counter(Example3),
        Example4, "return", collections.Counter(Example4),
        Example5, "return", collections.Counter(Example5),
        Example6, "return", collections.Counter(Example6),
        Example7, "return", collections.Counter(Example7),
    ]
    Show = json.dumps(showArrays)
    return Show


@app.route('/Ex2')
def index2():
    a = [1, 2]
    b = [1]
    Data = []
    ShowData = []
    for Sarawut in a:
        if Sarawut not in b:
            Data.append(Sarawut)
    Array_diff1 = [
        a, b, "return", Data
    ]
    ShowData.append(Array_diff1)

    a = [1, 2, 2, 2, 3]
    b = [2]
    Data2 = []
    for Sarawut in a:
        if Sarawut not in b:
            Data2.append(Sarawut)
    Array_diff2 = [
        a, b, "return", Data2
    ]
    ShowData.append(Array_diff2)
    return ShowData


@app.route('/Ex3')
def index3():
    gendayIn1 = '2021-10-21'
    gendayIn2 = '2021-12-21'
    gendayIn3 = '2021-15-21'
    genday =  1
    genday2 = 2
    genday3 = 11





@app.route('/path/index',methods = ['GET'])
def _get_():
    if request.method == 'GET':
        return  {"message":"Hello Jpark"}
    else:
        return "Error"
    
    

@app.route('/Ex5')
def index5():
    input=[
        {'id':1,'price':50,'payment_date':'2022-02-26 06:00:00'},
        {'id':2,'price':20,'payment_date':'2022-02-26 07:00:00'},
        {'id':3,'price':30,'payment_date':'2022-03-15 08:42:03'},
        {'id':4,'price':100,'payment_date':'2022-04-20 09:45:00'},
        {'id':5,'price':200,'payment_date':'2022-04-22 15:00:00'}
        ]
    prog_string = json.dumps(input,indent=4)
    print(input)
    return prog_string




if __name__ == "__main__":
    app.run()
