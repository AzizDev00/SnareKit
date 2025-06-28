# port_scanner.py
import socket, concurrent.futures, ipaddress
from colorama import Fore, Style

def _scan(host: str, port: int, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port)); return True
        except: return False

def run():
    print(Fore.CYAN + "\n— Port Scanner —" + Style.RESET_ALL)
    target = input("Target IP / domain: ").strip()
    port_range = input("Ports (e.g. 1-1024): ").strip() or "1-1024"
    start, end = (int(x) for x in port_range.split('-'))

    # resolve
    try:
        host = str(ipaddress.ip_address(target)) if target.replace('.','').isdigit() else socket.gethostbyname(target)
    except Exception as err:
        print(Fore.RED + f"Invalid target — {err}"); return

    print(f"Scanning {host} ports {start}-{end} …")
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as exe:
        fut = {exe.submit(_scan, host, p): p for p in range(start, end+1)}
        for f in concurrent.futures.as_completed(fut):
            port = fut[f]
            if f.result():
                open_ports.append(port)
                print(Fore.GREEN + f"Port {port} open")

    if not open_ports:
        print(Fore.YELLOW + "No open ports found.")
