# This is a simple port scanner that checks for open ports on a target host.

import socket
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


def scan_port_range(start_port, end_port, host_ip):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            result = s.connect_ex((host_ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports


@app.get("/")
async def redir():
    return RedirectResponse('/docs')


@app.get("/scan")
def scan(host: str, start_port: int, end_port: int):
    open_ports = scan_port_range(start_port, end_port, host)
    return {"open ports": open_ports}
