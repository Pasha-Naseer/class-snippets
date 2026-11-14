"""
JSON
reporter, datetime, report
{datetime: [reporter: report]}
"""
import datetime
import json
import os
# import pyttsx3

# engine = pyttsx3.init()

work_report = {}
while True:
    reporter = input("Enter reporter: ")
    report = input("Enter report: ")
    current_time = str(datetime.datetime.now())

    work_report[current_time] = [reporter, report]

    resume = input("Do you want to continue?(y/n) ").strip().lower()
    if resume == "n":
        break


# file addresses

# absolute address -> C:\Users\MFT\PycharmProjects\class-225\work_report.py
# relative address -> work_report.py

# modes
# r -> (read) | exists()->read, not exists()->error
# w -> (write) | exists()->overwrite, not exists()->create
# a -> (append) | exist()->append, not exists()->create
# x -> (create) | exists()->error, not exists()->create

# context manager
if os.path.exists("work_report.json"):
    with open("work_report.json", 'r') as f:  # Error
        data = json.load(f)
else:
    data = {}

data.update(work_report)

with open("work_report.json", "w") as f:
    json.dump(data, f, indent=1)
print("JSON file created successfully!")


# for i, j in work_report.items():
#     engine.say(f"reporter {j[0]} report {j[1]}")
#     engine.runAndWait()




