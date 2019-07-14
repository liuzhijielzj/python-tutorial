import json_test

filename = 'username.json_test'

with open(filename) as f_obj:
    username = json_test.load(f_obj)
    print("Welcome back, " + username + "!")