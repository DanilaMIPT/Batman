import app.db as db

def list_messages_by_chat(chat_id, limit):
    return db.query_all("""
        SELECT user_id, nick, name, 
            message_id, content, added_at
        FROM messages
        JOIN users USING (user_id)
        WHERE chat_id = %(chat_id)s
        ORDER BY added_at DESC
        LIMIT %(limit)s
    """, chat_id = int(chat_id), limit=int(limit))

def search_user(word, limit):
    return db.query_all("""
    SELECT nick, name, avatar
    FROM users 
    WHERE nick=%(word)s OR name=%(word)s
    LIMIT %(limit)s
    """, word = word, limit = int(limit))

def new_chat_id(user_id, member_id):
    report = db.query_all("""
    INSERT INTO Chats(topic)
    VALUES (%(topic)s)
    RETURNING chat_id;
    """, topic = str(user_id) + 'vs' + str(member_id))
    chat_id = (report[0]['chat_id'])
    return chat_id;

def add_member(member_id, chat_id):
    result = db.query_one("""
    INSERT INTO Members
    VALUES(%(member_id)s, %(chat_id)s)
    RETURNING member_raw;
    """, member_id = int(member_id), chat_id = int(chat_id))
    return result

def check_chat(user_id, member_id):
    result = db.query_all("""
    SELECT count(DISTINCT foo.chat_id)
    FROM (SELECT chat_id
            FROM members
            WHERE user_id = %(member_id)s
            AND chat_id IN (SELECT chat_id 
                        FROM members  
                        WHERE user_id = %(user_id)s)) AS foo 
    LEFT JOIN chats ON foo.chat_id = chats.chat_id
    WHERE is_group_chat = 0;
    """, user_id = int(user_id), member_id = int(member_id))
    return result

def new_chat(user_id, member_id):
    check = check_chat(user_id, member_id)[0]['count']
    if check == 0:
        chat_id = new_chat_id(user_id, member_id)
        add_member(user_id, chat_id)
        add_member(member_id, chat_id)
        report = 'your new chat is ' + str(chat_id)
    else:
        report = 'you have already chat with this guy'
    return report

