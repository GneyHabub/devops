"""This is a Web App built with Bottlepy which displays the current time in Moscow."""

import datetime
from bottle import route, run, template
import pytz
import os

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

@route('/visits')
def visits():
  new_count = 0
  """Returns the number of visits to the website"""
  if not os.path.exists("./data"):
    os.makedirs('data')
  if not os.path.exists("./data/visitCount.txt"):
    f = open('./data/visitCount.txt', 'w+')
    f.write("0")
    f.close()
  else:
    f = open('./data/visitCount.txt', 'r') 
    data = int(f.read())
    f.close()
    new_count = data + 1
    f = open('./data/visitCount.txt', 'w') 
    f.write(str(new_count))
    f.close()

  color = ("00000" + str(hex(new_count))[2:])[-6:]
  return template('''
  <div style="
    display:flex;
    justify-content:center;
    font-family:Arial;
    font-size:40px;
    padding-top: 10px;
  ">
    The website was visited &nbsp <b style="color: {{color}}">{{times}}</b> &nbsp times
  </div>
  ''', times=new_count, color="#" + color)

if __name__ == '__main__':
    run(server='paste', host='0.0.0.0', port=8080, debug=False)
