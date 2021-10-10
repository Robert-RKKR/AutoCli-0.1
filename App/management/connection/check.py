# Python Import:
import os

def check_ping(ip_address):
    ping_result = os.system(f"ping -c 5 {ip_address}")
    print(ping_result)