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


# REVOKE OR GRANT ACCESS

url = "https://sailpoint.api.identitynow.com/beta/access-requests"

payload = json.dumps({
  "requestedFor": [
    "2c91808883803e4b01838a209b5b291b"
  ],
  "requestType": "GRANT_ACCESS",
  "requestedItems": [
    {
      "type": "ENTITLEMENT",
      "id": "2c9180835d2e5168015d32f890ca1581",
      "comment": "Requesting access profile for John Doe",
      "clientMetadata": {
        "requestedAppName": "test-app",
        "requestedAppId": "2c91808f7892918f0178b78da4a305a1"
      },
      "removeDate": "2020-07-11T21:23:15.000Z"
    }
  ],
  "clientMetadata": {
    "requestedAppId": "2c91808f7892918f0178b78da4a305a1",
    "requestedAppName": "test-app"
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


