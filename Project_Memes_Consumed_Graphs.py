## Project_Memes_Consumed_Graphs
## January 11, 2019
## Verious graphs demonstrating meme consumption from Facebook, Instagram,
## and Tumblr per minute.
## Sourses:
## (Understanding how to make scatter plots)
## https://medium.com/python-pandemonium/data-visualization-in-python-scatter-plots-in-matplotlib-da90ac4c99f9

import matplotlib.pyplot as plt

minutesFacebook = sorted([0, 0, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5, 10, 10, 15, 30, 30, 30, 60, 60, 90, 120, 15])
memesFacebook = sorted([0, 0, 0, 0, 0, 0, 2, 25, 3, 3, 4, 5, 10, 10, 10, 10, 10, 20, 3.5, 50, 50, 60, 60])

minutesInstagram = sorted([0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 15, 15, 15, 30, 30, 30, 45, 45, 50, 60, 60, 10, 0])
memesInstagram = sorted([0, 0, 0, 0, 0, 0, 0, 1, 2.5, 3, 5, 5, 5, 10, 10, 20, 30, 50, 60, 90, 0, 0, 10])

minutesTumblr = sorted([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 0, 0])
memesTumblr = sorted([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 100, 0, 0, 0, 0])

#print((minutesFacebook), (memesFacebook))
#print((minutesInstagram), (memesInstagram))
#print((minutesTumblr), (memesTumblr))

plt.scatter(minutesFacebook, memesFacebook, color = 'r')
plt.scatter(minutesInstagram, memesInstagram, color = 'g')
plt.scatter(minutesTumblr, memesTumblr, color = 'b')

plt.ylabel("Number of Minutes")
plt.xlabel("Number of Memes")
plt.title("Number of Memes consumed per Minute", fontdict = None, loc = 'center', pad = None)
plt.show()


