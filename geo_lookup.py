# geo_lookup.py
import requests
import ipaddress
from colorama import Fore, Style

def run():
    print(Fore.CYAN + "\n— IP Geo Lookup —" + Style.RESET_ALL)
    ip = input("Enter IP (or leave blank for your IP): ").strip()

    if ip:
        # Check for private IP
        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.is_private:
                print(Fore.YELLOW + "⚠️ This is a private IP — no location data available.\n")
                return
        except ValueError:
            print(Fore.RED + "❌ Invalid IP address.\n")
            return

        url = f"https://ipinfo.io/{ip}/json"
    else:
        url = "https://ipinfo.io/json"

    try:
        r = requests.get(url, timeout=5)
        data = r.json()
        print()
        for key in ['ip', 'city', 'region', 'country', 'loc', 'org']:
            print(f"{key.title():<10}: {data.get(key, 'N/A')}")
    except Exception as e:
        print(Fore.RED + f"❌ Failed to retrieve data: {e}")
