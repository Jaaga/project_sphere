#!/bin/python

import csv, re, string
import pickle
from wordcloud import WordCloud, STOPWORDS
from stemming.porter2 import stem

def main():

    data = {}
    data['questions'] = []
    data['stakeholders'] = []
    data['wordclouds'] = {}


    stopwords = STOPWORDS.copy()
    sphere_stopwords = {'1a':['live', 'born', 'year', 'yrs', 'since'], \
    '1b':['live', 'born', 'year', 'yrs', 'moved', 'since'], \
    '2a':['time'], \
    '2b':[], \
    '3':[], \
    '4a':['bangalore', 'advantage', 'advantages'], \
    '4b':['bangalore', 'challenge', 'challenges'], \
    '4c':['work'], \
    '4d':['dependency', 'dependencies', 'external'], \
    '4e':['area', 'bangalore'], \
    '4f':[], \
    '5b':['food', 'air'], \
    '6a':['end', 'user', 'enduser'], \
    '6b':['month', 'income', 'per', 'household'], \
    '6c':['interact', 'interaction','end', 'user', 'enduser'], \
    '6d':['design', 'end', 'user', 'enduser'], \
    '7a':['quality', 'control', 'challenge'], \
    '7b':['end', 'user', 'access', 'challenge'], \
    '7c':[], \
    '7d':[], \
    '8a':['tool', 'resource', 'resource'], \
    '8b':['average', 'age', 'team'], \
    '8c':[], \
    '8d':[], \
    '8e':[], \
    '9a':[], \
    '9b':[], \
    '10a':[], \
    '10b':[], \
    '10c':[], \
    '10d':[], \
    '10e':[], \
    '10f':[], \
    '11a':[], \
    '11b':[], \
    '11c':[], \
    '12a':[], \
    '12b':[], \
    '12c':[], \
    '13a':[], \
    '13b':[], \
    '13c':[], \
    '13d':[], \
    '13e':[], \
    '13f':[], \
    '13g':[], \
    '13h':[], \
    '13i':[], \
    '14a':[], \
    '14b':[], \
    }

    #Filter out standalone words 2 letters or shorter
    shortword = re.compile(r'\W*\b\w{1,2}\b')

    with open('alldata.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stakeholder = row['Code']
            data['stakeholders'].append(stakeholder)
            data[stakeholder] = {}
            data[stakeholder]['alltext'] = ''
            for key in row:
                if key != 'Code':
                    question = key
                    if question not in data['questions']:
                        data['questions'].append(question)
                        data[question] = ''
                    raw_response = shortword.sub('', row[key].lower().translate(None,string.punctuation))
                    stemmed_response = ' '.join([stem(word) for word in raw_response.split()])
                    data[stakeholder][question] = row[key]
                    data[stakeholder]['alltext'] += stemmed_response
                    data[stakeholder]['alltext'] += ' '
                    data[question] += stemmed_response
                    data[question] += ' '

    #Generate word clouds:
    for question in sorted(data['questions']):
        if question is not '5a':
        #Number of words per question
        # print question, ':', len(data[question].split())
            try:
                s = stopwords.union(set(sphere_stopwords[question]))
                data['wordclouds'][question] = WordCloud(stopwords=s).generate(data[question])
            except:
                print question

    for stakeholder in data['stakeholders']:
        try:
            data['wordclouds'][stakeholder] = WordCloud(stopwords=stopwords).generate(data[stakeholder]['alltext'])
        except:
            print stakeholder

    pickle.dump(data, open('alldata_v2.pickle', 'wb'))

    # Display the generated image:
    # the matplotlib way:
    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud)
    # plt.axis("off")

if __name__ == "__main__":
    main()
