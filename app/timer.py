import json
import datetime
def wsgi_timer(env, start_resp):
    now = str(datetime.datetime.now().strftime("<%d-%m-%Y %H:%M>"))
    print(env)
    url = env['REMOTE_ADDR'] + env['PATH_INFO']
    start_resp('200 OK', [('Content-Type', 'application/json')])
    arr = {"time": now, "url": url}
    resp = json.dumps(arr)
    resp = resp.encode('utf-8')
    return[resp]
