# 1. 生成列表
print([x * x for x in range(1, 11)])

# 2. 复杂表达式
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.items()]
print('''<table>
 <tr><th>Name</th><th>Score</th><tr>
 ''')
print('\n'.join(tds))
print('</table>')

# 3.条件过滤
print([x * x for x in range(1, 11) if x % 2 == 0])

# 4.多层表达式
print([m + n for m in 'ABC' for n in '123'])
print([i*100 + j*10 + k for i in range(1, 10) for j in range(10) for k in range(10) if i == k])