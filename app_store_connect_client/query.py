from datetime import date, datetime
from urllib.parse import urlparse
from .dataclass import 

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
        self._api_url = "https://analytics.itunes.apple.com/analytics/api/v1"
        self._end_point = None
        self._time = None

    @property
    def analytics_url(self):
        return urlparse(self._api_url + self._end_point).geturl()

    def _clean_config(self, keys):
        for key in keys:
            if config.get(key):
                del self.config[key]

    def metrics(self, config):
        self._end_point = "/data/time-series"
        self._clean_config(["limit", "dimension"])
        if not self.config.get("group"):
            self.config["group"] = None
        if not self.config.get("dimensionFilters"):
            self.config["dimensionFilters"] = []
        if not self.config.get("measures"):
            self.config["measures"] = [
                .Measures.installs.value,
                enum.Measures.crashes.value,
            ]
        return self

    def sources(self, config):
        # config で measures と dimension が主に入ってくるのかな？
        self._end_point = "/data/sources/list"
        self._clean_config(["limit", "group", "dimensionFilters"])
        if not self.config.get("limit"):
            self.config["limit"] = 200
        if not self.config.get("dimension"):
            self.config["dimension"] = "domainReferer"
        self.config.update(config)
        return self
    
    def limit(self, limit=200):
        self.config["limit"] = limit

    def _validate_date(self, start, end):
        try:
            datetime.strptime(start, "%Y-%m-%d")
            if end:
                datetime.strptime(end, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect format, shoube be YYYY-MM-DD.")

    def date(self, start, end=None):
        # TODO: Support datetime
        self._validate_date(start, end)
        self.config["start"] = start + "T00:00:000Z"
        self.config["end"] = end + "T00:00:000Z"
        return self

    def assemble_body(self):
        self.config["adamId"] = [self.app_id]
        self.config["startTime"] = self.config.pop("start")
        self.config["endTime"] = self.config.pop("end")
        return self.config
