def application(env, start_resp):
    start_resp('200 OK', [('Content-Type', 'text/html')])
    return [ 'Hello there! <img src="/NGINX.png">'.encode('utf-8') ]
