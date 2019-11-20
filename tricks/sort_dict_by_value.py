xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(sorted(xs.items(), key=lambda x: x[1]))
print(xs)

import operator
sorted(xs.items(), key=operator.itemgetter(1))
