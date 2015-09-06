#!/bin/python

import csv, re, string
import pickle

def main():

    data = {}
    # data['questions'] = []
    # data['stakeholders'] = []


    with open('alldata.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stakeholder = row['Code']
            # data['stakeholders'].append(stakeholder)
            data[stakeholder] = {}
            for key in row:
                if key != 'Code':
                    question = key
                    # if question not in data['questions']:
                        # data['questions'].append(question)
                    response = filter(None, row[key].strip().split('\\'))
                    response = map(lambda s: s.strip(), response)
                    data[stakeholder][question] = response

    pickle.dump(data, open('alldata.pickle', 'wb'))

if __name__ == "__main__":
    main()
