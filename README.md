# 🔧 SnareKit

SnareKit is a terminal-based multi-tool utility kit built in Python.  
It includes essential features for web collection, system info, scanning, encryption, and more — all wrapped in a clean CLI interface.

---

## 🚀 Features

| Tool                      | Description                                      |
|---------------------------|--------------------------------------------------|
| 🌐 Website Copier         | Save full websites (HTML, CSS, JS, images) into a zip file |
| 💻 System Info            | View system information (OS, CPU, RAM, Disk, Network) |
| 🛰️ Port Scanner           | Scan common ports on any host                    |
| 🔐 Password Generator     | Create strong random passwords                   |
| 🔒 File Encrypt/Decrypt   | Encrypt or decrypt files using a password        |
| 🌍 IP Geo Lookup          | Lookup geolocation of any public IP              |

---

## 🧱 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
Required packages:

nginx
Copy
Edit
requests
beautifulsoup4
tqdm
colorama
psutil
cryptography
💻 Usage
Run the tool:

bash
Copy
Edit
python main.py
You'll be greeted with a CLI menu like this:

markdown
Copy
Edit
Choose a tool:
  1. Website Copier to ZIP
  2. System Info
  3. Port Scanner
  4. Password Generator
  5. File Encrypt / Decrypt
  6. IP Geo Lookup
  0. Exit
🧰 Tool Usage Details
1️⃣ Website Copier
Enter a website URL (e.g., https://example.com)

Choose whether to download CSS, JS, images, internal pages

Optionally compress to .zip

Files saved under a folder named after the domain

2️⃣ System Info
Displays:

OS version

Boot time

CPU usage and cores

Memory usage

Disk space

Network interface info

3️⃣ Port Scanner
Input a domain or IP

Scans common ports (22, 80, 443, etc.)

Shows which are open or filtered

4️⃣ Password Generator
Choose password length and strength level

Generates secure password with optional symbols and caps

5️⃣ File Encrypt / Decrypt
Encrypt any file with a password

Produces .enc file

Decrypt using same password

AES-128 based (Fernet from cryptography)

6️⃣ IP Geo Lookup
Enter any public IP or leave blank for your own

Displays location (country, city, org, lat/long)

Works via ipinfo.io

🏁 Future Ideas
Subdomain scanner

Website login support

Folder hash audits

Clipboard integration

📦 Project Structure
css
Copy
Edit
SnareKit/
├── main.py
├── website_copier.py
├── sys_info.py
├── port_scanner.py
├── password_gen.py
├── enc_dec.py
├── geo_lookup.py
├── requirements.txt
└── README.md
🔓 License
MIT License — use it, remix it, extend it. Just give credit if you build on it!

👤 Author
Developed by AzizDev00
📬 Telegram: @sharafutdinov_azizbek

