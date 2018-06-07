import requests
import json
from apic import *
from tabulate import *

requests.packages.urllib3.disable_warnings()

print("The hosts in the system are:")
print_host()
print("The network devices in the system are:")
print_device()

s_ip = input("Enter source IP address: ")
d_ip = input("Enter destination IP address: ")

api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/flow-analysis"
ticket = get_ticket()
print(ticket)
headers = {"Content-Type": "application/json",
           "X-Auth-Token": ticket}
body_json = {
  "destIP": d_ip,
  "sourceIP": s_ip
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
response_json = resp.json()
print("Response status: ", resp.status_code)
flow_id = response_json["response"]["flowAnalysisId"]
print("Flow ID: ", flow_id)

for i in range(16):
    check_url = api_url + '/' + flow_id
    resp = requests.get(check_url, headers=headers, verify=False)
    response_json = resp.json()
    #print(response_json)
    status = response_json['response']['request']['status']
    print(status)
    if status == 'COMPLETED':
        break;

network_elements = response_json['response']['networkElementsInfo']

all_device = []
num = 1;
for item in network_elements:
    if 'name' not in item:
        name = 'UNKNOWN'
    else:
        name = item['name']
    ip = item['ip']
    device = [num, name, ip]
    all_device.append(device)
    num = num + 1

header_table = ['number', 'name', 'IP address']
print(tabulate(all_device, header_table))
#print(all_device)

    





