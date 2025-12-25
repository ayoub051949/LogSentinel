#!/usr/bin/env python3
"""
Network Recon Tool
Purpose: Educational / Blue Team & Pentesting Learning
WARNING: Use only on systems you own or have permission to test.
"""

import socket
import argparse
from datetime import datetime

# Timeout for sockets
socket.setdefaulttimeout(1)

def print_banner():
    print("=" * 50)
    print(" Simple Network Recon Tool ")
    print(" Author: Mandelo ")
    print(" Educational use only ")
    print("=" * 50)

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "No banner"
            s.close()
            return True, banner
        s.close()
        return False, None
    except Exception:
        return False, None

def main():
    parser = argparse.ArgumentParser(description="Simple Network Recon Tool")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--ports", help="Port range (ex: 1-1000)", default="1-1024")
    parser.add_argument("-o", "--output", help="Output file", default="scan_results.txt")

    args = parser.parse_args()

    start_port, end_port = map(int, args.ports.split("-"))

    print_banner()
    print(f"[+] Target: {args.target}")
    print(f"[+] Scanning ports: {start_port}-{end_port}")
    print(f"[+] Start Time: {datetime.now()}\n")

    with open(args.output, "w") as f:
        f.write(f"Scan report for {args.target}\n")
        f.write(f"Started at: {datetime.now()}\n\n")

        for port in range(start_port, end_port + 1):
            open_port, banner = scan_port(args.target, port)
            if open_port:
                msg = f"[OPEN] Port {port} | Banner: {banner}"
                print(msg)
                f.write(msg + "\n")

    print("\n[✓] Scan finished")
    print(f"[✓] Results saved in {args.output}")

if __name__ == "__main__":
    main()
