import tweepy

consumer_key = ''
consumer_secret =''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
query = 'mr robot'
for tweet in tweepy.Cursor(api.search,q=query,count=100,result_type="recent",include_entities=True,lang='eng').items():
    print(tweet.text)




