# website_copier.py
import os, zipfile, requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
from colorama import Fore, Style

def _clean(path: str) -> str:
    return 'index.html' if path in ('', '/') else path.strip('/').replace('/', '_') + ('' if path.endswith('.html') else '.html')

def _unique(name: str) -> str:
    i, folder = 1, name
    while os.path.exists(folder):
        folder = f"{name}_{i}"; i += 1
    return folder

def _get(session, url, folder):
    os.makedirs(folder, exist_ok=True)
    fname = os.path.basename(urlparse(url).path) or None
    if not fname: return None
    local = os.path.join(folder, fname)
    if not os.path.exists(local):
        try:
            r = session.get(url, timeout=10); r.raise_for_status()
            with open(local, 'wb') as f: f.write(r.content)
        except Exception: return None
    return local

def _crawl(base, out, inc_img, inc_js, inc_css, inc_internal):
    session = requests.Session(); dom = urlparse(base).netloc
    todo, seen = [base], {}
    bar = tqdm(total=0, unit="pg", desc="Fetching")

    while todo:
        url = todo.pop(0)
        if url in seen: continue
        bar.update(1)
        try:
            doc = session.get(url, timeout=10).text
            soup = BeautifulSoup(doc, 'html.parser')
        except Exception: continue

        loc_name = _clean(urlparse(url).path); seen[url] = loc_name

        for a in soup.find_all('a', href=True):
            full = urljoin(url, a['href']); p = urlparse(full)
            if p.netloc == dom:
                a['href'] = _clean(p.path)
                if inc_internal and full not in seen and full not in todo:
                    todo.append(full); bar.total += 1  # extend progress bar

        if inc_css:
            for tag in soup.find_all('link', rel='stylesheet'):
                src = tag.get('href'); full = urljoin(url, src)
                local = _get(session, full, os.path.join(out, 'css'))
                if local: tag['href'] = os.path.relpath(local, out)

        if inc_js:
            for tag in soup.find_all('script', src=True):
                src = tag['src']; full = urljoin(url, src)
                local = _get(session, full, os.path.join(out, 'js'))
                if local: tag['src'] = os.path.relpath(local, out)

        if inc_img:
            for tag in soup.find_all('img', src=True):
                src = tag['src']; full = urljoin(url, src)
                local = _get(session, full, os.path.join(out, 'images'))
                if local: tag['src'] = os.path.relpath(local, out)

        with open(os.path.join(out, loc_name), 'w', encoding='utf-8') as f:
            f.write(str(soup))
    bar.close()

def run():
    print(Fore.CYAN + "\n— Website Copier —" + Style.RESET_ALL)
    base = input("URL to copy: ").strip()
    inc_css    = input("Include CSS? (y/n): ").lower().startswith('y')
    inc_js     = input("Include JS?  (y/n): ").lower().startswith('y')
    inc_img    = input("Include img? (y/n): ").lower().startswith('y')
    inc_int    = input("Download linked internal pages? (y/n): ").lower().startswith('y')
    compress   = input("Zip after download? (y/n): ").lower().startswith('y')

    folder = _unique(urlparse(base).netloc.replace("www.",""))
    os.makedirs(folder, exist_ok=True)
    _crawl(base, folder, inc_img, inc_js, inc_css, inc_int)

    if compress:
        zname = folder + ".zip"
        with zipfile.ZipFile(zname, 'w', zipfile.ZIP_DEFLATED) as z:
            for root,_,files in os.walk(folder):
                for f in files:
                    fp = os.path.join(root,f)
                    z.write(fp, arcname=os.path.relpath(fp,folder))
        print(Fore.GREEN + f"\nSaved & zipped as {zname}")
    else:
        print(Fore.GREEN + f"\nSaved in folder {folder}")
