import json
#userProfile_url = 'https://api.twitter.com/1.1/users/show.json?user_id=2597834149'
#userTweets_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=2597834149&count=20'

class DataScraper:

    def __init__(self, client):
        self.response = None
        self.client = client

    # Get User Profile Details
    def getUserProfileData(self, userProfile_url):
        try:
            response_code, response_content = self.client.request(userProfile_url)
            if response_code['status'] == str(200):
                userProfileInfo = json.loads(response_content)
                return userProfileInfo
            else:
                return response_code['status']
        except Exception as e:
            return e

    # Get User Tweets
    def getUserTweets(self, userTweets_url):
        try:
            response_code, response_content = self.client.request(userTweets_url)
            userTweetsInfo = json.loads(response_content)
            return userTweetsInfo
        except Exception as e:
            return e
