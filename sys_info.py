# sys_info.py  – System-information module (Windows-oriented)
import platform
import socket
import psutil
import shutil
import os
from datetime import datetime
from colorama import Fore, Style

def _bytes_to_gb(num):
    return f"{num / (1024 ** 3):.1f} GB"

def run():
    print(Fore.CYAN + "\n— Windows System Information —" + Style.RESET_ALL)

    uname = platform.uname()
    win_ver = platform.win32_ver()
    boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d  %H:%M:%S")

    # --- OS / basic ----
    print(f"OS           : Windows {win_ver[0]}  {win_ver[1]}  (Build {win_ver[2]})")
    print(f"Kernel       : {uname.release}  {uname.version.split(' ')[0]}")
    print(f"Boot time    : {boot_time}")
    print(f"Architecture : {uname.machine}")
    print(f"Hostname     : {socket.gethostname()}")
    print(f"Username     : {os.getlogin()}")

    # --- CPU ----
    print("\n" + Fore.YELLOW + "CPU" + Style.RESET_ALL)
    print(f"Cores (logical) : {psutil.cpu_count(logical=True)}")
    print(f"Cores (physical): {psutil.cpu_count(logical=False)}")
    if psutil.cpu_freq():
        print(f"Base freq        : {psutil.cpu_freq().max:.0f} MHz")
    print(f"CPU utilization  : {psutil.cpu_percent(interval=1)} %")

    # --- Memory ----
    print("\n" + Fore.YELLOW + "Memory" + Style.RESET_ALL)
    vmem = psutil.virtual_memory()
    print(f"Total   : {_bytes_to_gb(vmem.total)}")
    print(f"Used    : {_bytes_to_gb(vmem.used)}  ({vmem.percent} %)")
    print(f"Free    : {_bytes_to_gb(vmem.available)}")

    # --- Disk ----
    print("\n" + Fore.YELLOW + "Disk (C:)" + Style.RESET_ALL)
    usage = shutil.disk_usage("C:\\")
    print(f"Total   : {_bytes_to_gb(usage.total)}")
    print(f"Free    : {_bytes_to_gb(usage.free)}  ({usage.free / usage.total * 100:.0f} % free)")

    # --- Network (first active interface) ----
    print("\n" + Fore.YELLOW + "Network" + Style.RESET_ALL)
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    for iface, add_list in addrs.items():
        if stats.get(iface, None) and stats[iface].isup:
            ip4 = next((a.address for a in add_list if a.family.name == "AF_INET"), None)
            mac = next((a.address for a in add_list if a.family.name == "AF_LINK"), None)
            print(f"Interface : {iface}")
            print(f"IPv4      : {ip4}")
            print(f"MAC       : {mac}")
            break
