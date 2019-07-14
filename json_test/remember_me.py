import json_test

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json_test'
try:
    with open(filename, 'r') as f_obj:
        username = json_test.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json_test.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")