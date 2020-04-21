import requests
import asyncio
from urllib.parse import urlparse
import re
import json
class ITunes(object):
    def __init__(self, username, password, options=None):
        self.options = {
            "base_url": "https://appstoreconnect.apple.com/olympus/v1",
            "login_url": "https://idmsa.apple.com/appleauth/auth",
            "settings_url": "https://analytics.itunes.apple.com/analytics/api/v1",
            "apple_widget_key": "e0b80c3bf78523bfe80974d320935bfa30add02e1bff88ec2166c6bd5a706c42",
        }

        self.session = requests.Session()
        self._queue = asyncio.Queue(maxsize=2)
        
        if self.options.get("cookies") is None:
            self.login(username, password)
        else:
            self._cookies = self.options["cookies"]
    
    def execute_request(self, task, callback):
        query = task.query
        completed = task.completed
        request_body = query.assemble_body()
        uri = urlparse(query.api_url + query.endpoint)
        r = requests.post(uri, headers=self.get_headers(), timeout=300000, data=request_body)
        if r.status_code == 401:
            raise Exception("This request requires authentication. Please check your username and password.")

    def request(self, query, callback):
        pass

    def change_provider(self, provider_id, callback):
        pass

    def login(self, username, password):
        payload = {
            'accountName': username, 'password': password, 'rememberMe': False
        }
        headers = {
            'Content-Type': 'application/json',
            'X-Apple-Widget-Key': self.options["apple_widget_key"]
        }
        r = self.session.post(self.options["login_url"] + "/signin", json=payload, headers=headers)
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'scnt': r.headers['scnt'],
            'X-Apple-ID-Session-Id': r.headers['x-apple-id-session-id'],
            'X-Requested-With': 'XMLHttpRequest',
            'X-Apple-Domain-Id': '3',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
        };

        print("Enter the 2FA code:")
        two_factor_auth_code = input()
        self.session.post(self.options["login_url"] + "/verify/trusteddevice/securitycode", headers=headers, data={'securityCode': {'code': two_factor_auth_code}})
        r = self.session.post(self.options["login_url"] + "/2sv/trust", headers=headers)
        cookies = r.headers['set-cookie']
        if cookies is None or len(cookies) == 0:
            raise Exception("There was a problem with loading the login page cookies. Check login credentials.")

        self.session.get(self.options["base_url"] + "/session", allow_redirects=False)
        if 'myacinfo' not in self.session.cookies.get_dict().keys():
            raise Exception("There was a problem with loading the login page cookies. Check login credentials.")

        if 'itctx' not in self.session.cookies.get_dict().keys():
            raise Exception("No itCtx cookie :( Apple probably changed the login process")



        

    def get_apps(self):
        url = self.options['settings_url'] + '/app-info/all'
        self.get_api_url(url)

    def get_settings(self):
        url = self.options['settings_url'] + '/settings/all'
        self.get_api_url(url)


    def get_api_url(self, url):
        res = self.session.get(url, headers=self.get_headers(), timeout=500)
        print(json.dumps(res.text, indent=4))



    def get_cookies(self):
        cookies = self.session.cookies.get_dict()
        return cookies["myacinfo"] + " " + cookies["itctx"]

    def get_headers(self):
        return {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://analytics.itunes.apple.com',
            'X-Requested-By': 'analytics.itunes.apple.com',
            'Referer': 'https://analytics.itunes.apple.com/',
#            'Cookie': self.get_cookies()
        };
