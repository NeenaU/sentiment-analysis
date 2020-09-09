import re
import tweepy 
from tweepy.auth import OAuthHandler 
from textblob import TextBlob
  
class SentimentAnalysis(object): 

    #Class constructor
    def __init__(self): 
        
        #Keys and tokens from Twitter Developer portal
        consumerKey = 'LkdUg86X0KIVLw9cmvq1CgdZy'
        consumerSecret = '66jGHLbMmlPyNdOLC4utsXOw8D7F5Y4m4ge98QkSNAVLyqEMj7'
        accessToken = '456004005-6IXIKd3E3ntjSjT57INTYqmb5hjThonirsxFBvmz'
        accessTokenSecret = 'EclZSGVkxuw9NgKtFiJDu2Jo3zlWdWxVxklrn1h4Q4lgM'
  
        #Attempt authentication 
        try: 
            self.authHandler = OAuthHandler(consumerKey, consumerSecret) 
            self.authHandler.set_access_token(accessToken, accessTokenSecret) 

            #Create tweepy API object that will fetch tweets
            self.api = tweepy.API(self.authHandler)
            print("Authentication worked")

        except: 
            print("Authentication Failed")


    def getTweets(self, query, tweetNumber = 200):

        #List to store the text of each tweet
        content = []
        
        try:
            #Fetch the tweets using the query given
            fetchedTweets = self.api.search(q=query, count=tweetNumber)

            #Loop through tweets and store their text in the list
            for t in fetchedTweets:

                #Append tweet to list, ensuring it is only appended once
                if t.retweet_count > 0:
                    if t.text not in content:
                        content.append(t.text)
                else:
                    content.append(t.text)
                    
            return content
        
        except tweepy.TweepError as e:
            print("Error" + str(e))

    #Function to remove links and special characters from tweets
    #Taken from https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
    def cleanTweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 

    def getSentiment(self, content):

        #List to store the sentiment of each tweet
        sentiments = []

        for tweet in content:
            blob = TextBlob(self.cleanTweet(tweet))

            if blob.sentiment.polarity > 0:
                sentiments.append('positive')
            elif blob.sentiment.polarity == 0:
                sentiments.append('neutral')
            else:
                sentiments.append('negative')
            
        return sentiments 

def main():
    api = SentimentAnalysis()

    #Get tweets from twitter and find out their sentiment
    tweetContent = api.getTweets(query = 'Donald Trump')
    print(len(tweetContent), "tweets gathered")
    tweetSentiment = api.getSentiment(tweetContent)

    #List to store pairs of tweets and their sentiment
    tweets = []

    for i in range(len(tweetContent)-1):

        #Dictionary to store the text and sentiment of each tweet
        parameters = {}

        parameters['text'] = tweetContent[i]
        parameters['sentiment'] = tweetSentiment[i]

        tweets.append(parameters)

    #Select positive tweets and find percentage
    posTweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    posPercentage = len(posTweets)/len(tweets) * 100
    print("Positive tweets: ", round(posPercentage,2), "%")

    #Select negative tweets and find percentage
    negTweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    negPercentage = len(negTweets)/len(tweets) * 100
    print("Negative tweets: ", round(negPercentage,2), "%")

    #Find percentage of neutral tweets
    neutralPercentage = (len(tweets) - (len(negTweets)+len(posTweets)))/len(tweets) * 100
    print("Neutral tweets: ", round(neutralPercentage,2), "%")
            
#Call the main function
if __name__ == "__main__": 
    main()

    
