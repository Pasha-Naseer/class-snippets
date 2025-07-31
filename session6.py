import math
# for loop
tasks = ["eat", "sleep", "Code", "repeat"]
for i in tasks:
    print("~", i)

for j in range(0, 4):
    print("~", j)

# digital clock
for h in range(0, 23 + 1):
    for m in range(0, 59 + 1):
        time = f"{h} : {m}"
        print(time)

# nested for loops
# fact
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print(fact)

# standard library
print(math.factorial(num))

# nested for loop

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        print('*', end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(1, 5 + 1):
    for j in range(i, 1 - 1, -1):
        print(j, end=" ")
    print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

k = 7
for i in range(1, 5 + 1):
    for j in range(1, k-i):
        print(j, end=" ")
    print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

k = 6
for i in range(1, 5 + 1):
    for j in range(k-i, 0, -1):
        print(j, end=" ")
    print()
