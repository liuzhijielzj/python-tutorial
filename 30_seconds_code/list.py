# all_equal

'''
1, 2, 3, ..., length - 1 = 0, 1, 2, ..., length -2
'''
def all_equal(lst):
    return lst[1:] == lst[:-1]

all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True

# all_unique

def all_unique(lst):
    return len(lst) == len(set(lst))

x = [1,2,3,4,5,6]
y = [1,2,2,3,4,5]
all_unique(x) # True
all_unique(y) # False

# bifurcate
def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]
    ]
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]) # [ ['beep', 'boop', 'bar'], ['foo'] ]

# bifurcate_by
def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]

bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b') # [ ['beep', 'boop', 'bar'], ['foo'] ]

# Chunks

'''
Chunks a list into smaller lists of a specified size.

Use list() and range() to create a list of the desired size. 
Use map() on the list and fill it with splices of the given list. Finally, return use created list.
'''
from math import ceil

def chunk(lst, size):
    return list(
    map(lambda x: lst[x * size:x * size + size],
        list(range(0, ceil(len(lst) / size)))))
chunk([1,2,3,4,5],2) # [[1,2],[3,4],5]


'''
Removes falsey values from a list.
'''
def compact(lst):
    # list可以将迭代器转换为列表
    # filter在此返回迭代器
    return list(filter(bool, lst))

print(compact([0, 1, False, 2, '', 3, 'a', 's', 34])) # [ 1, 2, 3, 'a', 's', 34 ]

'''
Groups the elements of a list based on the given
    function and returns the count of elements in each group.

Use map() to map the values of the given list using the given function.
Iterate over the map and increase the element count each time it occurs.
'''
def count_by(arr, fn=lambda x: x):
    counts = {}
    for el in map(fn, arr):
        counts[el] = 1 if el not in counts else counts[el] + 1
    return counts
    
from math import floor
count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
print(count_by(['one', 'two', 'three'], len)) # {3: 2, 5: 1}

'''
Counts the occurrences of a value in a list.

Increment a counter for every item in the list that has the given value and is of the same type.
'''
def count_occurrences(lst, val):
    # return len([x for x in lst if x == val and type(x) == type(val)])
    count = 0
    for item in lst:
        if val == item and type(val) == type(item):
            # python中没有自增和自减功能
            ++count
            count = count + 1
    return count
print(count_occurrences([1, 2, 3, 2, 3, 2], 2))

'''
Returns the difference between two iterables.

Create a set from b, then use list comprehension on a to only keep values not
 contained in the previously created set, _b.
'''
def difference(a, b):
    s = set(b)
    return [item for item in a if item not in s]
print(difference([1, 2, 3], [1, 2, 4])) # [3]

'''
Deep flattens a list.

Use recursion. Define a function, 
spread, that uses either list.extend() or list.append() on each element in a list to flatten it.
Use list.extend() with an empty list and the spread function to flatten a list. 
Recursively flatten each element that is a list.
'''
lst = [1, 2]
lst.extend([[3], 4])
print(lst)
lst.append(5)
print(lst)

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(lst):
    result = []
    m = map(lambda x: deep_flatten(x) if type(x) == list else x, lst)
    result.extend(
        spread(list(m)))
    return result

print(deep_flatten([1, [2], [[3], 4], [5, [6, [7]]]])) # [1,2,3,4,5]

'''
Returns the difference between two lists, after applying
 the provided function to each list element of both.

Create a set by applying fn to each element in b, 
then use list comprehension in combination with fn on a
 to only keep values not contained in the previously created set, _b.
'''
def difference_by(a, b, fn):
    s = set(b)
    return [item for item in a if fn(item) not in s]

from math import floor
difference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]

'''
Returns True if the provided function returns True for every element in the list, False otherwise.

Use all() in combination with map and fn to check if fn returns True
 for all elements in the list.
'''
def every(lst, fn = lambda x: x):
    return all(map(fn, lst))
    
print(every([4, 2, 3], lambda x: x > 1)) # True
every([1, 2, 3]) # True

'''
Returns every nth element in a list.

Use [nth-1::nth] to create a new list that contains every nth element of the given list.
'''
def every_nth(lst, nth):
    return lst[nth - 1::nth]

print(every_nth([1, 2, 3, 4, 5, 6], 2))

'''
Filters out the non-unique values in a list.

Use list comprehension and list.count() to create a list containing only the unique values.
'''
def filter_non_unique(lst):
    return [item for item in lst if lst.count(item) == 1]

print(filter_non_unique([1, 2, 2, 3, 4, 4, 5])) # [1, 3, 5]

'''
Filters out the unique values in a list.

Use list comprehension and list.count() to create a list containing only the non-unique values.
'''
def filter_unique(lst):
    return [x for x in set(item for item in lst if lst.count(item) > 1)]

