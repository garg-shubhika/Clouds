import flask
import math
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/numericalintegration/<lower>/<upper>')
def fun(lower,upper):
    str1=' '
    N=[10,100, 100, 1000, 10000, 100000, 1000000]
    A=0.0
    lower=float(lower)
    upper=float(upper)
    I=[]
    for j in N:
        A=0.0
        for i in range(1,j):
            A=A+(-math.cos(i*upper/j)+math.cos((i-1)*upper/j + lower))
        I.append(A)
    for x in I:
        str1=str(x)+' '+str1
    return str1
if __name__=='main_':
    app.run(debug=True)
