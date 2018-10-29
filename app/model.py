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