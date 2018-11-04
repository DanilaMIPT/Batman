import app.model as model
from flask import render_template,  request, abort, jsonify
from app import app

@app.route('/messages/')
def messages():
    chat_id = int(request.args.get('chat_id'))
    messages = model.list_messages_by_chat(chat_id, 5)
    return jsonify(messages)

@app.route('/')
def index(): return 'uou'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        rv = jsonify( request.form )
        return rv
        print(request.form)
        abort(404)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "GET":
        return render_template('loginForm.html')
    elif request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('loginError.html', error=error)

def valid_login(name, password):
    if name in a:
        return a[name] == password
    else:
        return False

def log_the_user_in(name):
    return render_template('loginOK.html', name=name)

a = { 'danila': '1234',
      'alena': '4321'
}

@app.route('/search_users/', methods=['GET'])
def search_user():
    word = request.args.get('word')
    users = model.search_user(word, 5)
    return jsonify(users)

@app.route('/new_chat/')
def create_chat():
    a = model.new_chat(3, 4)
    return jsonify(a)