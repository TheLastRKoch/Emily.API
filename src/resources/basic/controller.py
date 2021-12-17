from flask_restful import Resource


class StatusController(Resource):
    url = "/status"

    def get(self):
        return {"msg": "Status OK"}


class RootController(Resource):
    url = "/"

    def get(self):
        return {
            "msg": "Welcome to the dafnix API"
        }


def add_basic_resource_table(api):
    api.add_resource(StatusController, StatusController.url)
    api.add_resource(RootController, RootController.url)
