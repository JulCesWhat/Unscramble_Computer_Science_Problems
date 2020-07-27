# Unscramble_Computer_Science_Problems

## Time Complexity (inclusing reading csv files)

### Task O: O(2n) => O(n)

The time complexity for this task is O(2n) because we are iterating over all the rows in the calls and text files while reading it. Since 2 does not matter when n is large, we can remove it.

### Task 1: O(4n) => O(n)

The time complexity for this task is O(4n) because we are iterating over all the rows in the calls and text files while reading it and then iterating over all the text and call rows that we have read. Since 4 does not matter when n is large, we can remove it.

### Task 2: O(3n) => O(n)

The time complexity for this task is O(3n) because we are iterating over all the rows in the calls and text files while reading it and then iterating over all the calls that we have read. Since 3 does not matter when n is large, we can remove it.

### Task 3: O(4n) => O(n)

The time complexity for this task is O(4n) because we are iterating over all the rows in the calls and text files while reading it. We are then iterating over all the calls and then over all the phone numbers that have been called by the bangalore number. Since 4 does not matter when n is large, we can remove it.

### Task 4: O(6n) => O(n)

The time complexity for this task is O(6n) because we are iterating over all the rows in the calls and text files while reading it. We are then iterating over all the calls and then over all the texts and then over all the calls again and then over all the remaning sent calls while printing the result. Since 6 does not matter when n is large, we can remove it.



## Time Complexity (not inclusing reading csv files)

### Task O: O(1) => O(1)

The time complexity for this task is constant since we are not iterating over anything and just retriving values at a certain place.

### Task 1: O(2n) => O(n)

The time complexity for this task is 0(2n) becuase we are iterating over all the calls and texts that we read. Since 2 does not matter when n is large, we can remove it.

### Task 2: O(1n) => O(n)

The time complexity for this task is 0(1n) becuase we are iterating over all the calls. Since 1 does not matter when n is large, we can remove it.

### Task 3: O(2n) => O(n)

The time complexity for this task is 0(2n) becuase we are iterating over all the calls and then over all the phones that have been called. Since 2 does not matter when n is large, we can remove it.

### Task 4: O(4n) => O(n)

The time complexity for this task is 0(4n) becuase we are iterating over all the calls and then text and then calls again and then over all the remaning phone number that have given a call. Since 4 does not matter when n is large, we can remove it.


## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run