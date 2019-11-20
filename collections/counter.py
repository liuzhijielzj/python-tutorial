#Counter是一个计数器，它可以帮助我们针对某项数据进行计数
'''
一个 Counter 是一个 dict 的子类，用于计数可哈希对象。
它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。
计数可以是任何整数值，包括0和负数。 Counter 类有点像其他语言中的 bags或multisets。
'''
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)

# 元素从一个 iterable 被计数或从其他的 mapping (or counter)初始化
c = Counter()
print(c)
c = Counter('gallahad') 
print(c)
c = Counter({'red': 4, 'blue': 2})
print(c)
c = Counter(cats=4, dogs=8)  
print(c)

# Counter对象有一个字典接口，如果引用的键没有任何记录，就返回一个0
c = Counter(['eggs', 'ham'])
print(c['eggs'])
print(c['bacon'])
c['eggs'] = 0
print(c['eggs'])
del c['eggs'] 
print(c['eggs'])

c = Counter(a=4, b=2, c=0, d=-2)
'''
返回一个迭代器，其中每个元素将重复出现计数值所指定次。 元素会按首次出现的顺序返回。 如果一个元素的计数值小于一，elements() 将会忽略它。
'''
print(sorted(c.items()))
print(Counter('abracadabra').most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts

