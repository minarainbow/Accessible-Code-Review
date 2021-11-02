# Accessible-Code-Review
This is a repository for our project to be submitted to CSCL 2022. 

## Task 1 Fibonacci Number
For your information, refer this definition of Fibonacci number
http://en.wikipedia.org/wiki/Fibonacci_number
Using while -loop, you should fill a list with these Fibonacci numbers
which are less than 1000

### Examples
evaluate fibonacci.py

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

We recommend you to start with two initial values, 0 and 1.


## Task 2 Drawing Integers
### 1. drawing_integers(lb, ub, trials)
- Goal: Make a list of random integers
- Parameters
  - Range of the integers: lb <= the integers <= ub
  - Length of the integers: trials
- Return: an integers list.
- Hint: Use randint function in the random module

### 2. average_integers(num_list)
- Goal: Compute the average of the integer sequence in the list
- Parameter: a list which is returned from drawing_integers
- Return: average value of the list

### 3. count_integers(num_list)
- Goal: Count the frequency of the integers in the list
- Parameter: a list which is returned from drawing_integers
- Return: A list of tuples that are the integer and its frequency
Ex) [(1, 2), (2, 3), (3, 0), (4, 2)] for [4,1,2,2,4,2,1]

### Examples
list1 = drawing_integers(1, 6, 20)

print(list1)

print(average_integers(list1))

print(count_integers(list1))

print()

list2 = drawing_integers(5, 12, 15)

print(list2)

print(average_integers(list2))

print(count_integers(list2))

**Expected Results**

[6, 1, 6, 4, 5, 1, 4, 1, 1, 5, 3, 2, 3, 4, 5, 5, 5, 6, 6, 1]

3.7

[(1, 5), (2, 1), (3, 2), (4, 3), (5, 5), (6, 4)]

[11, 11, 11, 8, 10, 9, 6, 5, 5, 10, 12, 6, 9, 9, 11]

8.86666666667

[(5, 2), (6, 2), (7, 0), (8, 1), (9, 3), (10, 2), (11, 4), (12, 1)]
