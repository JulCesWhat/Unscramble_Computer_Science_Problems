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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

if __name__ == '__main__':
    texts, calls = getCSVData()

    send_calls = {}
    for row_call in calls:
        if not send_calls.get(row_call[0]):
            send_calls[row_call[0]] = True

    for row_text in texts:
        if send_calls.get(row_text[0]):
            # send_calls[row_text[0]] = False
            del send_calls[row_text[0]]
        
        if send_calls.get(row_text[1]):
            # send_calls[row_text[1]] = False
            del send_calls[row_text[1]]

    for row_call in calls:
        if send_calls.get(row_call[1]):
            # send_calls[row_call[1]] = False
            del send_calls[row_call[1]]

    print("These numbers could be telemarketers: ")
    all_send_calls = sorted(list(send_calls))
    for send in all_send_calls:
        print(send)
    