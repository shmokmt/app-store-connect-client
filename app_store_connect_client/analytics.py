import requests
from urllib.parse import urlparse
import json
from . import query


class Client(object):
    def __init__(self, username, password, is_2fa_auth=False):
        self.is_2fa_auth = is_2fa_auth

        self._session = requests.Session()
        self._options = {
            "base_url": "https://appstoreconnect.apple.com/olympus/v1",
            "login_url": "https://idmsa.apple.com/appleauth/auth",
            "settings_url": "https://analytics.itunes.apple.com/analytics/api/v1",
            "apple_widget_key": "e0b80c3bf78523bfe80974d320935bfa30add02e1bff88ec2166c6bd5a706c42",
        }
        self._headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://analytics.itunes.apple.com",
            "X-Requested-By": "analytics.itunes.apple.com",
            "Referer": "https://analytics.itunes.apple.com/",
        }

        self._login(username, password)

    def _login(self, username, password):
        payload = {"accountName": username, "password": password, "rememberMe": False}
        headers = {
            "Content-Type": "application/json",
            "X-Apple-Widget-Key": self._options["apple_widget_key"],
        }
        r = self._session.post(
            self._options["login_url"] + "/signin", json=payload, headers=headers
        )

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "scnt": r.headers["scnt"],
            "X-Apple-ID-Session-Id": r.headers["x-apple-id-session-id"],
            "X-Requested-With": "XMLHttpRequest",
            "X-Apple-Domain-Id": "3",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
        }

        if self.is_2fa_auth:
            print("Enter the 2FA code:")
            two_factor_auth_code = input()
            self._session.post(
                self._options["login_url"] + "/verify/trusteddevice/securitycode",
                headers=headers,
                data={"securityCode": {"code": two_factor_auth_code}},
            )
        r = self._session.post(
            self._options["login_url"] + "/2sv/trust", headers=headers
        )
        cookies = r.headers["set-cookie"]
        if cookies is None or len(cookies) == 0:
            raise Exception(
                "There was a problem with loading the login page cookies. Check login credentials."
            )

        self._session.get(self._options["base_url"] + "/session", allow_redirects=False)
        if "myacinfo" not in self._session.cookies.get_dict().keys():
            raise Exception(
                "There was a problem with loading the login page cookies. Check login credentials."
            )

        if "itctx" not in self._session.cookies.get_dict().keys():
            raise Exception(
                "No itCtx cookie :( Apple probably changed the login process"
            )

    def _get_api_url(self, url):
        res = self.session.get(url, headers=self._headers, timeout=500)

    def get_apps(self):
        url = self.options["settings_url"] + "/app-info/all"
        self._get_api_url(url)

    def get_settings(self):
        url = self.options["settings_url"] + "/settings/all"
        self._get_api_url(url)

    def change_provider(self, provider_id):
        # TODO: check the workking currect.
        data = {"provider": {"providerId": provider_id}}
        self._session.post(url=self._options["base_url"])

    def execute(self, query=None):
        request_body = query.assemble_body()
        res = self._session.post(
            query.analytics_url,
            headers=self._headers,
            timeout=300000,
            json=request_body,
        )
        if res.status_code == 401:
            raise Exception(
                "This request requires authentication. Please check your username and password."
            )
        if res.status_code == 400:
            raise Exception("400 Bad Request. Please check your config.")
        return res.json()
