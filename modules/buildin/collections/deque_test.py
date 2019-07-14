from collections import deque

# 高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.insert(0, 'd')
q.appendleft('e')
print(q)
q.pop()
print(q)
q.popleft()
print(q)