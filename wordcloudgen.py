#!/bin/python

import csv, re, string
import pickle
from wordcloud import WordCloud, STOPWORDS

def main():

    data = {}
    data['questions'] = []
    data['stakeholders'] = []
    data['wordclouds'] = {}

    stopwords = STOPWORDS.copy()

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
                    response = shortword.sub('', row[key].lower().translate(None,string.punctuation))
                    data[stakeholder][question] = response
                    data[stakeholder]['alltext'] += response
                    data[stakeholder]['alltext'] += ' '
                    data[question] += response
                    data[question] += ' '

    #Generate word clouds:
    for question in sorted(data['questions']):
        if question is not '5a':
        #Number of words per question
        # print question, ':', len(data[question].split())
            try:
                data['wordclouds'][question] = WordCloud(stopwords=stopwords).generate(data[question])
            except:
                print question

    for stakeholder in data['stakeholders']:
        try:
            data['wordclouds'][stakeholder] = WordCloud(stopwords=stopwords).generate(data[stakeholder]['alltext'])
        except:
            print stakeholder

    pickle.dump(data, open('alldata.pickle', 'wb'))

    # Display the generated image:
    # the matplotlib way:
    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud)
    # plt.axis("off")

if __name__ == "__main__":
    main()
