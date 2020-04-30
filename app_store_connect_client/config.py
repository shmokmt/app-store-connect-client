from .dataclass import frequency

# TODO: use Config class Instead of config dict.
class Config():
    def __init__(self, app_id):
        self.startTime = None
        self.endTime = None
        self.adamId = [app_id]
        self.group = None
        self.frequency = frequency.days
        self.dimensionFilters = []
        self.measures = []


class MeasuresConfig(Config):
    def __init__(self, app_id):
        self.group = {}


class SourcesConfig(Config):
    def __init__(self, app_id):
        self.measures: list = []
        self.dimension: str =  None


