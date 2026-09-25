# NetScan

A lightweight web-based TCP port scanner built with Python, Flask, HTML, CSS, and JavaScript.

## What it does

Enter an IPv4 address and NetScan checks a focused list of common TCP ports, then displays which ports are open and the commonly associated service.

## Features

- IPv4 validation
- TCP connect scanning
- Common port/service identification
- Clean cybersecurity dashboard
- JSON API
- Responsive frontend
- Educational authorization notice

## Run locally

```bash
git clone https://github.com/btwsalts/net-scan.git
cd net-scan
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open http://127.0.0.1:5000.

## Ports checked

21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5432, 5900, 8080.

## Architecture

Browser → Flask API → Python TCP scanner → Target → JSON results → Browser

## Security note

Only scan systems you own or have explicit permission to test. This project is intended for learning, home labs, and authorized security testing.

## Limitations

- IPv4 targets only.
- The initial release checks a predefined list of common ports.
- A closed result means the TCP connection attempt did not succeed; it does not prove that a service is absent.
- Results can be affected by firewalls, filtering, routing, and network conditions.

## Future improvements

- Custom port ranges
- Concurrent scanning
- Scan history
- Exportable reports
- More service detection
- Authentication for hosted deployments
- Rate limiting and audit logging
