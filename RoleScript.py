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
print(data)

json_dict = json.loads(data)
key = json_dict['access_token']
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer '+key
}


# REVOKE OR GRANT ACCESS

url = "/beta/access-requests"

payload = json.dumps({
  "requestedFor": [
    "2c918088838059a201838a209b591f75"
  ],
  "requestType": "GRANT_ACCESS",
  "requestedItems": [
    {
      "type": "ENTITLEMENT",
      "id": "2c9180887e8e29e1017e8fe4d1ca3aa0",
      "comment": "Requesting access profile for Nikita Saha",
    }
  ],
})

conn.request("POST", url, headers, payload)
print("printing response")
print(response.text)



