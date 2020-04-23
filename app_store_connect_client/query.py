from datetime import date, datetime
from urllib.parse import urlparse
from . import enum
class Query(object):
    def __init__(self, app_id):
        self.app_id = app_id
        self.config = {
            "start": None,
            "end": None,
            "group": None,
            "frequency": "DAY",
            "dimensionFilters": [],
        }
        self._api_url = 'https://analytics.itunes.apple.com/analytics/api/v1'
        self._end_point = None
        self._time = None
    
    @property
    def analytics_url(self):
        return urlparse(self._api_url + self._end_point).geturl()
    
    def metrics(self, config):
        self._end_point = "/data/time-series"
        for key in ["limit", "dimension"]:
            if config.get(key):
                del self.config[key]
        if not self.config.get("group"):
            self.config["group"] = None
        if not self.config.get("dimensionFilters"):
            self.config["dimensionFilters"] = []
        if not self.config.get("measures"):
            self.config["measures"] = [enum.Measures.installs.value, enum.Measures.crashes.value]
        return self
    
    def sources(self, config):
        self._end_point = "/data/sources/list"
        for key in ["limit", "group", "dimensionFilters"]:
            if self.config.get(key):
                del self.config[key]
        if not self.config.get("limit"):
            self.config["limit"] = 200
        if not self.config.get("dimension"):
            self.config["dimension"] = "domainReferer"
        self.config.update(config)
        return self
    

    def date(self, start, end=None):
        self.config["start"] = start
        self.config["end"] = end
        return self
        

    def assemble_body(self):
        body = {
            "startTime": str(self.config["start"]),
            "endTime": str(self.config["end"]),
            "adamId": [self.app_id]
        }
        body.update(self.config)
        del body["start"]
        del body["end"]
        return body

