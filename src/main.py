from SWIMMRS.src.TweetClassifier import Tokenizer, FeatureExtraction
from SWIMMRS.src.scraper.Datascraper import DataScraper
from SWIMMRS.src.scraper.OauthConnectionClient import OauthClient

userTweets_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=2597834149&count=20'

def main():
    oauth_obj = OauthClient()
    oauth_client = oauth_obj.getOauthClient()

    data_scraper = DataScraper(oauth_client)
    user_tweets = data_scraper.getUserTweets(userTweets_url)

    for a in user_tweets:
        print(a['text'])
        tokenList = Tokenizer.preprocess(a['text'])
        print(tokenList)
        # for t in tokenList:
        # print(t.encode('unicode-escape'))
        featureList = FeatureExtraction.getfeatureVector(tokenList)
        print(featureList)


if __name__ == '__main__':
    main()

