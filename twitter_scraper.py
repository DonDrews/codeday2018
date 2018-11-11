import tweepy
import csv

# Store OAuth authentication credentials in relevant variables
consumer_key = 'nj3wTygQk1eJCAflALgUCCKvI'
consumer_secret = 'JyTxJDYQ03wG1W3dVqj1dXrHsg4Azvv8s6Qb6PT6B64HxW894m'
access_token = '1053752149518077953-C6ZHXrDoUIKD9awPN4kvDy0pS2TyVM'
acces_secret = 'MqNGIb1RrgvcAhLQByJxPy4rYb4RK0VnNXthr7zOB3f97'

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_secret)
api = tweepy.API(auth)

# Opening CSV file
textFile = open('test.txt', 'w')

# Initilizing the var for counting the grabbed tweets
x = 0

# Taking user input
userIn = str(input("What would you like to stream on twitter?\n"))

# Grabbing all tweets based on the query search and the language
for tweet in tweepy.Cursor(api.search, q = userIn, lang = "en").items():
    # Write a row to the CSV file
    textFile.write(tweet.text)
    print(tweet.text)
    print("\n")

    # Only taking in 2000 tweets for anaylising with word map
    x += 1
    if x == 2000:
        break

# Closing the text file
textFile.close()
