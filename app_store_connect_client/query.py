import enum
from datetime import datetime

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
    
    def metrics(self, config):
        self._end_point = "/data/time-series"
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
        value, unit = self._time
        if unit == "days" and type(self._time) is list:
            self.config["start"] -= value
        elif self.config["end"] > self.config["start"]:
            self.config["start"] = self.config["end"]
        else:
            raise Exception("Assemble body error.")

        return body

