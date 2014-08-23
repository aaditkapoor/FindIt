__author__ = "Aadit Kapoor"
__version__ = "1.0.0"

"""
    Name: storer.py
    Purpose: Keeps all the modification code
"""
import json

def store_data(file_):
    '''
        (str,file) -> list[]
        Return the content of the file into a list
    '''
    data = []
    for line in file_:
        data.append(line)  # For short data only

    return data  # Returning processed data


    # for i,j in enumerate(file_):
    #     data.append(j)


def remove_slashn(data):
    '''
        (list) -> list
        return a modified list with '\n' removed.
    '''
    if not data:
        print ('Invalid! Empty File')
    for i in range(len(data)):
        if '\n' in data[i]:
            
            data[i] = data[i].replace('\n', '')
        else:
            pass

   #d = [d.replace('\n','') for d in data]


def to_lower(data):
    '''
        to_lower(data) -> list
        Return the lowercases version of the list
    '''
##
##    for i in range(len(data)):
##        data[i] = data[i].lower()

    d = [d.lower() for d in data]

    data = d

