import tweepy
import re
import os
import time
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Store OAuth authentication credentials in relevant variables
consumer_key = 'nj3wTygQk1eJCAflALgUCCKvI'
consumer_secret = 'JyTxJDYQ03wG1W3dVqj1dXrHsg4Azvv8s6Qb6PT6B64HxW894m'
access_token = '1053752149518077953-C6ZHXrDoUIKD9awPN4kvDy0pS2TyVM'
acces_secret = 'MqNGIb1RrgvcAhLQByJxPy4rYb4RK0VnNXthr7zOB3f97'

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_secret)
api = tweepy.API(auth)

# Opening TXT file
textFile = open('test.txt', 'w')

# Initilizing the var for counting the grabbed tweets
x = 0

# Initilizing the var making sure the hibernating doesn't get stuck
y = 0

# Taking user input
userIn = str(input("What would you like to stream on twitter?\n"))

# setting up logic for the stream listner
class StreamListener(tweepy.StreamListener):
    # Init local variable for counting
    z = 0

    # Streaming tweets and keeping track
    def on_status(self, status):
        print(status.text)
        textFile.write(status.text)
        self.z += 1
        if self.z > 1000:
            print("\n\n")
            print("--------------------------------------")
            print("One moment please, drawing word cloud!")
            print("--------------------------------------")
            print("\n\n")
            return False
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def on_error(self, status_code):
        if status_code == 429:
            return False

# Listening for tweets
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=[userIn], languages=["en"])


# Closing the text file
textFile.close()

# Opening new text files
file = open('test.txt', 'r')
bannedFile = open('joshs_thot_police.txt')

# Setting up a blank list
lines = []

# Setting up a blank list
banned = []

for line in bannedFile:
    banned.append(line)

# Replace all special chars with spaces
for line in file:
    line = re.sub('[^A-Za-z0-9@]', ' ', line)
    lines.append(line)

words = []
for l in lines:
    wordList = l.split(' ')
    for ws in wordList:
        if ws != "" and not '@' in ws:
            found = False
            for b in banned:
                if ws.lower().rstrip() == b.lower().rstrip():
                    found = True
            if not found:
                words.append(ws.lower())

# Setting up file out put to be read
output = open('mapme.txt', 'w')

# Sending banned words to the list
for w in words:
    output.write(w)
    output.write('\n')

# Closing file output
output.close()

# Get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'mapme.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(width=1000, height=1000, collocations=False).generate(text)

# Display the generated image:
# The matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Lower max_font_size
'''
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
'''

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
