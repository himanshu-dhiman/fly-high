
class PlanRequestDTO():

    def __init__(self, **kwargs):

        self.source: str = kwargs.get("source", "")