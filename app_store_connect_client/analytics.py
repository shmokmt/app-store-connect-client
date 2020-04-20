import requests
import asyncio
from urllib.parse import urlparse
class ITunes(object):
    def __init__(self, username, password, options=None):
        self.options = {
            "base_url": "https://appstoreconnect.apple.com/olympus/v1",
            "login_url": "https://idmsa.apple.com/appleauth/auth",
            "settings_url": "https://analytics.itunes.apple.com/analytics/api/v1",
            "apple_widget_key": "e0b80c3bf78523bfe80974d320935bfa30add02e1bff88ec2166c6bd5a706c42",
        }

        self._cookies = []
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
        # resolvewithfullrepsponse?
        payload = {
            'accountName': username, 'password': password, 'rememberMe': False
        }
        headers = {
            'Content-Type': 'application/json',
            'X-Apple-Widget-Key': self.options["apple_widget_key"]
        }
        r = requests.post(self.options["login_url"] + "signin", data=payload, headers=headers)
        if r.status_code != 409:
            raise Exception("409 Conflict.")
        
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
        #TODO 2FAの処理
        cookies = r.headers['set-cookie']
        if !(cookies and len(cookies) == 0):
            raise Exception("There was a problem with loading the login page cookies. Check login credentials.")


        

    def get_apps(self, apps, callback):
        url = self.options['settings_url'] + '/app-info/all'
        self.get_api_url(url, callback)

    def get_settings(self, callback):
        url = self.options['settings_url'] + '/settings/all'
        self.get_api_url(url, callback)


    def get_api_url(self, uri, callback):
        pass


    def get_cookies(self):
        return self._cookies

    def get_headers(self):
        return {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://analytics.itunes.apple.com',
            'X-Requested-By': 'analytics.itunes.apple.com',
            'Referer': 'https://analytics.itunes.apple.com/',
            'Cookie': self._cookies
        };
