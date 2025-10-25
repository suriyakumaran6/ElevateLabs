# scanner.py
import queue
from requester import Requester
from crawler import extract_links, extract_forms, same_domain
from xss_tester import test_reflected_xss_get, test_forms_for_xss, XSS_MARKER
from db import init_db, insert_endpoint
from config import TARGET, MAX_DEPTH, ALLOWED_HOSTS
from urllib.parse import urlparse

def run_scan(base_url=TARGET, max_depth=MAX_DEPTH):
    init_db()
    requester = Requester(base_url)
    visited = set()
    q = queue.Queue()
    q.put((base_url, 0))
    print(f"[+] Starting scan on {base_url} (max depth {max_depth})")
    while not q.empty():
        url, depth = q.get()
        if url in visited or depth > max_depth:
            continue
        visited.add(url)
        try:
            resp = requester.get(url)
            html = resp.text or ""
            # record endpoint
            insert_endpoint(url, method="GET", params="")
            # quick XSS test on GET param reflection
            xss_results = test_reflected_xss_get(requester, url)
            if xss_results:
                print(f"[!] XSS findings on {url}: {len(xss_results)}")
            # extract forms and test them
            forms = extract_forms(html, base_url)
            for f in forms:
                fr = test_forms_for_xss(requester, f)
                if fr:
                    print(f"[!] XSS in form on {f['action']}")
            # extract links
            links = extract_links(html, base_url)
            for link in links:
                if same_domain(link, ALLOWED_HOSTS) and link not in visited:
                    q.put((link, depth + 1))
        except Exception as e:
            print(f"[-] Error fetching {url}: {e}")
    print("[+] Scan complete.")

if __name__ == "__main__":
    run_scan()
