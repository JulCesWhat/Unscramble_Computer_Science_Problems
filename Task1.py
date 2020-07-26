#!/usr/bin/env python3

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv

def getCSVData():
    texts = []
    calls = []
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
    return (texts, calls)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

if __name__ == '__main__':
    dicTelephones = {}
    texts, calls = getCSVData()
    for text in texts:
        if not dicTelephones.get(text[0]):
            dicTelephones[text[0]] = True
        if not dicTelephones.get(text[1]):
            dicTelephones[text[1]] = True
    for call in calls:
        if not dicTelephones.get(call[0]):
            dicTelephones[call[0]] = True
        if not dicTelephones.get(call[1]):
            dicTelephones[call[1]] = True
    print("There are {} different telephone numbers in the records.".format(len(dicTelephones)))
    