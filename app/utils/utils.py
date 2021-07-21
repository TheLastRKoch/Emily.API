from datetime import datetime
from flask import Response
import json


class Utils:
    @classmethod
    def customResponse(self, response):

        return Response(
            json.dumps(
                {"msg": {
                    "status": response["status"],
                    "message": response["message"]
                }}),
            mimetype='application/json', status=int(response["status"]))

    @classmethod
    def unauthorizedResponse(self, exception):
        response = {
            "status": 401,
            "message": "Unauthorized",
            "exception": exception
            }
        return self.customResponse(response, exception)

    @classmethod
    def successfullyResponse(self, exception):
        response = {"status": 200, "message": "Ok"}
        return self.customResponse(response, exception)

    @classmethod
    def createdResponse(self, exception):
        response = {"status": 201, "message": "Created Successfully"}
        return self.customResponse(response, exception)

    @classmethod
    def deletedResponse(self, exception):
        response = {"status": 200, "message": "Deleted Successfully"}
        return self.customResponse(response, exception)

    @classmethod
    def updatedResponse(self, exception):
        response = {"status": 200, "message": "Updated Successfully"}
        return self.customResponse(response, exception)

    @classmethod
    def retrievedResponse(self, exception):
        response = {"status": 200, "message": "Retrieved Successfully"}
        return self.customResponse(response, exception)

    @classmethod
    def missingInfoResponse(self, exception):
        response = {"status": 422, "message": "Missing Information"}
        return self.customResponse(response, exception)

    @classmethod
    def QuestionsNotFoundResponse(self, exception):
        response = {"status": 404, "message": "Not Found For This Owner"}
        return self.customResponse(response, exception)

    @classmethod
    def QuestionNotFoundResponse(self, exception):
        response = {"status": 404, "message": "Not Found For This Id"}
        return self.customResponse(response, exception)

    @classmethod
    def InternalServerErrorResponse(self, exception):
        response = {"status": 500, "message": "Internal Server Error"}
        return self.customResponse(response, exception)

    @classmethod
    def valid_data_question(self, data):
        if "question" not in data:
            return False
        if "topics" not in data:
            return False
        if "choices" not in data:
            return False
        if "answer" not in data:
            return False
        else:
            return True

    @classmethod
    def valid_data_feedback(self, data):
        if "question_id" not in data:
            return False
        if "description" not in data:
            return False
        else:
            return True

    @classmethod
    def logging(self, level, message, details):
        date = datetime.now()
        print(
            {
                "Level": level,
                "Message": message,
                "Timespan": date.isoformat(),
                "Details": details
            })
