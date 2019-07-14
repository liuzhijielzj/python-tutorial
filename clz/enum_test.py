from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数

from enum import Enum, unique

# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun)
print(Weekday['Mon'])
print(Weekday.Sun.value)
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
print(Weekday(1))
print(Weekday(7))