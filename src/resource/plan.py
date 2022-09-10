import json
from flask_restful import Resource, request
from src.dto.request.plan import PlanRequestDTO
from src.dto.response.plan import PlanResponseDTO

from base_constants import app_root
from src.services.plan_service import PlanService

class Plan(Resource):

    def __init__(self) -> None:
        super().__init__()

        self.plan_service = PlanService()

    def post(self):
        data = json.loads(request.data)

        try:

            plan_request_dto = self.__validate_request(data)

            trip_plan = self.plan_service.get_trip_plan_for_source(plan_request_dto)

            return PlanResponseDTO(
                data=trip_plan,
                status="SUCCESS",
                message="Trip planned successfully"
            ).__dict__
            
        except Exception as e:

            return PlanResponseDTO(
                message=str(e),
                status="FAILURE"
            ).__dict__


    def __validate_request(self, data): 

        if 'source' not in data and data.get("source") != "":
            raise Exception("Source is not present");

        return PlanRequestDTO(
            source=data.get("source")
        )