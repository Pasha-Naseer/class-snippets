import time
import random

every_avn_list = []
avn_std_car_count = 10
red_light_time = 9
yellow_light_time = 3
green_light_time = 9

for i in range(4):
    # x = int(input(f"Enter avenue {i+1} car count: "))
    x = random.randrange(10, 51)
    every_avn_list.append(x)

for i in every_avn_list:
    if i > avn_std_car_count:
        for j in range(i):
            red_light_time += 0.1
            yellow_light_time += 0.05
            green_light_time += 0.1


    print(red_light_time)
    print(yellow_light_time)
    print(green_light_time)

    print(f"Entry {every_avn_list.index(i)+1}")
    print("green light!")

    time.sleep(red_light_time)

    print('Yellow light!')

    time.sleep(yellow_light_time)

    print('red light!')

    time.sleep(green_light_time)
