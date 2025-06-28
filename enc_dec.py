# enc_dec.py  – File Encrypt / Decrypt utility for SnareKit
import os, base64, hashlib, getpass
from cryptography.fernet import Fernet, InvalidToken
from colorama import Fore, Style

# ----- key derivation from password ----------------------------------------
def _derive_key(password: str) -> bytes:
    sha = hashlib.sha256(password.encode()).digest()   # 32-byte hash
    return base64.urlsafe_b64encode(sha)               # Fernet expects urlsafe b64

# ----- core helpers ---------------------------------------------------------
def _encrypt_file(src: str, dst: str, key: bytes):
    f = Fernet(key)
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        fout.write(f.encrypt(fin.read()))

def _decrypt_file(src: str, dst: str, key: bytes):
    f = Fernet(key)
    with open(src, "rb") as fin:
        try:
            data = f.decrypt(fin.read())
        except InvalidToken:
            print(Fore.RED + "❌  Wrong password or not a valid encrypted file.")
            return False
    with open(dst, "wb") as fout:
        fout.write(data)
    return True

# ----- user-facing runner ----------------------------------------------------
def run():
    print(Fore.CYAN + "\n— Encrypt / Decrypt —" + Style.RESET_ALL)
    print("[1] Encrypt a file\n[2] Decrypt a file")
    choice = input("Choose 1 or 2: ").strip()

    if choice not in ("1", "2"):
        print(Fore.RED + "Invalid selection.\n")
        return

    src = input("Path to input file: ").strip()
    if not os.path.isfile(src):
        print(Fore.RED + "File not found.\n"); return

    # default output path
    if choice == "1":
        default_out = src + ".enc"
    else:
        default_out = src.replace(".enc", "") or (src + ".dec")

    dst = input(f"Output file [{default_out}]: ").strip() or default_out
    pwd = getpass.getpass("Password: ")
    key = _derive_key(pwd)

    if choice == "1":      # Encrypt
        _encrypt_file(src, dst, key)
        print(Fore.GREEN + f"✅  Encrypted → {dst}\n")
    else:                  # Decrypt
        ok = _decrypt_file(src, dst, key)
        if ok:
            print(Fore.GREEN + f"✅  Decrypted → {dst}\n")
