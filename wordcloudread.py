#!/bin/python

# import csv, re, string
import pickle
from wordcloud import WordCloud

def main():

    data = pickle.load( open('alldata_v3.pickle', 'rb') )

    for key in data['wordclouds']:
        try:
            wc = data['wordclouds'][key]
            wc.to_file('clouds/'+key+'.png')
        except:
            print key



    # Display the generated image:
    # the matplotlib way:
    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud)
    # plt.axis("off")

if __name__ == "__main__":
    main()
