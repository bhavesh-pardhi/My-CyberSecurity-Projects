import socket
import argparse
from colorama import init, Fore
from datetime import datetime

# Initialize colorama
init(autoreset=True)

def scan_ports(target, ports):
    print(Fore.YELLOW + f"\n[~] Starting scan on {target}")
    print(Fore.YELLOW + f"[~] Time started: {datetime.now()}\n")

    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(Fore.GREEN + f"[+] Port {port} is open")
            s.close()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan interrupted by user. Exiting...")
        exit()
    except socket.gaierror:
        print(Fore.RED + "[!] Hostname could not be resolved.")
        exit()
    except socket.error:
        print(Fore.RED + "[!] Could not connect to server.")
        exit()

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--top", action="store_true", help="Scan top 1000 ports")
    group.add_argument("-a", "--all", action="store_true", help="Scan all 65535 ports")
    parser.add_argument("target", help="Target IP or domain")

    args = parser.parse_args()
    target = socket.gethostbyname(args.target)

    if args.top:
        ports = range(1, 1001)
    elif args.all:
        ports = range(1, 65536)

    try:
        scan_ports(target, ports)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] User aborted. Bye! 💔")
        exit()

if __name__ == "__main__":
    main()
