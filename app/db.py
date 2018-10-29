import flask
import psycopg2, psycopg2.extras
import app.instance.config as config

def get_connection():
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(
                database=config.DB_NAME, host=config.DB_HOST,
                user=config.DB_USER, password=config.DB_PASS)
    return flask.g.dbconn

def get_cursor():
    return get_connection().cursor(
            cursor_factory=psycopg2.extras.DictCursor)

def query_one(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        result = {}
        return dict(cur.fetchone())

def query_all(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        result = cur.fetchall()
        answer = {}
        i=1
        for raw in result:
            print(raw)
            answer[i] = dict(raw)
            i += 1
        return answer


def _rollback_db(sender, exception, **extra):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconnconn.rollback()
        conn.close()
        delattr(flask.g, 'dbconn')

#def _commit_db(sender, ...):
#    if hasattr(flask.g, 'dbconn'):
#        conn = flask.g.dbconn
#        conn.commit()
#        conn.close()
#        delattr(flask.g, 'dbconn')
