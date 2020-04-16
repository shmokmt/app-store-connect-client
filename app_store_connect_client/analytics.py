class ITunes(object):
    def __init__(self, username, password, options=None):
        self.options = {
            "base_url": "https://appstoreconnect.apple.com/olympus/v1",
            "login_url": "https://idmsa.apple.com/appleauth/auth",
            "settings_url": "https://analytics.itunes.apple.com/analytics/api/v1",
            "apple_widget_key": "e0b80c3bf78523bfe80974d320935bfa30add02e1bff88ec2166c6bd5a706c42",
            "concurrent_requests": 2,
        }

        self._cookies = []
        self._queue = None
    
    def execute_request(self, task, callback):
        pass

    def request(self, query, callback):
        pass

    def change_provider(self, provider_id, callback):
        pass

    def login(self, login):
        pass

    def get_apps(self, apps):
        pass

    def get_settings(self, callback):
        pass


    def get_api_url(self, uri, callback):
        pass

    def get_headers():
        return {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://analytics.itunes.apple.com',
            'X-Requested-By': 'analytics.itunes.apple.com',
            'Referer': 'https://analytics.itunes.apple.com/',
            'Cookie': this._cookies
        };
