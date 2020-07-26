#!/usr/bin/env python3

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

if __name__ == '__main__':
    texts, calls = getCSVData()
    durationCall = int(calls[0][3])
    phoneNumber = calls[0][0]
    for call in calls:
        duration = int(call[3])
        if durationCall < duration:
            durationCall = duration
            phoneNumber = call[0]
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phoneNumber, str(durationCall)))
