#with open('pi_digits.txt') as file_object:
with open('test_files/pi_digits.txt') as file_object: #relative path
    contents = file_object.read()
    print(contents.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)

birthday = input("please input your birthday, in format mmdd yy: ");
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


