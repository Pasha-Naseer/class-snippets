# conditional statement
x = 5
if x < 5:
    print(f"{x} is smaller than 5")
elif x > 5:
    print(f"{x} is bigger than 5")  # We could have multiple elif blocks if needed
else:
    print(f"x is 5")

# interactive coding
name = input("Enter Your Name: ")
last_name = input("Enter You last name: ")
print(f"Hello {name} {last_name}!")

# some string methods
my_string = "     Alan Turing        "
print(my_string.lower())
print(my_string.upper())
print(my_string.title())
print(my_string.capitalize())
print(my_string.rstrip())
print(my_string.lstrip())
print(my_string.strip())

# exercise
# ask if male or female (use string methods)
name = input("Enter Your Name: ").strip().capitalize()
last_name = input("Enter You last name: ").strip().capitalize()
gender = input("Enter gender(male/female): ").strip().lower()  # Because we will check in lower mode
if gender == "male":
    print(f"Hello mr.{name} {last_name}")
elif gender == 'female':
    print(f"Hello miss/mrs.{name} {last_name}")
elif gender == "AI":
    print("Hello World!")
else:
    print("Invalid Answer")