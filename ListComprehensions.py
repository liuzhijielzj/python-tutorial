print([x * x for x in range(1, 11) if x % 2 == 0]) #for循环后面还可以加上if判断
print([m + n for m in 'ABC' for n in 'XYZ']) #可以使用两层循环
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

import os

print([d for d in os.listdir('.')])

print([s.lower() for s in ['1', 2, '3', '4', 5] if isinstance(s, str)])