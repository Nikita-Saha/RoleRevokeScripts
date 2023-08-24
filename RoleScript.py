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

payload = json.dumps({
  "requestedFor": [
    "2c91808884157ab201841d761d977526"
  ],
  "requestedItems": [
    {
      "type": "ACCESS_PROFILE",
      "id": "50cce5d029bc47459349203cbcc0560f",
      "comment": "Requesting access profile for Coupa user"
    }
    
  ],
   "requestType": "GRANT_ACCESS"
  
})

conn.request("POST", "/beta/access-requests",payload, headers)
res = conn.getresponse()
data = res.read()
print("printing response")
print(data)
