# Project Overview

## Purpose

NetScan demonstrates how a browser interface can interact with a Python network-security component.

## Workflow

1. User enters an IPv4 address.
2. JavaScript sends the address to the Flask API.
3. Flask validates the address.
4. The scanner attempts TCP connections to selected ports.
5. The API returns structured JSON.
6. The frontend displays port status and service names.

## Technologies

- Python
- Flask
- Python socket library
- ipaddress
- HTML5
- CSS3
- JavaScript

## Security concept

TCP port scanning is a basic network reconnaissance technique. Open ports can indicate services that are reachable from the scanning host. In real security work, results are interpreted alongside service versions, configuration, authentication, exposure, and other controls.

## Safety considerations

Use this application only against systems for which you have authorization. A production deployment should add authentication, rate limiting, logging, and stricter target controls.

## Current scope

The first version intentionally keeps the scanner simple: IPv4 only and a predefined set of common TCP ports.

## Possible next version

- Concurrent port checks
- Custom port selection
- Better service detection
- Result export
- Scan history
- Authentication and audit logs
