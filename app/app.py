from flask import Flask
import bluelinkfunctions
from bluelinkfunctions import login,logout,get_pauth,req_unlock,req_lock
import configparser
config = configparser.ConfigParser()
config.read('remote.conf')
username = config['DEFAULT']['username']
password = config['DEFAULT']['password']
carid = config['DEFAULT']['carid']
pin = config['DEFAULT']['pin']

headers = {'Pragma': 'no-cache', 'Origin': 'https://mybluelink.ca', 'language': '0', 'offset': '-5', 'Accept-Language': 'en-US,en;q=0.9', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36', 'content-type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain, */*', 'Cache-Control': 'no-cache', 'Referer': 'https://mybluelink.ca/login', 'Connection': 'keep-alive', 'from': 'CWP'}

app = Flask(__name__)

@app.route("/")
def home():
    return "Yo!"

@app.route("/lock")
def lock():
    accesstoken = login(headers, username, password)
    pauth = get_pauth(headers, accesstoken, pin)
    print ( req_lock(headers, accesstoken, pauth, pin, carid) )
    print ( logout(headers, accesstoken) )
    return "Lock"

@app.route("/unlock")
def unlock():
    accesstoken = login(headers, username, password)
    pauth = get_pauth(headers, accesstoken, pin)
    print ( req_unlock(headers, accesstoken, pauth, pin, carid) )
    print ( logout(headers, accesstoken) )
    return "Unlock"

@app.route("/start")
def start():
    return "Start"

@app.route("/stop")
def stop():
    return "Stop"
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
