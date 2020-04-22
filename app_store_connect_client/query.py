import enum
from datetime import datetime

class Frequency(enum.Enum):
    day = "DAY"
    week = "WEEK"
    monthly = "MONTHLY"
    

class Measures(enum.Enum):
    installs = "installs"
    uninstalls = "uninstalls"
    sessions = "sessions"
    page_views = "pageViewCount"
    active_devices = "activeDevices"
    active_last_30days = "rollingActiveDevices"
    crashes = "crashes"
    paying_users = "payingUses"
    units = "units"
    sales = "sales"
    iap = "iap"
    impressions = "impressionsTotal"
    impressions_unique = "impressionsTotalUnique"
    page_view_unique = "pageViewUnique"

class Dimension(enum.Enum):
    app_version = "appVersion"
    campaigns = "campaignId"
    device = "platform"
    platform_version = "platformVersion"
    region = "region"
    territory = "storefront"
    websites = "domainReferrer"
    apps = "appReferrer"
    source_type = "source"

class DimensionFilterKey(enum.Enum):
    app_purchase_week = "apppurchaseweek"
    app_purchase_day = "apppurchaseday"
    app_purchase_month = "apppurchasemonth"
    app_version = "appVersion"
    campaigns = "campaignId"
    device = "platform"
    platform_version = "PlatformVersion"
    territory = "storefront"
    region = "region"
    websites = "domainReferrer"

class Platform(enum.Enum):
    iphone = "iPhone"
    ipad = "iPad"
    iPod = "iPod"
    apple_tv = "AppleTV"

class QueryType(enum.Enum):
    sources = "sources"
    metrics = "metrics"


class Query(object):
    def __init__(self, app_id, config, api_url=None, end_point=None):
        self.app_id = app_id
        self.config = {
            "start": None,
            "end": None,
            "group": None,
            "frequency": "DAY",
            "dimensionFilters": [],
        }
        self.api_url = 'https://analytics.itunes.apple.com/analytics/api/v1'
        self.end_point = None
    
        self.config.update(config)
        self.__time = None
    
    def metrics(self, config):
        endpoint = "/data/time-series"
        for key in ["limit", "dimension"]:
            del self.config[key]
        
        defaults = [
            {"key": 'group', 'value': None},
            {"key": 'dimensionFilters', 'value': []}
        ]

        return self
    
    def date(self, start, end=None):
        self.config["start"] = datetime.strptime(start, '%Y-%m-%d')
        if end is not None:
            self.config["end"] = datetime.strptime(end, '%Y-%m-%d')
        return self
        
    def time(self, value, unit):
        # e.g. .time(1, 'days')
        self._time = value, unit
        return self

    def limit(self, limit):
        self.config["limit"] = limit
        return self
    
    def assemble_body(self):
        body = {
            "startTime": self.config["start"],
            "endTime": self.config["end"],
            "admId": self.app_id
        }
        cfg = {}
        cfg.update(self.config)
        del cfg["start"]
        del cfg["end"]
        for key, value in cfg.items():
            if value is None:
                del(cfg[key])
        return cfg

    def sources(self, limit=200, dimension="domainReferrer"):
        self.end_point = "/data/sources/list"
        for key in ["limit", "group", "dimensionFilters"]:
            del self.config[key]
        # if self.config["limit"] is None:
        #     self.config["limit"] = 200
        # if self.config["dimension"] is None:
        #     self.config["dimension"] = dimension
        return self
