# This is a simple port scanner that checks for open ports on a target host.

import socket

def scan_port_range(host_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            result = s.connect_ex((host_ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

TARGET_HOST = "127.0.0.1"

starting_port = int(input("Please specify starting port: "))
ending_port = int(input("Please specify ending port: "))
print(f"Starting port scan on IP: {TARGET_HOST} from ports {starting_port} - {ending_port}:")

open_ports = scan_port_range(TARGET_HOST, starting_port, ending_port)

print(f"Open ports: {open_ports}")




    