from src.services import GithubGistService
from flask_restful import Resource
from requests.api import request
from os import environ as env
from flask import request
from src.utils import utils


class PlayerController(Resource):
    url = "/player"

    # Get List
    def get(self):
        ggs = GithubGistService(env["GIST_URL"], env["GITHUB_API_KEY"])
        url = ggs.get_url()

        return utils.generateResponse(
            {
                "body": f"Current URL {url}",
                "status_code": 200
            })

    # Create
    def patch(self):
        url = request.json["url"]
        ggs = GithubGistService(env["GIST_URL"], env["GITHUB_API_KEY"])
        ggs.update_url(url)
        return utils.generateResponse(
            {
                "body": "The url has been updated successfully",
                "status_code": 200
            })


def add_player_resource_table(api):
    api.add_resource(PlayerController, PlayerController.url)
