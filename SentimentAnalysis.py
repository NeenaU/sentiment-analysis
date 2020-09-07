import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
  
class SentimentAnalysis(object): 

    #Class constructor
    def __init__(self): 
        
        #Keys and tokens from Twitter Developer portal
        consumer_key = 'LkdUg86X0KIVLw9cmvq1CgdZy'
        consumer_secret = '66jGHLbMmlPyNdOLC4utsXOw8D7F5Y4m4ge98QkSNAVLyqEMj7'
        access_token = '456004005-4Cqe4mKXZSL1nFWl0e582lIjpK6j5iszH28AfS1c'
        access_token_secret = 'iEMDvCyhsL0y5iZ2wgdJ1Y6Yj6StHDcN5pzzw8dYNm9Ze'
  
        #Attempt authentication 
        try: 
            self.authHandler = OAuthHandler(consumer_key, consumer_secret) 
            self.authHandler.set_access_token(access_token, access_token_secret) 

            #Create tweepy API object that will fetch tweets
            self.api = tweepy.API(self.auth)

            #Test authentication
            api.verify_creditials()
            print("Authentication worked")

        except: 
            print("Authentication Failed")


    def getTweets():
        #Number of tweets to be extracted
        self.tweetNumber = 200

        tweets = api.user_timeline

    def main():
        api = SentimentAnalysis()
        tweets = api.getTweets()


#Call the main function
if __name__ == "__main__": 
    main()

    
