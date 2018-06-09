import requests
import json
from tabulate import *

requests.packages.urllib3.disable_warnings()

def get_ticket():
    api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/ticket"
    headers = {"Content-Type": "application/json"}
    body_json = {"username": "devnetuser", "password": "NTgmY5UY"}

    resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
    #print(resp)
    resp_json = resp.json()
    ticket = resp_json["response"]["serviceTicket"]
    #print("Service ticket is ", ticket)
    return ticket

def print_host():
    api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {"Content-Type": "application/json",
               "X-Auth-Token": ticket}
    resp = requests.get(api_url, headers=headers, verify=False)
    #print(ticket)
    #print(resp.status_code)
    response_json = resp.json()
    #print(response_json)
    host_list = []
    i = 0
    for item in response_json["response"]:
        i = i+1
        host = [i, item["hostType"], item["hostIp"]]
        host_list.append(host)

    table_header = ["Number", "Type", "IP"]
    print(tabulate(host_list, table_header))

def print_device():
    api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {"Content-Type": "application/json",
               "X-Auth-Token": ticket}
    resp = requests.get(api_url, headers=headers, verify=False)
    #print(ticket)
    #print(resp.status_code)
    response_json = resp.json()
    #print(response_json)
    device_list = []
    i = 0
    for item in response_json["response"]:
        i = i+1
        device = [i, item["type"], item["managementIpAddress"]]
        device_list.append(device)

    table_header = ["Number", "Type", "Management IP Address"]
    print(tabulate(device_list, table_header))
