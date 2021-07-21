from app.utils.utils import Utils
from flask_restful import Resource


# /status
class StatusEndpoint(Resource):
    def get(self):
        return Utils.customResponse({
            "status": 200,
            "message": "Service online"
        })
