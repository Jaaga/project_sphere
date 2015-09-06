#!/bin/python

import pickle

def main():
    data = pickle.load( open('alldata.pickle', 'rb') )

    def search(data, phrase):
        results = {}
        for stakeholder in data:
            for question in data[stakeholder]:
                for response in data[stakeholder][question]:
                    count = 0
                    if all(word in response.lower() for word in phrase.lower().split()):
                        count += 1
                        code = stakeholder+'-'+question+'-'+str(count)
                        results[code]=response
        return(results)

    while True:
        phrase = raw_input("Search phrase: ")
        if phrase is 'exit':
            break
        else:
            for key,value in search(data, phrase).iteritems():
                print key+': '+value



if __name__ == "__main__":
    main()
