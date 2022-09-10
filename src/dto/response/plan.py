class PlanResponseDTO():

    def __init__(self, **kwargs):

        self.data: dict = kwargs.get("data", {})
        self.status: str = kwargs.get("status", "")
        self.message: str = kwargs.get("message", "")
