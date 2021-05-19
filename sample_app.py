import os
import requests
from bottle import route, template, redirect, static_file, error, run


@route('/')
def handle_root_url():
    msg = "My butt farted ^_^"
    requests.post('https://discord.com/api/webhooks/839988220203630623/f0e6qbNlT5cPmsP3M3638XEb_dEaeFoownCvOx3pdnebTR3FNWfAYGp-p6LV1Qff3xeT', data={"content": msg})

@error(404)
def error404(error):
    return template('EXE', error_msg='Four :heart_eyes: 04 Eror')


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
