# built-in function
print()
print(len("James"))
# input()
print(range(1, 6))
print(type("hey"))
print(ord("A"))
print(chr(66))
print(list(enumerate(['a', 'b', 'c', 'd'])))
print(abs(-2))
print(ascii("に"))
print(max(22, 1, 4, 56, 87, 98))
print(min(22, 1, 4, 56, 87, 98))
print(round(12.4586, 2))
print(sum([12, 123, 453, 56, 123]))
list1 = [1, 2, 3, 4]
list2 = [11, 22, 33, 44]
print(list(zip(list1, list2)))


# create a function
def plus_five(n):  # snake case
    return n + 5


print(plus_five(6))
print(plus_five(8))
print(plus_five(10))


# divide 5
def divide_5(number):
    if number == 0:
        return "Can't divide by 0!"
    return 5 / number


print(divide_5(10))
print(divide_5(0))  # argument


# divide
def divide(x, y):  # parameter
    return x / y


# positional arguments
print(divide(23, 2))

# keyword arguments
print(divide(y=4, x=8))

# *args(arbitrary positional arguments)


def marathon_winner(*names):
    return f"Winner: {names[0]}"


print(marathon_winner("Martin", "Alfred", "Merab", "George"))


# **kwargs (arbitrary keyword arguments)
def race_winner(**cars):
    return f"Winner team: {cars['first']}"


print(race_winner(second="Ferrari", first="RedBull", third="McLaren"))


# lambda
divide = lambda x, y: x / y
print(divide(4, 2))

divide_5 = lambda x: "can't divide by 5" if x == 0 else 5 / x
print(divide_5(0))
print(divide_5(10))


# map
def power_of2(x):
    return x ** 2


num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(power_of2, num_list)))

power_of2 = lambda x: x ** 2
print(list(map(power_of2, num_list)))


# exercise 1
# write a function to return the average of n numbers

def avg(*nums):
    return sum(nums) / len(nums)


print(avg(1, 5, 7, 2, 6))
print(avg(2, 4, 6))


# exercise 2
# write a function to return even or odd
def even_or_odd(n):
    print("Even" if n % 2 == 0 else "Odd")


even_or_odd(5)
even_or_odd(6)


# avg with input
def avg():
    numbers = []
    n = int(input("How many? "))
    for i in range(n):
        number = int(input("Enter number: "))
        numbers.append(number)
    return sum(numbers) / len(numbers)


print(avg())


# scope
x = 6
def func():
    x = 7
    print(x)
print(x)
func()


# recursive functions
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)


add = lambda a, b: a+b
print(add(2, 3))


# reduce
from functools import reduce
x = [1, 2, 3, 4, 5, 6]
total = reduce(add, x)
print(total)

# filter
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)