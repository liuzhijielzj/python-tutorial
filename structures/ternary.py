fat = True
# (if_test_is_false, if_test_is_true)[test]
fitness = ("skinny", "fat")[fat]
# 不使用元组条件表达式的缘故是因为在元组中会把两个条件都执行
print("Ali is", fitness)

# if-else 的条件表达式不会把两个条件都执行
condition = True
print(2 if condition else 1 / 0)

# 在元组中是先建数据，然后用True(1)/False(0)来索引到数据。 而if-else条件表达式遵循普通的if-else逻辑树
print((1 / 0, 2)[condition])
