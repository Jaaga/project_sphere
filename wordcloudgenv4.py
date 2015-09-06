#!/bin/python

import csv, re, string
import pickle
from wordcloud import WordCloud, STOPWORDS

def main():

    data = pickle.load( open('alldata.pickle', 'rb') )
    data['wordclouds'] = {}

    stopwords = STOPWORDS.copy()
    sphere_stopwords = { 'common': ['sam', 'mayu', 'mani'],
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

    questions = []
    text = {}

    for stakeholder in data:
        text[stakeholder] = ''
        for question in data[stakeholder]:
            if question not in questions:
                questions.append(question)
                text[question] = ''
            response = shortword.sub('', ' '.join(data[stakeholder][question]).lower().translate(None,string.punctuation))
            text[stakeholder] += response + ' '
            text[question] += response + ' '

    #Generate word clouds:
    for question in sorted(questions):
        if question is not '5a':
            try:
                s = stopwords.union(set(sphere_stopwords[question]+sphere_stopwords['common']))
                wordcloud = WordCloud(stopwords=s, width=1600, height=800, background_color='white').generate(text[question])
                wordcloud.to_file('clouds/'+question+'-'+str(len(text[question].split()))+'words.png')
            except:
                print question

    for stakeholder in data:
        try:
            s = stopwords.union(set(sphere_stopwords['common']))
            wordcloud = WordCloud(stopwords=s, width=1600, height=800, background_color='white').generate(text[stakeholder])
            wordcloud.to_file('clouds/'+stakeholder+'-'+str(len(text[stakeholder].split()))+'words.png')
        except:
            print stakeholder

    # pickle.dump(data, open('alldata_v3.pickle', 'wb'))

if __name__ == "__main__":
    main()
