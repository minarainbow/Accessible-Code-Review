# For your information, refer this definition of Fibonacci number http://en.wikipedia.org/wiki/Fibonacci_number
# Using while -loop, you should fill a list with these Fibonacci numbers which are less than 1000

# Examples
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

# We recommend you to start with two initial values, 0 and 1.


# Required variables
first_num = 0
second_num = 1
sum = first_num + second_num
fib_list = [0, 1]

# Loop body
while sum < 1000:
    fib_list.append(sum)
    first_num = second_num
    second_num = sum
    sum = first_num + second_num


# Print result
print(fib_list)
