# password_gen.py
import secrets, string
from colorama import Fore, Style

def run():
    print(Fore.CYAN + "\n— Password Generator —" + Style.RESET_ALL)
    length = int(input("Password length (default 16): ") or 16)
    use_symbols = input("Include symbols? (y/n): ").lower().startswith('y')

    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation

    pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
    print(Fore.GREEN + f"\nGenerated password:\n{Style.BRIGHT}{pwd}")
