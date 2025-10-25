# xss_tester.py
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from db import insert_endpoint, insert_finding

# A safe marker to reflect — non-destructive, no scripts that pop up.
XSS_MARKER = "INJ_XSS_9b3"

XSS_PAYLOADS = [
    XSS_MARKER,
    f"<svg/onload=void(document.title='{XSS_MARKER}')>",  # a harmless DOM-visible trick
    f"'><{XSS_MARKER}>",
]

def test_reflected_xss_get(requester, url, db_allowed=True):
    """
    Sends simple GET payloads by appending a parameter to URL.
    Returns list of findings.
    """
    findings = []
    # naive param injection: add ?injection=...
    for payload in XSS_PAYLOADS:
        test_url = url
        sep = "&" if "?" in url else "?"
        test_url = f"{url}{sep}injection={payload}"
        resp = requester.get(test_url)
        body = resp.text or ""
        if XSS_MARKER in body:
            eid = insert_endpoint(url, method="GET", params="injection")
            evidence = f"payload={payload}\nresponse_snippet={body[:400]}"
            fid = insert_finding(eid, "XSS-REFLECTED", payload, evidence, "High")
            findings.append({"endpoint_id": eid, "vuln_type": "XSS-REFLECTED", "payload": payload, "evidence": evidence})
    return findings

def test_forms_for_xss(requester, form):
    findings = []
    # submits form with marker in all fields
    action = form["action"]
    method = form["method"].upper()
    data = {}
    for inp in form["inputs"]:
        data[inp["name"]] = XSS_MARKER
    if method == "GET":
        resp = requester.get(action, params=data)
    else:
        resp = requester.post(action, data=data)
    if XSS_MARKER in (resp.text or ""):
        eid = insert_endpoint(action, method=method, params=",".join([i["name"] for i in form["inputs"]]))
        evidence = f"form_payload={data}\nresponse_snippet={(resp.text or '')[:400]}"
        insert_finding(eid, "XSS-FORM", str(data), evidence, "High")
        findings.append({"endpoint_id": eid, "vuln_type": "XSS-FORM", "payload": str(data), "evidence": evidence})
    return findings
