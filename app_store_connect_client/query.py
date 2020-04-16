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
            "group": null,
            "frequency": "DAY",
            "dimensionFilters": [],
        }
        self.api_url = 'https://analytics.itunes.apple.com/analytics/api/v1'
    
        self.config.update(config)

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