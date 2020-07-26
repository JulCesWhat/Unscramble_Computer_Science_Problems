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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
    - Fixed lines start with an area code enclosed in brackets. The area
    codes vary in length but always begin with 0.
    - Mobile numbers have no parentheses, but have a space in the middle
    of the number to help readability. The prefix of a mobile number
    is its first four digits, and they always start with 7, 8 or 9.
    - Telemarketers' numbers have no parentheses or space, but they start
    with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

if __name__ == '__main__':
    texts, calls = getCSVData()
    total_calls = 0
    called_phones = {}
    for call in calls:
        if "(080)" in call[0]:
            areaCode = call[1].split(")")
            if (len(areaCode) > 1):
                code = areaCode[0] + ")"
                total_calls += 1
                if called_phones.get(code):
                    called_phones[code] += 1
                else:
                    called_phones[code] = 1
                    # print(code)
            elif "140" in call[0]:
                code = "140"
                total_calls += 1
                if called_phones.get(code):
                    called_phones[code] += 1
                else:
                    called_phones[code] = 1
                    # print("140")

    all_lines = sorted(list(called_phones))
    print("The numbers called by people in Bangalore have codes:")
    for line in all_lines:
        print(line)

    percentage_lines = 0
    if called_phones.get("(080)"):
        percentage_lines = called_phones["(080)"] / total_calls

    print("\n{:0.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_lines))
