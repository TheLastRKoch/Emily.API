import requests
import json
from os import environ as env
from dotenv import load_dotenv


class GithubGistService():
    def __init__(self, githubGist_url, githubAPI_token):
        self.url = githubGist_url
        self.headers = {
            'Authorization': "Token " + githubAPI_token,
            'Content-Type': 'application/json'
        }

    def __get_request(self):
        response = requests.request(
            "GET", url=self.url, headers=self.headers)
        return json.loads(response.text)

    def __patch_request(self, body):
        response = requests.request(
            "PATCH", url=self.url, headers=self.headers, data=body)
        return json.loads(response.text)

    def get_all_files(self):
        response = self.__get_request()
        return response["files"]

    def get_url(self):
        response = self.__get_request()
        return response["files"]["PlayerURL"]["content"]

    def update_url(self, url):
        body = json.dumps({"files": {"PlayerURL": {"content": url}}})
        self.__patch_request(body)


if __name__ == "__main__":
    load_dotenv()
    ggs = GithubGistService(env["GIST_URL"], env["GITHUB_API_KEY"])
    print(ggs.get_url())
