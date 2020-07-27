# Unscramble_Computer_Science_Problems

## Time Complexity (inclusing reading csv files)

### Task O:

* Worse case complexity: O(n)
* Algorithm:
    * Reading all calls from csv: O(n)
    * reading all texts from csv: O(n)
    * Getting first element of text: O(1)
    * Getting last element of calls: O(1)
    * Printing first text: O(1)
    * Printing last call: O(1)

### Task 1:

* Worse case complexity: O(n)
* Algorithm:
    * Creating telephone dictionary: O(1)
    * Reading all calls from csv: O(n)
    * reading all texts from csv: O(n)
    * First check: O(1)
    * Update dictionary: O(1)
    * Second check: O(1)
    * Update dictionary: O(1)
    * Iterating over all texts: O(n)
    * Iterating over all calls: O(n)
    * First check: O(1)
    * Update dictionary: O(1)
    * Second check: O(1)
    * Update dictionary: O(1)
    * Printing message: O(1)

### Task 2:

* Worse case complexity: O(n)
* Algorithm:
    * Reading all calls from csv: O(n)
    * reading all texts from csv: O(n)
    * Creating durationCall: O(1)
    * Creating phoneNumber: O(1)
    * Iterating over all calls: O(n)
    * Creating duration: O(1)
    * Doing check: O(1)
    * Setting new durationCall value: O(1)
    * Setting new phoneNumber value: O(1)
    * Printing message: O(1)

### Task 3:

* Worse case complexity: O(n + 𝑛log𝑛)
* Algorithm:
    * Reading all calls from csv: O(n)
    * reading all texts from csv: O(n)
    * Creating total_calls: O(1)
    * Creating called_phones: O(1)
    * Iterating over calls: O(1)
    * Checking for (080) or 140: O(1)
    * Spletting string: O(n)
    * Lenght check: O(1)
    * Creating code: O(1)
    * Updatting total_calls: O(1)
    * Check for called_phones: O(1)
    * Update called_phones: O(1)
    * Sorting call_phones: 𝑂(𝑛log𝑛)
    * Iterating over all_lines: O(n)
    * printing line: O(1)
    * Creating percentage_lines: O(1)
    * Checking called_phones: O(1)
    * Setting new percentage_lines: O(1)
    * Printing message: O(1)

### Task 4:

* Worse case complexity: O(n + 𝑛log𝑛)
* Algorithm:
    * Reading all calls from csv: O(n)
    * reading all texts from csv: O(n)
    * Creating send_calls: O(1)
    * Iterating over calls: O(n)
    * Checking send_calls: O(1)
    * Updating send_calls: O(1)
    * Iterating over texts: O(n)
    * Checking send_calls: O(1)
    * Deleting send_calls value: O(1)
    * Checing send_calls: O(1)
    * Deleting send_calls value: O(1)
    * Iterating over calls: O(n)
    * Checing send_calls: O(1)
    * Deleting send_calls value: O(1)
    * Printing message: O(1)
    * Sorting: 𝑂(𝑛log𝑛)
    * Iterating over all_send_calls: O(n) 
    * Printing message: O(1)



## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run