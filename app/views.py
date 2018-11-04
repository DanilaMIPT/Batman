from flask import request, abort, jsonify
import json
from app import app, jsonrpc

@jsonrpc.method('hello')
@app.route('/<string:name>/')
@app.route('/')
def index(name="world"):
    return "Hello, {}!".format( name )

@app.route('/favicon.ico')
def icon():
    return

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        return """<html><head></head><body>
        <form method="POST" action="/form/">
            <input name="first_name" >
            <input name="last_name" >
            <input type="submit" >
        </form>
        </body></html>"""
    else:
        rv = jsonify( request.form )
        return rv
        print(request.form)
        abort(404)

@jsonrpc.method('print_name')
def foo():
    return {"name": "Ivan"}