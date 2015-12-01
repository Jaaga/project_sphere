#!/bin/python

import csv, re, string
import json

#Store metadata within a sub-dictionary for easier parsing when displaying
#Note we are not storing Confidentiality (as all of these are open) and
#Shortname - this is instead used as the key within the parent dictionary
metadata_tags = ['Organisation', 'URL', 'Name(s) of Interviewee(s)', 'Sector', 'Type', 'Interview Number', 'Date and Time',
'Orator', 'Documentor', 'Venue', 'Duration', 'Interview Code']

#Questions list to store responses within a sub-dictionary for easier parsing when displaying
#Note that this question order is not retained in the dictonary 'data' as Python dictionaries are unordered. We reuse this
#order when displaying the information.
qorder = ['1a', '1b', '2a', '2b', '3', '4a', '4b', '4c', '4d', '4e', '4f', '5a', '5b', '6a', '6b', '6c', '6d', '7a',
'7b', '7c', '7d', '8a', '8b', '8c', '8d', '8e', '9a', '9b', '10a', '10b', '10c', '10d', '10e', '10f', '11a', '11b', '11c',
'12a', '12b', '12c', '13a', '13b', '13c', '13d', '13e', '13f', '13g', '13h', '13i', '14a', '14b']

def main():
    #Initialise the main dictionary
    data = {}
    questions = {}

    with open('interviews.csv') as csvfile:
        #Read the csv file as a list of dictionaries
        reader = csv.DictReader(csvfile)
        for row in reader:
            #Use the shortname as item key for easier lookups
            #We will also use the shortname when displaying lists of stakeholders for cleaner displays
            stakeholder = row['Shortname']
            #Initialise the parent stakeholder dictionary and the sub-dictionaries for metadata and responses
            data[stakeholder] = {}
            data[stakeholder]['metadata'] = {}
            data[stakeholder]['responses'] = {}
            for key in row:
                #Strip all the backslashes '\' from the text. Two '\\' because Python escapes them when reading in
                response = filter(None, row[key].strip().split('\\'))
                #Strip all whitespaces at end of line
                response = map(lambda s: s.strip(), response)
                if len(response) is not 0:
                    if key in metadata_tags:
                        data[stakeholder]['metadata'][key] = response
                    if key in qorder:
                        data[stakeholder]['responses'][key] = response

    with open('questions.tsv') as tsvfile:
        #Read the csv file as a list of dictionaries
        reader = csv.DictReader(tsvfile, delimiter='\t')
        for row in reader:
            questions[row['#']]=row['Question']

    #Write the dictionary to a json file. Allows quicker reads and is safer than using pickle.
    json.dump(data, open('interviews.json', 'wb'))
    json.dump(questions, open('questions.json', 'wb'))

#Execute the main loop
if __name__ == "__main__":
    main()
