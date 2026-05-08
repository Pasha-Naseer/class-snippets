# functions

# built-in
# enumerate
test = ['a', 'b', 'c', 'd']
for i, j in enumerate(test):
    print(f"{i}:{j}")


# zip
test2 = [1, 2, 3, 4]
print(list(zip(test, test2)))

# len
print(len(test))
print(len(test2))


# recursive functions
def recursive_factorial(n):
    if n == 1:
            return n
    else:
            return n * recursive_factorial(n-1)


# lambda
add = lambda a, b: a+b
print(add(2, 3))

# map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# reduce
from functools import reduce
x = [1, 2, 3, 4, 5, 6]
total = reduce(add, x)
print(total)

# filter
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)