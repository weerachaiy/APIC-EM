import requests
import json

requests.packages.urllib3.disable_warnings()
api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/ticket"
headers = {"Content-Type": "application/json"}
body_json = {"username": "devnetuser", "password": "NTgmY5UY"}

resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
#print(resp)
resp_json = resp.json()
#print(resp_json)
ticket = resp_json["response"]["serviceTicket"]
print("Service ticket is ", ticket)

