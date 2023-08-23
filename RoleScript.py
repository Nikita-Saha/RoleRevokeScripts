import os
import http.client
import json
import sys
from email.message import EmailMessage
import ssl
import smtplib
import re
from datetime import date
from datetime import datetime

CLIENT_ID = os.environ["client_id"]
CLIENT_SECRET = os.environ["client_secret"]
URL = os.environ["url"]
conn = http.client.HTTPSConnection("kpmgukdev.api.identitynow.com")



#TO GET ACCESS TOKEN :-
#-------------------------
#url = "/oauth/token?grant_type=client_credentials&client_id=27d6fde9-91ca-4ec6-94d4-49d9b7faf107&client_secret=b8d4d865786ed856c749b6d99218db5e6c851b18f8f555b77b1fc3789b69ec6d"
payload = ''
headers = {}
conn.request("POST", f"/oauth/token?grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}", payload, headers)
#conn.request("POST", url, payload, headers)
res = conn.getresponse()
data = res.read()
json_dict = json.loads(data)
print("printing access token")
print(json_dict)
key = json_dict['access_token']
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer '+key
}


# REVOKE OR GRANT ACCESS

url1 = "/beta/access-requests"

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

conn.request("POST", url1, headers, payload)
res = conn.getresponse()
data = res.read()
print("printing response")
print(data)
