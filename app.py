from flask import Flask, jsonify, request, send_from_directory
from scanner import scan_ports, validate_ip

app = Flask(__name__, static_folder="frontend", static_url_path="")

DEFAULT_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5432, 5900, 8080]


@app.get("/")
def index():
    return send_from_directory("frontend", "index.html")


@app.post("/api/scan")
def scan():
    data = request.get_json(silent=True) or {}
    ip = str(data.get("ip", "")).strip()

    if not validate_ip(ip):
        return jsonify({"error": "Enter a valid IPv4 address."}), 400

    results = scan_ports(ip, DEFAULT_PORTS)
    open_ports = [item for item in results if item["status"] == "open"]

    return jsonify({
        "target": ip,
        "scanned": len(results),
        "open_count": len(open_ports),
        "results": results,
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
