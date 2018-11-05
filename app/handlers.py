import app.model as model
from flask import render_template,  request, abort, jsonify
from app import app

# show 50 last messages from this chat_id
@app.route('/messages/', methods=['GET'])
def messages():
    chat_id = int(request.args.get('chat_id'))
    messages = model.list_messages_in_chat(chat_id, 50)
    return jsonify(messages)


@app.route('/')
def index(): return 'uou'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

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

# find user
@app.route('/search_users/', methods=['GET'])
def search_user():
    word = request.args.get('word')
    users = model.search_user(word, 5)
    return jsonify(users)

# create new chat#СПРОСИТЬ, НУЖНО ЛИ ПЕРЕДЕЛАТЬ НА POST
@app.route('/new_chat/', methods=['GET'])
def create_chat():
    user_id = int(request.args.get('user_id'))
    member_id = int(request.args.get('member_id'))
    report = model.new_chat(user_id, member_id)
    return jsonify(report)

# show chats of this user in order of last message added_at
@app.route('/chats/', methods=['GET'])
def user_chats():
    user = request.args.get('user_id')
    a = model.user_chats(user)
    return jsonify(a)

# send a new message
@app.route('/new_message/', methods=['GET', 'POST'])
def new_message():
    if request.method == "GET":
        user_id = int(request.args.get('user_id'))
        chat_id = int(request.args.get('chat_id'))
        return render_template('new_message.html',
                               user_id = user_id, chat_id = chat_id)
    elif request.method == 'POST':
        content = request.form['content']
        user_id = int(request.args.get('user_id'))
        chat_id = int(request.args.get('chat_id'))
        result = model.add_message_to_db(user_id, chat_id, content)
        return jsonify(result, 'message added')
    print(request.new_message)
    abort(404)


