angle_between_consecutive_hour_marks = 360 / 12
angle_between_consecutive_minute_marks = 360 / 60
additional_hour_angle_per_every_minute = 30 / 60
hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
hour_angle = hour * angle_between_consecutive_hour_marks + (minute * additional_hour_angle_per_every_minute)
minute_angle = minute * angle_between_consecutive_minute_marks

if hour_angle > minute_angle:
    angle = hour_angle - minute_angle
elif hour_angle < minute_angle:
    angle = minute_angle - hour_angle
else:
    angle = 0

angle2 = 360 - angle
print(angle)
print(f"Bigger angle {angle2}")
# I will add seconds to be able to track the exact overlap where the angle is 0!
# This ccode will be updated
# Bugs are yet to be fixed!
