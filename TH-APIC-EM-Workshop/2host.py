import requests
import json
from apic import *
import tabulate
requests.packages.urllib3.disable_warnings()

api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/host"
ticket = get_ticket()
headers = {"Content-Type": "application/json",
           "X-Auth-Token": ticket}
resp = requests.get(api_url, headers=headers, verify=False)
response_json = resp.json()
print(response_json)

host_list = []
i = 0
for item in response_json["response"]:
    i = i+1
    host = [i, item["hostType"], item["hostIp"]]
    host_list.append(host)

table_header = ["Number", "Type", "IP"]
print(host_list[0])
print(host_list[1])
print(host_list[2])
print(tabulate.tabulate(host_list, table_header))
