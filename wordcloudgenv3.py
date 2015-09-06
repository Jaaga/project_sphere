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
    sphere_stopwords = { 'common': ['sam', 'mayu', 'mani']
    '1a':['live', 'born', 'year', 'years', 'yrs', 'since', 'bangalore'], \
    '1b':['live', 'born', 'year', 'yrs', 'moved', 'since', 'bangalore'], \
    '2a':['balance', 'time'], \
    '2b':['inspiration'], \
    '3':['lifestyle', ], \
    '4a':['bangalore', 'advantage', 'advantages'], \
    '4b':['bangalore', 'challenge', 'challenges'], \
    '4c':['work'], \
    '4d':['dependency', 'dependencies', 'external'], \
    '4e':['area', 'bangalore'], \
    '4f':['measures'], \
    '5b':['food', 'air'], \
    '6a':['end', 'user', 'enduser'], \
    '6b':['month', 'income', 'per', 'household'], \
    '6c':['interact', 'interaction','end', 'user', 'enduser'], \
    '6d':['design', 'end', 'user', 'enduser'], \
    '7a':['quality', 'control', 'challenge'], \
    '7b':['end', 'user', 'access', 'challenge'], \
    '7c':[], \
    '7d':[], \
    '8a':['tool', 'tools', 'resource', 'resources'], \
    '8b':['average', 'age', 'years', 'team', 'people'], \
    '8c':['fund', 'funding', 'funded', 'money'], \
    '8d':['tech', 'technology'], \
    '8e':['office', 'location', 'work', 'space'], \
    '9a':['skill', 'skills'], \
    '9b':['training'], \
    '10a':['active', 'internal', 'collaboration', 'collaborate'], \
    '10b':['active', 'external', 'collaboration', 'collaborate'], \
    '10c':['lead', 'leads', 'learning', 'collaboration', 'collaborate'], \
    '10d':['part', 'formal', 'collaboration', 'collaborate', 'platform'], \
    '10e':['culture', 'open', 'share', 'sharing', 'sector'], \
    '10f':['share', 'shares', 'shared'], \
    '11a':['partner', 'partners', 'partnership', 'partnerships'], \
    '11b':['criteria', 'partner', 'partners', 'partnership', 'partnerships'], \
    '11c':['partner', 'partners', 'partnership', 'partnerships', 'sector'], \
    '12a':['monitoring', 'evaluation', 'method', 'methods', 'impact'], \
    '12b':['goal', 'next', 'year', 'years'], \
    '12c':['impact', 'studies', 'data', 'shared'], \
    '13a':['entrepreneur'], \
    '13b':['start', 'starting', 'startup'], \
    '13c':['entrepreneur', 'entrepreneurs', 'interact', 'interaction'], \
    '13d':['entrepreneur', 'entrepreneurs', 'role', 'local', 'needs'], \
    '13e':['advantage', 'advantages', 'local', 'entrepreneur', 'entrepreneurs'], \
    '13f':['barrier', 'barriers', 'entry', 'local', 'entrepreneur', 'entrepreneurs'], \
    '13g':['challenge', 'challenges', 'local', 'entrepreneur', 'entrepreneurs'], \
    '13h':['entrepreneur', 'entrepreneurs', 'fail'], \
    '13i':['resource', 'resources', 'need', 'needed', 'strengthen', 'local', 'entrepreneur', 'entrepreneurs'], \
    '14a':['recommend', 'stakeholder', 'stakeholders'], \
    '14b':['map', 'visual'], \
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
                s = stopwords.union(set(sphere_stopwords[question]))
                # print s.difference(stopwords)
                data['wordclouds'][question] = WordCloud(stopwords=s, width=1600, height=800, background_color='white').generate(data[question])
            except:
                print question

    for stakeholder in data['stakeholders']:
        try:
            data['wordclouds'][stakeholder] = WordCloud(stopwords=stopwords, width=1600, height=800, background_color='white').generate(data[stakeholder]['alltext'])
        except:
            print stakeholder

    pickle.dump(data, open('alldata_v3.pickle', 'wb'))

    # Display the generated image:
    # the matplotlib way:
    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud)
    # plt.axis("off")

if __name__ == "__main__":
    main()
