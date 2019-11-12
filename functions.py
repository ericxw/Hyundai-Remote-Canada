import requests
import json
import configparser
config = configparser.ConfigParser()
config.read('remote.conf')
username = config['DEFAULT']['username']
password = config['DEFAULT']['password']

def login():
  headers = {'Pragma': 'no-cache', 'Origin': 'https://mybluelink.ca', 'language': '0', 'offset': '-5', 'Accept-Language': 'en-US,en;q=0.9', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36', 'content-type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain, */*', 'Cache-Control': 'no-cache', 'Referer': 'https://mybluelink.ca/login', 'Connection': 'keep-alive', 'from': 'CWP'}

  payload = "{\"loginId\":\"" + username + "\", \"password\":\"" + password + "\"}"

  r = requests.post("https://mybluelink.ca/tods/api/lgn", headers=headers, data=payload, verify=False)

  json_response = r.json()

  return json_response['result']['accessToken']

def get_status():

def req_unlock():

def req_lock():

def req_engine_start():
