"""This is a Web App built with Bottlepy which displays the current time in Moscow."""

import datetime
from bottle import route, run, template
import pytz

@route('/')
def msctime():
    """Returns the an HTML string with current time in Moscow."""

    now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).time()
    return template('''
    <div style="
      display:flex;
      justify-content:center;
      font-family:Arial;
      font-size:40px;
      padding-top: 10px;
    ">
      Time in Moscow: &nbsp <b>{{time}}</b>
    </div>
    ''', time=now)

if __name__ == '__main__':
    run(server='paste', host='0.0.0.0', port=8080, debug=False)
