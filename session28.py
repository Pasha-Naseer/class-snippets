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