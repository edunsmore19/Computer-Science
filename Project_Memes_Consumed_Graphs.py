## Project_Memes_Consumed_Graphs
## January 11, 2019
## Verious graphs demonstrating meme consumption from Facebook, Instagram,
## and Tumblr per minute.
## Sourses:
## (Understanding how to make scatter plots)
## https://medium.com/python-pandemonium/data-visualization-in-python-scatter-plots-in-matplotlib-da90ac4c99f9

import matplotlib.pyplot as plt
import random
import numpy as np

minutesFacebook = sorted([0, 0, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5, 10, 10, 15, 30, 30, 30, 60, 60, 90, 120, 15, 30, 30, 0])
memesFacebook = sorted([2, 25, 3, 3, 4, 5, 10, 10, 10, 10, 10, 20, 3.5, 50, 50, 60, 60, 8, 30])

minutesInstagram = sorted([0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 15, 15, 15, 30, 30, 30, 45, 45, 50, 60, 60, 10, 0, 15, 0, 0])
memesInstagram = sorted([1, 2.5, 3, 5, 5, 5, 10, 10, 20, 30, 50, 60, 90, 10, 1])

minutesTumblr = sorted([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0, 0])
memesTumblr = sorted([0.5, 100])

bins = sorted([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
bins2 = sorted([0, 5, 10, 15, 20, 30, 40, 50, 60, 70])

## Display the number of people who use each platform & how many minutes they spend on each
## Utilizing a histogram in order to give an impression of frequency by sorting engagement
## into 'bins' which stack to make a graph

'''
plt.hist(minutesFacebook, bins, histtype = "bar", rwidth = 0.4, color = (0, 0.9, 0.5, 0.6), label = "Facebook")
plt.hist(minutesInstagram, bins, histtype = "bar", rwidth = 0.4, color = (0.4, 0, 0.9, 0.6), label = "Instagram")
plt.hist(minutesTumblr, bins, histtype = "bar", rwidth = 0.4, color = (0.1, 0.9, 0, 0.6), label = "Tumblr")
plt.legend()
plt.ylabel("Frequency")
plt.xlabel("Number of Minutes")
plt.title("Frequency of Minutes Spent on Visual Social Media Platforms")
'''

## Display the user-reported average number of memes encountered per hour of usage 
plt.hist(memesFacebook, bins2, histtype = "bar", rwidth = 0.4, color = (0, 0.9, 0.5, 0.6), label = "Facebook")
plt.hist(memesInstagram, bins2, histtype = "bar", rwidth = 0.4, color = (0.4, 0, 0.9, 0.6), label = "Instagram")
plt.hist(memesTumblr, bins2, histtype = "bar", rwidth = 0.4, color = (0.1, 0.9, 0, 0.6), label = "Tumblr")
plt.legend()
plt.ylabel("Average Number")
plt.xlabel("Number of Memes")
plt.title("Average Number of Memes Encountered in an Hour")

#plt.plot(minutesFacebook, memesFacebook, label = "Facebook minutes", color = 'b')
#plt.legend()

#plt.scatter(minutesFacebook, memesFacebook, label = "Facebook", color = 'r')
#plt.scatter(minutesInstagram, memesInstagram, label = "Instagram", color = 'g')
#plt.scatter(minutesTumblr, memesTumblr, label = "Tumblr", color = 'b')

#plt.ylabel("Number of Minutes")
#plt.xlabel("Number of Memes")
#plt.title("Number of Memes consumed per Minute", fontdict = None, loc = 'center', pad = None)
#plt.legend()
plt.show()


