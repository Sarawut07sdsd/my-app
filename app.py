import json
import collections
import numpy as np
import datetime
from datetime import date
from flask import Flask

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
def index3(birthdate):
     return "xxxx"


if __name__ == "__main__":
    app.run()
