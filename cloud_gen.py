import tweepy
import re
import os
import time
import matplotlib.pyplot as plts
from os import path
from wordcloud import WordCloud

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

# This loop take into account any errors that tweepy with throw and sleep until the tweets are replenishable
while True:
    try:
        # Grabbing all tweets based on the query search and the language
        for tweet in tweepy.Cursor(api.search, q = userIn, lang = "en").items():
            # Write to a text
            textFile.write(tweet.text)
            print(tweet.text)
            print("\n")
            # Only taking in 2000 tweets for anaylising with word map
            x += 1
            if x == 2000:
                break
    # If tweepy throws the 429 error(which it usually does after seraching), this excpet will sleep the program until it's ready to go
    except tweepy.TweepError:
        time.sleep(.1)
        print("One Moment Please, Hibernating")
        y += 1
        if y == 10:
            break
    # This will stop the loop if this condition is meet
    except StopIteration:
        break

# Closing the text file
textFile.close()import matplotlib.pyplot as plt

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
