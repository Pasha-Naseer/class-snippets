# case types

# snake_case
# SCREAMING_SNAKE_CASE
# camelCase
# PascalCase
# kebab-case


# arithmetic operators
x = 6
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x % y)
print(x / y)  # floating point division
print(x // y)  # integer division

# concatenate
# str + str
name = "John"
last_name = "Wick"
age = 32

print(name + " " + last_name)

print(name, last_name)

print(f"{name} {last_name}")

# bio
print("I am" + " " + name + " " + last_name + "," + " " + "and I am" + " " + str(age) + " " + "years old!")
print("I am", name, last_name, ",", "and I am", age, "years old!")  # the whitespace before the comma is annoying
print(f"I am {name} {last_name}, and I am {age} years old!")

# type()
my_str = "man"
my_int = 1
print(type(my_str))
print(type(my_int))

# Collection data types
# list
# ordered, changeable, allows duplicates
students = ["Tom", "Alexander", "Arta", "Dimitri", "Alice"]
print(students)

# index
print(students[0])
print(students[3])

# slice
print(students[0:5])
print(students[0:3])
print(students[-5:-2])
print(students[0:5:1])
print(students[:])
print(students[0:5:2])
print(students[5::-1])


# Slicing and indexing are also for strings
fruit = "watermelon"
print(fruit[0:5])

# len
print(len(students))

# being changeable
# methods
# info
print(students.index("Alexander"))
print(students.count("Alexander"))
# manipulate
students.append("Pedro")
print(students)
students.insert(2, "Luke")
print(students)
students.remove("Arta")
print(students)
students.pop(1)
print(students)
popped = students.pop()
print(students)
print(popped)
students2 = ["Jim", "Conor", "Eliot"]
students.extend(students2)
print(students)
students.reverse()
print(students)
students.sort()
print(students)
students.sort(reverse=True)
print(students)
other_students = students.copy()
print(other_students)
other_students.clear()
print(other_students)
