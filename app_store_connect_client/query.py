import enum
from datetime import datetime

class Frequency(enum.Enum):
    days = "DAY"
    weeks = "WEEK"
    monthlys = "MONTHLY"
    

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
    def __init__(self, app_id, config=None, api_url=None, end_point=None):
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
    
        self.__time = None
    
    def metrics(self, config):
        self.end_point = "/data/time-series"
        for key in ["limit", "dimension"]:
            if config.get(key):
                del self.config[key]
        if not self.config.get("group"):
            self.config["group"] = None
        if not self.config.get("dimensionFilters"):
            self.config["dimensionFilters"] = []
        return self
    
    def sources(self, limit=200, dimension="domainReferrer"):
        self.end_point = "/data/sources/list"
        for key in ["limit", "group", "dimensionFilters"]:
            if config.get(key):
                del self.config[key]
        if not self.config.get("limit"):
            self.config["limit"] = limit
        if not self.config["dimension"]:
            self.config["dimension"] = dimension
        return self

    def date(self, start, end=None):
        self.config["start"] = datetime.strptime(start, '%Y-%m-%d')
        if end is not None:
            self.config["end"] = datetime.strptime(end, '%Y-%m-%d')
        return self
        
    def time(self, value, unit):
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
        body = cfg
        #TODO: time のケア
        return body

