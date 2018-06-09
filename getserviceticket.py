import api
import requests
import json
import tabulate

def main():
    requests.packages.urllib3.disable_warnings()

    api.print_host()

    api.print_device()

    #s_IP = input("Source IP: ")
    s_IP = "10.1.15.117"
    #d_IP = input("Destination IP: ")
    d_IP = "10.2.1.22"

    api.print_flowurl(s_IP,d_IP)

if __name__ == '__main__':
    main()
