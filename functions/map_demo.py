items = [1, 2, 3, 4, 5]
squared = list(map(lambda x : x ** 2, items))

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
funcs = [multiply, add] # 列表的函数
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))