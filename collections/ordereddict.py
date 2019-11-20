'''
OrderedDict keeps its entries sorted as they are initially inserted. Overwriting a value
of an existing key doesn’t change the position of that key. However, deleting and
reinserting an entry moves the key to the end of the dictionary
'''
colours = {"Red" : 198, "Green" : 170, "Blue" : 160}
for key, value in colours.items():
    print(key, value)

from collections import OrderedDict
colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)