# main.py  –  SnareKit master menu
from colorama import Fore, Style, init
init(autoreset=True)

# ── import SnareKit modules ────────────────────────────────────────────────
import website_copier
import sys_info          # Windows-oriented system info
import port_scanner
import password_gen
import enc_dec           # NEW: Encrypt / Decrypt (replaces File Hasher)
import geo_lookup
# ───────────────────────────────────────────────────────────────────────────

VERSION = "v1.0"

BANNER = (
    Fore.CYAN
    + r"""
███████╗███╗   ██╗ █████╗ ██████╗ ███████╗██╗  ██╗██╗████████╗
██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║╚══██╔══╝
███████╗██╔██╗ ██║███████║██████╔╝█████╗  █████╔╝ ██║   ██║   
╚════██║██║╚██╗██║██╔══██║██╔══██╗██╔══╝  ██╔═██╗ ██║   ██║   
███████║██║ ╚████║██║  ██║██║  ██║███████╗██║  ██╗██║   ██║   
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝
"""
    + Style.BRIGHT
    + f"                     [ SnareKit {VERSION} ]"
    + Style.RESET_ALL
)

MENU = f"""
{Fore.YELLOW}Choose a tool:{Style.RESET_ALL}
  1. Website Copier to ZIP
  2. System Info
  3. Port Scanner
  4. Password Generator
  5. File Encrypt / Decrypt
  6. IP Geo Lookup
  0. Exit
"""

def main() -> None:
    while True:
        print(BANNER)
        print(MENU)
        choice = input(f"{Fore.GREEN}>>> {Style.RESET_ALL}").strip()

        match choice:
            case "1": website_copier.run()
            case "2": sys_info.run()
            case "3": port_scanner.run()
            case "4": password_gen.run()
            case "5": enc_dec.run()      # updated
            case "6": geo_lookup.run()
            case "0":
                print(Fore.CYAN + "\n👋  Exiting SnareKit. Bye!" + Style.RESET_ALL)
                break
            case _:
                print(Fore.RED + "Invalid choice!\n")

        input(f"{Fore.MAGENTA}\nPress Enter to return to menu…{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
