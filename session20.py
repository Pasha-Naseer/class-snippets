# multiplication table
for i in range(1, 10+1):
    for j in range(1, 10+1):
        print(f"{i * j:3}", end=" ")
    print()

# print(55 * 3)
# print(3+6+9+12+15+18+21+24+27+30)


print("\n")


# component table
for i in range(1, 10+1):
    for j in range(1, 10+1):
        print(f"{i ** j:11}", end=' ')
    print()


print("\n")


# *        *
#  *      *
#   *    *
#    *  *
#     *

for i in range(1, 6):
    for j in range(1, 10):
        if j == i or j == 10-i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


print("\n")


#     *
#    * *
#   *   *
#  *     *
# *       *

for i in range(1, 6):
    for j in range(1, 10):
        if 6-i == j or 4+i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n")

for i in range(1, 8):
    for j in range(1, 10):
        if j == 1+i or j == 9-i or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
