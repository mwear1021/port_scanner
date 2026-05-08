# Port Scanner

A simple port scanner API built with FastAPI and deployed via Docker. It scans a target host for open ports over a specified range and returns the results as JSON.

## Legal Notice

Only scan hosts you own or have explicit permission to scan. A safe public test target is `scanme.nmap.org`, which is provided by the Nmap project for this purpose.

## How It Works

The app exposes a single endpoint, `/scan`, which accepts a hostname and port range, attempts a TCP connection on each port, and returns a list of open ports.

Visiting the root `/` will automatically redirect you to `/scan`.

## Usage

### Swagger UI (Recommended)

The easiest way to use the API is through the built-in Swagger UI:

1. Navigate to `https://port-scanner-t9zg.onrender.com` in your browser
2. Click on the `GET /scan` endpoint to expand it
3. Click **"Try it out"**
4. Fill in the following parameters:
   - `host` — the target hostname or IP address (e.g. `scanme.nmap.org` or `127.0.0.1`)
   - `start_port` — the first port in the range to scan (e.g. `1`)
   - `end_port` — the last port in the range to scan (e.g. `100`)
5. Click **"Execute"**
6. The response may take a bit to scan each port, but will show a list of open ports, for example:
```json
{
  "open ports": [22, 80]
}
```

## Running Locally with Docker

```bash
docker build -t port-scanner .
docker run -p 8000:8000 port-scanner
```

Then visit `http://localhost:8000/docs`.

## Requirements

- Python 3.12
- `fastapi[standard]`
