import ipaddress
import socket


def validate_ip(ip: str) -> bool:
    try:
        address = ipaddress.ip_address(ip)
        return address.version == 4
    except ValueError:
        return False


def scan_port(ip: str, port: int, timeout: float = 0.6) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((ip, port)) == 0


def service_name(port: int) -> str:
    try:
        return socket.getservbyport(port, "tcp").upper()
    except OSError:
        return "UNKNOWN"


def scan_ports(ip: str, ports: list[int]) -> list[dict]:
    results = []
    for port in ports:
        is_open = scan_port(ip, port)
        results.append({
            "port": port,
            "status": "open" if is_open else "closed",
            "service": service_name(port) if is_open else "-"
        })
    return results
