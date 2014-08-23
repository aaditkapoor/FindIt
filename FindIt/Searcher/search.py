__author__ = 'Aadit'
__version__ = '1.0.0'
import sys

"""
    Name: search.py
    Purpose: Searching functions
"""


def start_searching(word, data):
    '''
        start_searching(word,data) -> int
        Searches a given word (a whole word, or just a letter)

        Searches a single word and highlights it
    '''
    count = 0
    for i in range(len(data)):
        if word == data[i]:
            print (data[i],file=sys.stderr)
            count += 1
            continue
        else:
            index = data[i].find(word)
            if index == -1:
                continue
            else:
                count += 1
                word_to = data[i][index]
                ind = data[i].find(word_to)
                ind = data[i][ind]
                for d in data[i]:
                    if d == ind:
                        # print >> sys.stderr,d,
                        print (u"\u2588%s\u2588 " % d,end='') # Printing the word in color
                        continue

                    else:
                        print ("%s " % d ,end='')

        print ("\n ")

            

        # print 'Total count: %d' % count
    return count


def search_word(word, data):
    """
        search_word(): to find a given word in the file and show its occurences in the file
    """
    searched = {}
    i = 0
    for f in data:
        if word == f:
            i += 1
            searched[word] = i
            continue
    if not len(searched):
        print ('No results!')

    for k, v in searched.items():
        print ('Word: %s: Occurences: %d' % (k, int(v)))

    
    