'''
Flattens a list of lists once.

Use nested list comprehension to extract each value from sub-lists in order.
'''
def flatten(lst):
    return [x for y in lst for x in y]

'''
Groups the elements of a list based on the given function.

Use map() and fn to map the values of the list to the keys of an object.
Use list comprehension to map each element to the appropriate key.
'''
def group_by(lst, fn):
    return {key : [el for el in lst if fn(el) == key] for key in map(fn,lst)}

'''
Returns True if there are duplicate values in a flast list, False otherwise.

Use set() on the given list to remove duplicates, compare its length with the length of the list.
'''
def has_duplicates(lst):
    return len(lst) != len(set(lst))

'''
Returns the head of a list.

use lst[0] to return the first element of the passed list.
'''
def head(lst):
    return lst[0]

'''
Returns all the elements of a list except the last one.

Use lst[0:-1] to return all but the last element of the list.
'''
def initial(lst):
    return lst[0:-1]

'''
Initializes a 2D list of given width and height and value.

Use list comprehension and range() to generate h rows where each is a list with length h, 
initialized with val. If val is not provided, default to None.
'''
def initialize_2d_list(w,h, val = None):
    return [[val for x in range(w)] for y in range(h)]
print(initialize_2d_list(2, 3, 0))

'''
Initializes a list containing the numbers in the specified range 
where start and end are inclusive with their common difference step.

Use list and range() to generate a list of the appropriate length, 
filled with the desired values in the given range. 
Omit start to use the default value of 0. Omit step to use the default value of 1.
'''
def initialize_list_with_range(end, start = 0, step = 1):
    return list(range(start, end + 1, step))
print(initialize_list_with_range(9,0,2))

'''
Initializes and fills a list with the specified value.

Use list comprehension and range() to generate a list of length equal to n, 
filled with the desired values. Omit val to use the default value of 0.
'''
def initialize_list_with_values(n, val = 0):
    return [val for x in range(n)]

'''
Returns a list of elements that exist in both lists.

Create a set from a and b, then use the built-in set operator & 
to only keep values contained in both sets, then transform the set back into a list.
'''
def intersection(a, b):
    sa, sb = set(a), set(b)
    return list(sa & sb)
print(intersection([1, 2, 3], [4, 3, 2])) # [2, 3]

'''
Returns a list of elements that exist in both lists, 
after applying the provided function to each list element of both.

Create a set by applying fn to each element in b, 
then use list comprehension in combination with fn on a to only 
keep values contained in both lists.
'''
def intersection_by(a, b, fn):
    sb = map(fn, b)
    return [item for item in a if fn(item) in sb]

from math import floor
print(intersection_by([2.1, 1.2], [2.3, 3.4],floor))

'''
Returns the last element in a list.

use lst[-1] to return the last element of the passed list.
'''
def last(lst):
    return lst[-1]

'''
Takes any number of iterable objects or objects with a length property 
and returns the longest one. If multiple objects have the same length,
the first one will be returned.

Use max() with len as the key to return the item with the greatest length.
'''
def longest_item(*args):
    return max(args, key = len)

'''
Returns the n maximum elements from the provided list. 
If n is greater than or equal to the provided list's length, 
then return the original list (sorted in descending order).

Use sorted() to sort the list, 
[:n] to get the specified number of elements. 
Omit the second argument, n, to get a one-element list.
'''
def max_n(lst, n=1):
    return sorted(lst, reversed=True)[:n]

def min_n(lst, n=1):
    return sorted(lst, reverse=False)[:n]

'''
Returns the most frequent element in a list.

Use set(list) to get the unique values in the list combined with max()
    to find the element that has the most appearances.
'''
def most_frequent(list):
    return max(set(list), key = list.count)
print(most_frequent([1,2,1,2,3,2,1,4,2]) )

'''
Returns False if the provided function returns True 
for at least one element in the list, True otherwise.

Use all() and fn to check if fn returns False for all the elements in the list.
'''
def none(lst, fn=lambda x: x):
    return all(not fn(x) for x in lst)
print(none([0, 1, 2, 0], lambda x: x >= 2 ))

'''
Moves the specified amount of elements to the end of the list.

Use lst[offset:] and lst[:offset] to get the two slices of the list and 
combine them before returning.
'''
def offset(lst, offset):
    return lst[offset:] + lst[0:offset]
print(offset([1, 2, 3, 4, 5], 2))

'''
Returns a random element from an array.

Use randint() to generate a random number that corresponds to an index in the list, return the element at that index.
'''
from random import randint

def sample(lst):
    return lst[randint(0, len(lst) - 1)]
print(sample([3, 7, 9, 11]))

