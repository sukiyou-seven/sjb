import hashlib
import json

import eel
import requests

base_url = "http://127.0.0.1:12369/"


@eel.expose
def py_login(u, p):
    ph = hashlib.md5()
    ph.update(p.encode("utf-8"))
    p = ph.hexdigest()

    response = requests.post(url=base_url + 'login', auth=(u, p))
    response = json.loads(response.text)
    print(response)
    print(response['code'])
    if response['code'] != '0':
        print("2")
        eel.py_login_response('500')
    else:
        print("1")
        eel.py_login_response('200')


eel.init('view')

eel.start('index.html', size=(800, 600), port=52100, debug=True)

