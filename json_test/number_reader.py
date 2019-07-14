import json_test

filename = 'numbers.json_test'
with open(filename) as f_obj:
    numbers = json_test.load(f_obj)
print(numbers)