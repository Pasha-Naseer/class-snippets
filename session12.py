'''
Two fun exercises for playing with python syntax!
exercise 1)
Try to sort an unordered list without using list methods and max/min functions.
exercise 2)
Dicts are for accessing values by keys.
Try to access keys by values using loops!
'''
# exercise 1
# [1, 2, 3, 4, 5]
my_list = [1, 4, 5, 3, 2]
sort_list = []
x = float('+inf')
while my_list:
    for i in my_list:
        if i < x:
            x = i
    sort_list.append(x)
    my_list.remove(x)
    x = 25
print(sort_list)


# [5, 4, 3, 2, 1]
my_list = [1, 4, 5, 3, 2]
sort_list = []

y = float('-inf')
while my_list:
    for i in my_list:
        if i > y:
            y = i
    sort_list.append(y)
    my_list.remove(y)
    y = float('-inf')
print(sort_list)

# exercise 2
soccer_clubs = {'Barca': 250, 'Liverpool': 230, "Arsenal": 300, "Tottenham": 249}
# 1. Compare scores
# 2. access the key (create manual index, since dicts are ordered)
x = 0
for i in soccer_clubs.values():
    if i > x:
        x = i
y = 0
for i in soccer_clubs.keys():
    y += 1
    if soccer_clubs[i] == x:
        print(i)
