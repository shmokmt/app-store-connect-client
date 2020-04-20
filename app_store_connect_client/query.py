import enum


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
    def __init__(self, app_id, config, api_url=None):
        self.app_id = app_id
        self.config = {
            "start": None,
            "end": None,
            "group": None,
            "frequency": "DAY",
            "dimensionFilters": [],
        }
        self.api_url = 'https://analytics.itunes.apple.com/analytics/api/v1'
    
        self.config.update(config)

# AnalyticsQuery オブジェクトは実装しない


# TODO Replace below with Python.
#  if (!_.isArray(this.config.measures)) {
#    this.config.measures = [this.config.measures];
#  }
#
        self.__time = None
    
    def metrics(self):
        endpoint = "/data/time-series"
        for key in ["limit", "dimension"]:
            #TODO configのdictからlimit と dimensionをkeyに持つものを削除
            pass
    
    def date(self, start, end=None):
        #js : to moment object.
        self.config["start"] = start
        if end is not None:
            self.config["end"] = end
        
    def time(self, value, unit):
        self._time = value, unit

    def limit(self, limit):
        config["limit"] = limit
    
    def assemble_body(self):
        # convert datetime obj?
        # self.config["start"]
        # self.config["end"]
        if hoge:
            pass

        elif foo:
            pass

        timestamp_format = "YYYY-"

        if type(self.config["measures"]) is not list:
            self.config["measures"] = list(self.config["measures"])
        
        body = {
            "start_time": self.config["start"],
            "end_time": self.config["end"],
            "admId": 
        }

    def sources(self):
        end_point = "/data/sources/list"
        for key in ["limit", "group", "dimensionFilters"]:
            #TODO: KeyError handling.
            del self.config[key]
        
        defaults = [
            {"key": "limit", "value": 200},
            {"key": "dimension", "value": "domainReferrer"}
        ]

        #TODO: KeyError handling