import configparser
import requests
import os


class LastpassAPI:
    def __init__(self, API):
        config = configparser.ConfigParser()
        config.read(os.path.dirname(__file__) + "/config.cfg")
        self.url = config.get(API, "url")
        self.attribute = config.get(API, "response")
        self.header = {"content-type": "application/json"}

    def get(self):
        response = requests.get(self.url, headers=self.header)
        response = response.json()

        # Browse the response to fetch only the attributes you want
        self.attribute = self.attribute.split(".")
        depth = len(self.attribute)
        for i in range(depth):
            response = response[self.attribute[i]]

        print(response)
        return response
