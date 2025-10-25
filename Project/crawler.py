# crawler.py
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

def extract_links(html, base_url):
    soup = BeautifulSoup(html, "lxml")
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        # Normalize
        full = urljoin(base_url, href)
        links.add(full)
    return links

def extract_forms(html, base_url):
    soup = BeautifulSoup(html, "lxml")
    forms = []
    for form in soup.find_all("form"):
        action = form.get("action") or ""
        method = form.get("method", "get").upper()
        inputs = []
        for inp in form.find_all(["input", "textarea", "select"]):
            name = inp.get("name")
            if not name:
                continue
            input_type = inp.get("type", "text")
            value = inp.get("value", "")
            inputs.append({"name": name, "type": input_type, "value": value})
        forms.append({"action": urljoin(base_url, action), "method": method, "inputs": inputs})
    return forms

def same_domain(url, allowed_hosts):
    try:
        host = urlparse(url).hostname or ""
        return any(h in host for h in allowed_hosts)
    except:
        return False
