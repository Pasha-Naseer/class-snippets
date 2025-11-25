import time
user1 = str(input("Enter username1: "))
input('press \'enter\' to start...')
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print(f'Hold Your freaking breath! {user1}')
start_time = time.time()

input("Press 'enter' to stop...")
end_time = time.time()
record1 = end_time - start_time
print(f"{user1} record -> {record1}")

print(30 * "-")

user2 = str(input("Enter username2: "))
input('press \'enter\' to start...')
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print(f'Hold Your freaking breath! {user2}')
start_time = time.time()

input("Press 'enter' to stop...")
end_time = time.time()
record2 = end_time - start_time
print(f"{user2} record -> {record2}")

print(30 * "-")

if record1 > record2:
    print(f"FATALITY! {user1} Wins!")
elif record1 < record2:
    print(f"FATALITY! {user2} Wins!")
else:
    print("Both lost!")


# Meysam -> 62.374
# Darya -> 14.653
# Arshan -> 76.846
# Asal -> 43.286
# Zohre -> 67.383
# Tarranom -> 99.270
