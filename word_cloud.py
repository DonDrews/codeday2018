#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the Bee Movie using default arguments.
"""

import os

from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'mapme.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(width=1000, height=1000, collocations=False).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# lower max_font_size
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
