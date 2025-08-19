# files
file = open('beginner.txt', 'r')  # relative path
print(file.readlines())  # returns every line of the file as an item of the list
print(file.readline())  # returns a line each time
print(file.readline())
print(file.readline())
print(file.read())  # reads the whole file
print(file.read(5))  # You have a specified the number of the characters you want to return
file.close()
file = open('beginner.txt', 'r')
file.seek(3)
print(file.readline())  # adjusts the cursor
file = open('beginner2.txt', 'w')
file.write('This is also an unworthy text to read!')
file.close()

file = open('beginner.txt', 'a')
file.write('\nNothing more to say!')
file.close()

file = open('beginner.txt', 'x')
file.write('xxxxxxxxxxxxxxxxxx!')
file.close()  # file exists

with open('beginner.txt', 'a') as file:
    file.write('\nThe End')

with open('beginner.txt3', 'w') as file:
    file.writelines(['The following line is written to the file:', '\nThe following line'])
