import random

# 1. drawing_integers function

# Goal: Make a list of random integers
# Parameters : Range of the integers: lb <= the integers <= ub, Length of the integers: trials
# Return: an integers list.
# Hint: Use randint function in the random module

def drawing_integers(lb, ub, trials):
    drawing_list = []
    if lb > ub:
        print("Please check the input upperbound is same or larger than the input lowerbound.")
        return None
    for i in range(trials):
        n = random.randint(lb, ub)
        drawing_list.append(n)
    return(drawing_list)


# Test
list1 = drawing_integers(6, 6, 20)

print(list1)


# 2. average_integers

# Goal: Compute the average of the integer sequence in the list
# Parameter: a list which is returned from drawing_integers
# Return: average value of the list

def average_integers(num_list):
    sum = 0
    for i in num_list:
        sum = sum + i
    average = sum/len(num_list)
    return(average)

# Test
print(average_integers(list1))

# 3. count_integers(num_list)

# Goal: Count the frequency of the integers in the list
# Parameter: a list which is returned from drawing_integers
# Return: A list of tuples that are the integer and its frequency Ex) [(1, 2), (2, 3), (3, 0), (4, 2)] for [4,1,2,2,4,2,1]