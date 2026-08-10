import socket
import subprocess
import platform
import time


def check_connectivity(host="8.8.8.8"):
    """Check whether a host is reachable."""
    print(f"\n[+] Testing connectivity to {host}...")

    flag = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", flag, "1", host],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            print("[✓] Host is reachable.")
        else:
            print("[X] Host could not be reached.")

    except Exception as error:
        print(f"[X] Connectivity test failed: {error}")


def dns_lookup(domain):
    """Resolve a domain name to an IP address."""
    print(f"\n[+] Resolving {domain}...")

    try:
        ip_address = socket.gethostbyname(domain)
        print(f"[✓] {domain} -> {ip_address}")
        return ip_address

    except socket.gaierror:
        print("[X] DNS lookup failed.")
        return None


def check_port(host, port):
    """Check whether a TCP port is reachable."""
    print(f"\n[+] Checking {host}:{port}...")

    try:
        with socket.create_connection((host, port), timeout=3):
            print(f"[✓] Port {port} is reachable.")
            return True

    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f"[X] Port {port} is not reachable.")
        return False


def measure_latency(host="8.8.8.8"):
    """Measure approximate TCP connection latency."""
    print(f"\n[+] Measuring latency to {host}...")

    start = time.perf_counter()

    try:
        with socket.create_connection((host, 53), timeout=3):
            latency = (time.perf_counter() - start) * 1000
            print(f"[✓] Approximate latency: {latency:.2f} ms")
            return latency

    except OSError:
        print("[X] Unable to measure latency.")
        return None


def local_network_info():
    """Display basic local network information."""
    print("\n[+] Local Network Information")

    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        print(f"Hostname: {hostname}")
        print(f"Local IP: {ip_address}")

    except socket.error as error:
        print(f"[X] Unable to retrieve network information: {error}")


def main():
    print("=" * 48)
    print("                  NETSCOPE")
    print("          Network Diagnostic Toolkit")
    print("=" * 48)

    local_network_info()
    check_connectivity()

    domain = input("\nEnter a domain to diagnose (example.com): ").strip()

    if not domain:
        domain = "example.com"

    ip_address = dns_lookup(domain)

    if ip_address:
        check_port(domain, 80)
        check_port(domain, 443)
        measure_latency(domain)

    print("\n" + "=" * 48)
    print("Diagnostic complete.")
    print("=" * 48)


if __name__ == "__main__":
    main()
