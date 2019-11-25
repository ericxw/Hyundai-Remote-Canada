import requests
import json

def login(headers, username, password):
  payload = "{\"loginId\":\"" + username + "\", \"password\":\"" + password + "\"}"
  r = requests.post("https://mybluelink.ca/tods/api/lgn", headers=headers, data=payload)
  json_response = r.json()

  return json_response['result']['accessToken']

def logout(headers, accesstoken):
  authheaders = dict(headers)
  authheaders['accessToken'] = accesstoken
  payload = "{}"
  r = requests.post("https://mybluelink.ca/tods/api/lgout", headers=authheaders, data=payload)
  json_response = r.json()
  
  return json_response['responseHeader']['responseCode']

def get_pauth(headers, accesstoken, pin):
  payload = "{\"pin\":\"" + pin + "\"}"
  authheaders = dict(headers)
  authheaders['accessToken'] = accesstoken
  r = requests.post("https://mybluelink.ca/tods/api/vrfypin", headers=authheaders, data=payload)
  json_response = r.json()

  return json_response['result']['pAuth']

#def get_status():

def req_unlock(headers, accesstoken, pauth, pin, carid):
  payload = "{\"pin\":\"" + pin + "\"}"
  authheaders = dict(headers)
  authheaders['accessToken'] = accesstoken
  authheaders['pAuth'] = pauth
  authheaders['vehicleId'] = carid
  r = requests.post("https://mybluelink.ca/tods/api/drulck", headers=authheaders, data=payload)
  json_response = r.json()

  return json_response['responseHeader']['responseCode']

def req_lock(headers, accesstoken, pauth, pin, carid):
  payload = "{\"pin\":\"" + pin + "\"}"
  authheaders = dict(headers)
  authheaders['accessToken'] = accesstoken
  authheaders['pAuth'] = pauth
  authheaders['vehicleId'] = carid
#  print("req_lock: " + json.dumps(authheaders, indent = 2))
  r = requests.post("https://mybluelink.ca/tods/api/drlck", headers=authheaders, data=payload)
  json_response = r.json()

  return json_response['responseHeader']['responseCode']

#def req_engine_start():
