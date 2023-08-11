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

#TO GET EVENT TRIGGER DETAILS
url = f'/identity-attributes-changed'
conn.request("GET",url, payload, headers)
res = conn.getresponse()
data = res.read()
json_dict = json.loads(data)
print(json_dict)


# REVOKE OR GRANT ACCESS

url = "https://sailpoint.api.identitynow.com/beta/access-requests"

payload = json.dumps({
  "requestedFor": [
    "<string>",
    "<string>"
  ],
  "requestedItems": [
    {
      "id": "<string>",
      "type": "<string>",
      "comment": "<string>",
      "clientMetadata": {
        "aliquab10": "<string>",
        "Ut58": "<string>",
        "quis14b": "<string>",
        "adipisicing5": "<string>"
      },
      "removeDate": "<dateTime>"
    },
    {
      "id": "<string>",
      "type": "<string>",
      "comment": "<string>",
      "clientMetadata": {
        "velit_c": "<string>"
      },
      "removeDate": "<dateTime>"
    }
  ],
  "requestType": "<string>",
  "clientMetadata": {
    "voluptatea": "<string>",
    "in_3": "<string>",
    "in_e1e": "<string>"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


#TO GET THE INVOCATION STATUS
url = "https://kpmgukdev.api.identitynow.com/beta/trigger-invocations/status"

payload={}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


