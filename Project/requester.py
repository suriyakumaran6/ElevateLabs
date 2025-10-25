# requester.py
import requests
from urllib.parse import urljoin
from config import USER_AGENT, RATE_LIMIT_SEC
import time

class Requester:
    def __init__(self, base_url, rate_limit=RATE_LIMIT_SEC):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.rate_limit = rate_limit

    def get(self, path_or_url, params=None):
        url = urljoin(self.base_url, path_or_url)
        resp = self.session.get(url, params=params, timeout=15, allow_redirects=True)
        time.sleep(self.rate_limit)
        return resp

    def post(self, path_or_url, data=None):
        url = urljoin(self.base_url, path_or_url)
        resp = self.session.post(url, data=data, timeout=15, allow_redirects=True)
        time.sleep(self.rate_limit)
        return resp

    def request_raw(self, method, url, **kwargs):
        # send full URL if provided
        resp = self.session.request(method, url, timeout=15, **kwargs)
        time.sleep(self.rate_limit)
        return resp
