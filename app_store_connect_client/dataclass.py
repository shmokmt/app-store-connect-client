from typing import NamedTuple


class Frequency(NamedTuple):
    days: str
    weekly: str
    monthly: str


class Measures(NamedTuple):
    installs: str
    uninstalls: str
    sessions: str
    page_views: str
    active_devices: str
    active_last_30days: str
    crashes: str
    paying_users: str
    units: str
    sales: str
    iap: str
    impressions: str
    impressions_unique: str
    page_view_unique: str


class Dimension(NamedTuple):
    app_version: str
    campaigns: str
    device: str
    platform_version: str
    region: str
    territory: str
    websites: str
    apps: str
    source_type: str


class DimensionFilterKey(NamedTuple):
    app_purchase_week: str
    app_purchase_day: str
    app_purchase_month: str
    app_version: str
    campaigns: str
    device: str
    platform_version: str
    territory: str
    region: str
    websites: str


class Platform(NamedTuple):
    iphone: str
    ipad: str
    ipod: str
    apple_tv: str


class QueryType(NamedTuple):
    sources: str
    metrics: str


query_type = QueryType(sources="sources", metrics="metrics")

frequency = Frequency(days="days", weekly="weekly", monthly="monthly")

measures = Measures(
    installs="installs",
    uninstalls="uninstalls",
    sessions="sessions",
    page_views="pageViewCount",
    active_devices="activeDevices",
    active_last_30days="rollingActiveDevices",
    crashes="crashes",
    paying_users="payingUses",
    units="units",
    sales="sales",
    iap="iap",
    impressions="impressionsTotal",
    impressions_unique="impressionsTotalUnique",
    page_view_unique="pageViewUnique",
)

dimension = Dimension(
    app_version="appVersion",
    campaigns="campaignId",
    device="platform",
    platform_version="platformVersion",
    region="region",
    territory="storefront",
    websites="domainReferrer",
    apps="appReferrer",
    source_type="source",
)

dimension_filter_key = DimensionFilterKey(
    app_purchase_week="apppurchaseweek",
    app_purchase_day="apppurchaseday",
    app_purchase_month="apppurchasemonth",
    app_version="appVersion",
    campaigns="campaignId",
    device="platform",
    platform_version="PlatformVersion",
    territory="storefront",
    region="region",
    websites="domainReferrer",
)

platform = Platform(iphone="iPhone", ipad="iPad", ipod="iPod", apple_tv="AppleTV")

query_type = QueryType(sources="sources", metrics="metrics")
