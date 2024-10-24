
"""
Calculate the sentiment score of the searched contexts from twitter.

Author: Anh Hoang, David Yuxuan Zhang

Time spent: 2 hours

"""
from csc121 import twitter

def search_tweet(search):
    """
    Parameters:
    search - The word that is going to be searched on twitter
        
    Returns:
    A list of context of tweets that contains the searched word
        
    Pseudocode:
    This function search the recent 100 tweets that are related to the
    searched word. Then by using for-loop, the function extract only the
    context of the tweets, and turn them into all lower-cases.
    """
    
    tweet_list = []
    tweets = twitter.get_tweets(search)
    #tweets = twitter.get_cached_tweets()
    tweet_status = tweets['statuses']
    
    
    for i in range(len(tweet_status)):
        tweet = tweet_status[i].get('text',0)
        tweet = tweet.lower()
        tweet_list.append(tweet)
    return tweet_list
    

def analyze_tweets(search):
    """
    Parameters:
    search - The word that is going to be searched on twitter
    
    Returns:
    If no error is generated, the function returns the sentiment score of the
    searched tweets. If there are errors like FileNotFoundError or IOError
    appeared, the function prints "Error" to the screen, and returns 0
    
    Pseudocode:
    We first created a dictionary with each word as key and the score of the
    word as value. Then we scan through the context of the tweets to see if any
    words in the tweets are in our dictionary. Then we count the total score of
    the tweets, and we calculate the sentiment score by calculating the average
    score of the tweets.
    """
    
    tweet_list = search_tweet(search)
    word_valence = {}
    try:
        with open('AFINN-111.txt', 'r') as myfile:
            for line in myfile:
                words = line.split()
                word_valence[words[0]] = int(words[1])
        count = 0
        score_lst = []
        for tweet in tweet_list: #Iterate through each lines of tweets
            word_tweet = tweet.split() #Create a list with seperate words
            for word in word_tweet: #Iterate through each word in each tweet
                if word in word_valence: #Check if the word has a valence score
                    count += word_valence[word] #Count the total score of
                                                 #each tweet
            score_lst.append(count) #Store each score into a list
            count = 0
        sentiment_score = sum(score_lst)/len(score_lst) # Calculate the average
        return sentiment_score
    except:
        print("Error")
        return 0
        

        
def main():
    """
    A wrapper function that calls the functions above
    """
    
    #print(analyze_tweets('jhdsfgieqjrhgp8hfasoifhw'))
    
    ## More code here

'''
Do NOT change the code below
'''
    
if __name__ == "__main__":
    main() 