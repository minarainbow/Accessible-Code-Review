# For your information, refer this definition of Fibonacci number http://en.wikipedia.org/wiki/Fibonacci_number
# Using while -loop, you should fill a list with these Fibonacci numbers which are less than 1000

# Examples
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

# We recommend you to start with two initial values, 0 and 1.

fib_list = []
i = 0
j = 1
fib_list.append(i)
fib_list.append(j)
k = i + j
while k < 1000:
    fib_list.append(k)
    i = j
    j = k
    k = i + j
print(fib_list)
