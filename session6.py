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


#             01
#         01  02  03
#     01  02  03  04  05
# 01  02  03  04  05  06  07
# 01  02  03  04  05  06  07
#     01  02  03  04  05
#         01  02  03
#             01
n = 200
with open("output.txt", 'w') as file:
    n_of_digits = len(str(n)) + 1
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" "*n_of_digits, end=" ", file=file)
        for e in range(1, i*2):
            print(f"{e:0{n_of_digits}d}", end=" ", file=file)
        print(file=file)

    for i in range(1, n+1).__reversed__():
        for j in range(1, n-i+1).__reversed__():
            print(" "*n_of_digits, end=" ", file=file)
        for e in range(1, i*2):
            print(f"{e:0{n_of_digits}d}", end=" ", file=file)
        print(file=file)

n = 100
with open("output.html", "w") as file:
    file.write("""
    <html>
    <body>
    <pre style="font-family: monospace; font-size: 10px;">
    """)

    n_of_digits = len(str(n)) + 1

    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" " * n_of_digits, end=" ", file=file)

        for e in range(1, i * 2):
            print(f"{e:0{n_of_digits}d}", end=" ", file=file)

        print(file=file)

    for i in range(1, n + 1).__reversed__():
        for j in range(1, n - i + 1).__reversed__():
            print(" " * n_of_digits, end=" ", file=file)

        for e in range(1, i * 2):
            print(f"{e:0{n_of_digits}d}", end=" ", file=file)

        print(file=file)

    file.write("""
    </pre>
    </body>
    </html>
    """)


# 1                 1  # 8   # 1  10-(2*i)
# 1 2             2 1  # 6   # 2
# 1 2 3         3 2 1  # 4   # 3
# 1 2 3 4     4 3 2 1  # 2   # 4
# 1 2 3 4 5 5 4 3 2 1  # 0   # 5
for i in range(1, 5+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for e in range(0, 10-(i*2)):
        print(" ", end=" ")
    for z in range(i, 0, -1):
        print(z, end=" ")
    print()
