from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def do_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{add(a, b)}"

@app.route("/sub")
def do_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{sub(a, b)}"

@app.route("/mult")
def do_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{mult(a, b)}"

@app.route("/div")
def do_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{div(a, b)}"

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<opr>")
def do_math(opr):
    a = int(request.args["a"])
    b = int(request.args["b"])
    func = operations.get(opr)
    return f"{func(a, b)}"

