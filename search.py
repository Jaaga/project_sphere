#!/bin/python

import pickle

def main():
    data = pickle.load( open('alldata.pickle', 'rb') )

    def search(data, phrase):
        results = []
        for stakeholder in data:
            for question in data[stakeholder]:
                for response in data[stakeholder][question]:
                    if all(word in response.lower() for word in phrase.lower().split()):
                        results.append(stakeholder + ' ' + question +': ' + response + '\n')
        return(results)

    while True:
        phrase = raw_input("Search phrase: ")
        if phrase is 'exit':
            break
        else:
            for result in search(data, phrase):
                print result



if __name__ == "__main__":
    main()
