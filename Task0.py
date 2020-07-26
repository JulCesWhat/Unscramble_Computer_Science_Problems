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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

if __name__ == '__main__':
    texts, calls = getCSVData()
    f_text = texts[0]
    l_call = calls[len(calls) - 1]
    print("First record of texts, {} texts {} at time {}".format(f_text[0], f_text[1], f_text[2]))
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(l_call[0], l_call[1], l_call[2], l_call[3]))
    