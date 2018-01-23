import os

import oauth2 as oauth


class OauthClient:

    def __init__(self):
        self.client = None
        path = os.path.join("../src/scraper/Credentials.txt")
        with open(path, 'r') as cred:
            credentials = cred.readlines()
        self.CONSUMER_KEY = credentials[0].strip()
        self.CONSUMER_SECRET = credentials[1].strip()
        self.ACCESS_KEY = credentials[2].strip()
        self.ACCESS_SECRET = credentials[3].strip()

    def getOauthClient(self):
        consumer = oauth.Consumer(key=self.CONSUMER_KEY, secret=self.CONSUMER_SECRET)
        access_token = oauth.Token(key=self.ACCESS_KEY, secret=self.ACCESS_SECRET)
        try:
            self.client = oauth.Client(consumer, access_token)
        except Exception as e:
            return e
        return self.client

    def removeClient(self):
        raise NotImplementedError