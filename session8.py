import math


def binary_search(user, start, end):
    import random
    num = random.randint(start, end)
    counter = 0
    print(f"Guess the number\nRange -> {start} - {end}")
    while True:
        guess = int(input("Enter Your Guess: "))
        if guess not in range(start, end + 1):
            print('What the hell\nOut of range!')
        elif guess == num:
            counter += 1
            print("Found it!")
            print(f"{user} Good job!\nYour Record --> {counter}")
            break
        elif guess < num:
            counter += 1
            print("Wrong guess fella\nGuess higher...")
        elif guess > num:
            counter += 1
            print('Wrong guess fella\nGuess lower...')
    return counter


beginning = int(input("Choose Range Start: "))
while True:
    ending = int(input("Choose Range End: "))
    if ending > beginning:
        break
    print(f"End Should be bigger than {beginning}")

n = (ending + 1) - beginning
bigO = math.ceil(math.log2(n))
print(f"BigO ---> {bigO}")

# user 1
first_user = str(input("Enter a username: "))
user1 = binary_search(first_user, beginning, ending)

# user 2
second_user = str(input("Enter a username: "))
user2 = binary_search(second_user, beginning, ending)

if user1 < user2:
    print(f"{first_user} won!\nCongratulations!")
elif user1 > user2:
    print(f"{second_user} won!\nCongratulations!")
else:
    print('Draw Draw Draw!')
