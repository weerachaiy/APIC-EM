import api

api.print_host()

api.print_device()

s_IP = input("Source IP: ")
d_IP = input("Destination IP: ")
flow_url = api.print_flowid(s_IP,d_IP)
print(flow_url)
#api.print_flow_detail(flow_url)
