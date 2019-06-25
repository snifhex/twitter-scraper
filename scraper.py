import tweepy

consumer_key = ''
consumer_secret =''
access_token = ''
access_token_secret = ''

def authorization():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def get_tweets(query, api)
    public_tweets = api.home_timeline()
    query = 'mr robot'
    for tweet in tweepy.Cursor(api.search,q=query,count=100,result_type="recent",include_entities=True,lang='eng').items():
        print(tweet.text)
        
def main():
    pass

if __name__ == "__main__":
    main()


