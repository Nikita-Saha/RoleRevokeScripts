import os
import http.client
import json
import sys
from email.message import EmailMessage
import ssl
import smtplib
import re
import requests

CLIENT_ID = os.environ["client_id"]
CLIENT_SECRET = os.environ["client_secret"]
URL = os.environ["url"]
conn = http.client.HTTPSConnection(f"{URL}")


#TO GET ACCESS TOKEN :-
#-------------------------
payload = ''
headers = {}
conn.request("POST", f"/oauth/token?grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}", payload, headers)
res = conn.getresponse()
data = res.read()
json_dict = json.loads(data)
key = json_dict['access_token']
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer '+key
}


#TO GET THE INVOCATION STATUS
url = "https://kpmgukdev.api.identitynow.com/beta/trigger-invocations/status"

payload={}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


