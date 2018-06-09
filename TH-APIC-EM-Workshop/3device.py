import requests
import json
from apic import *
import tabulate
requests.packages.urllib3.disable_warnings()

api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/network-device"
ticket = get_ticket()
headers = {"Content-Type": "application/json",
           "X-Auth-Token": ticket}
resp = requests.get(api_url, headers=headers, verify=False)
response_json = resp.json()

device_list = []
i = 0
for item in response_json["response"]:
    i = i+1
    device = [i, item["type"], item["managementIpAddress"]]
    device_list.append(device)

table_header = ["Number", "Type", "Management IP Address"]
print(tabulate.tabulate(device_list, table_header))
