## Project_Memes_Consumed_Graphs
## January 11, 2019
## Verious graphs demonstrating meme consumption from Facebook, Instagram,
## and Tumblr per minute.
## Sourses:
## (Understanding how to make scatter plots)
## https://medium.com/python-pandemonium/data-visualization-in-python-scatter-plots-in-matplotlib-da90ac4c99f9
## (Understanding how to make histograms)
## https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
## Honor Code:
## I have neither given nor recieved any unauthorized aid.

import matplotlib.pyplot as plt
import random
import numpy as np

minutesFacebook = sorted([0, 0, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5, 10, 10, 15, 30, 30, 30, 60, 60, 90, 120, 15, 30, 30, 0])
memesFacebook = sorted([2, 25, 3, 3, 4, 5, 10, 10, 10, 10, 10, 20, 3.5, 50, 50, 60, 60, 8, 30])
## Adjusted point-to-point data for scatter plot
minutesFacebookAdjusted = [0, 0, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5, 10, 10, 15, 30, 30, 30, 60, 60, 90, 120, 15, 30, 30, 0]
memesFacebookAdjusted = [0, 0, 0, 0, 0, 0, 2, 25, 3, 3, 4, 5, 10, 10, 10, 10, 10, 20, 3.5, 50, 50, 60, 60, 8, 30, 0]

minutesInstagram = sorted([0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 15, 15, 15, 30, 30, 30, 45, 45, 50, 60, 60, 10, 0, 15, 0, 0])
memesInstagram = sorted([1, 2.5, 3, 5, 5, 5, 10, 10, 20, 30, 50, 60, 90, 10, 1])
## Adjusted ptp data
minutesInstagramAdjusted = ([0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 15, 15, 15, 30, 30, 30, 45, 45, 50, 60, 60, 10, 0, 15, 0, 0])
memesInstagramAdjusted = ([0, 0, 0, 0, 0, 0, 0, 0, 1, 2.5, 3, 5, 5, 5, 10, 10, 20, 30, 50, 60, 90, 10, 0, 1, 0, 0])

minutesTumblr = sorted([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0, 0])
memesTumblr = sorted([0.5, 100])
## Adjusts ptp data
minutesTumblrAdjusted = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0, 0])
memesTumblrAdjusted = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 100, 0, 0, 0, 0, 0])

bins = sorted([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
bins2 = sorted([0, 5, 10, 15, 20, 30, 40, 50, 60, 70])

## Display the number of people who use each platform & how many minutes they spend on each
## Utilizing a histogram in order to give an impression of frequency by sorting engagement
## into 'bins' which stack to make a graph


plt.hist(minutesFacebook, bins, histtype = "bar", rwidth = 0.4, color = (0, 0.4, 0.8, 0.6), label = "Facebook")
plt.hist(minutesInstagram, bins, histtype = "bar", rwidth = 0.4, color = (0.4, 0, 0.9, 0.6), label = "Instagram")
plt.hist(minutesTumblr, bins, histtype = "bar", rwidth = 0.4, color = (0.1, 0.9, 0, 0.6), label = "Tumblr")
plt.legend()
plt.ylabel("Frequency")
plt.xlabel("Number of Minutes")
plt.title("Frequency of Minutes Spent on Visual Social Media Platforms")
plt.show()

## Display the user-reported average number of memes encountered per user-reported average of usage 


plt.hist(memesFacebook, bins2, histtype = "bar", rwidth = 0.4, color = (0, 0.4, 0.8, 0.6), label = "Facebook")
plt.hist(memesInstagram, bins2, histtype = "bar", rwidth = 0.4, color = (0.4, 0, 0.9, 0.6), label = "Instagram")
plt.hist(memesTumblr, bins2, histtype = "bar", rwidth = 0.4, color = (0.1, 0.9, 0, 0.6), label = "Tumblr")
plt.legend()
plt.ylabel("Average Number")
plt.xlabel("Number of Memes")
plt.title("Average Number of Memes Encountered in an Hour")
plt.show()

## Display the individual data points
plt.scatter(minutesFacebookAdjusted, memesFacebookAdjusted, color = (0, 0.4, 0.8, 0.6), label = "Facebook")
plt.scatter(minutesInstagramAdjusted, memesInstagramAdjusted, color = (0.4, 0, 0.9, 0.6), label = "Instagram")
plt.scatter(minutesTumblrAdjusted, memesTumblrAdjusted, color = (0.1, 0.9, 0, 0.6), label = "Tumblr")
plt.legend()
plt.ylabel("Memes Consumed")
plt.xlabel("Minutes Spent Online")
plt.title("Data Sets")
plt.show()


