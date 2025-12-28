"""
Bubble sort algorithm
BigO complexity: O(n2)!
"""
random_list = [6, 2, 3, 5, 4, 9, 1]
for _ in range(len(random_list)):
    for i in range(len(random_list) - 1):
        if random_list[i] > random_list[i+1]:
            random_list[i], random_list[i+1] = random_list[i+1], random_list[i]

print(random_list)

# also in python we can
random_list = [6, 2, 3, 5, 4, 9, 1]
print(sorted(random_list))
random_list.sort()
print(random_list)
