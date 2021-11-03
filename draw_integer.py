import random

# drawing_integers function
def drawing_integers(lb, ub, trials):
    drawing_list = []
    for i in range(trials):
        n = random.randint(lb, ub)
        drawing_list.append(n)
    return(drawing_list)

# Test
list1 = drawing_integers(1, 6, 20)

print(list1)
