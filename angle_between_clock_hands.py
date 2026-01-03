import time
import datetime

def angle_between_clock_hands(_hour, _minute):
    angle_between_consecutive_hour_marks = 360 / 12  # 30
    angle_between_consecutive_minute_marks = 360 / 60  # 6
    additional_hour_angle_per_every_minute = 30 / 60  # 0.5
    hour = _hour
    minute = _minute
    hour_angle = hour * angle_between_consecutive_hour_marks + (minute * additional_hour_angle_per_every_minute)
    minute_angle = minute * angle_between_consecutive_minute_marks

    # print(f"hour angle: {hour_angle}")
    # print(f"minute angle: {minute_angle}")

    if hour_angle > minute_angle:
        angle = hour_angle - minute_angle
    elif hour_angle < minute_angle:
        angle = minute_angle - hour_angle
    else:
        angle = 0

    if angle > 180:
        angle2 = 360 - angle
        print(f"smaller angle: {angle2}")
        print(f"Bigger angle: {angle}")
    elif angle < 180:
        angle2 = 360 - angle
        print(f"smaller angle: {angle}")
        print(f"Bigger angle: {angle2}")
    else:
        print("big angle and small angle are equal!")
        print(angle)

# input custom hour
while True:
    try:
        h = int(input("Enter hour: "))
    except ValueError:
        print("Invalid Input!")
    else:
        if h in range(0, 13):
            break
        elif h in range(13, 25):
            h -= 12
            break
        else:
            print("Invalid Input!")

# input custom minute
while True:
    try:
        m = int(input("Enter minute: "))
    except ValueError:
        print("Invalid Input!")
    else:
        if m in range(0, 60):
            break
        else:
            print("Invalid Input!")

angle_between_clock_hands(h, m)
print("*"*30)
# current angle between the time hands
print("The angle between the current time clock hands:")
print(datetime.datetime.now().strftime("%I : %M %p"))
h = int(datetime.datetime.now().strftime("%#I"))
m = int(datetime.datetime.now().minute)
angle_between_clock_hands(h, m)

# I will add seconds to be able to track the exact overlap where the angle is 0!
# This code will be updated
