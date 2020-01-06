import os
from flask import Flask,request
import bluelinkfunctions
from bluelinkfunctions import login,logout,get_pauth,req_unlock,req_lock,req_engine_start,req_engine_stop
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
carid = os.environ['CARID']
pin = os.environ['PIN']
key = os.environ['KEY']

headers = {'Pragma': 'no-cache', 'Origin': 'https://mybluelink.ca', 'language': '0', 'offset': '-5', 'Accept-Language': 'en-US,en;q=0.9', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36', 'content-type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain, */*', 'Cache-Control': 'no-cache', 'Referer': 'https://mybluelink.ca/login', 'Connection': 'keep-alive', 'from': 'CWP'}

app = Flask(__name__)

@app.route("/")
def home():
    return "Yo!"

@app.route("/lock")
def lock():
    if request.form.get('key') == key:
      accesstoken = login(headers, username, password)
      pauth = get_pauth(headers, accesstoken, pin)
      response = str(req_lock(headers, accesstoken, pauth, pin, carid))
      logout(headers, accesstoken)
      return response
    else:
      return "Key failed"

@app.route("/unlock")
def unlock():
    if request.form.get('key') == key:
      accesstoken = login(headers, username, password)
      pauth = get_pauth(headers, accesstoken, pin)
      response = str(req_unlock(headers, accesstoken, pauth, pin, carid))
      logout(headers, accesstoken)
      return response
    else:
      return "Key failed"

@app.route("/start")
def start():
    if request.form.get('key') == key:
      accesstoken = login(headers, username, password)
      pauth = get_pauth(headers, accesstoken, pin)
      response = str(req_engine_start(headers, accesstoken, pauth, pin, carid))
      logout(headers, accesstoken)
      return response
    else:
      return "Key failed"

@app.route("/stop")
def stop():
    if request.form.get('key') == key:
      accesstoken = login(headers, username, password)
      pauth = get_pauth(headers, accesstoken, pin)
      response = str(req_engine_stop(headers, accesstoken, pauth, pin, carid))
      logout(headers, accesstoken)
      return response
    else:
      return "Key failed"
    
if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
