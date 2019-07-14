import matplotlib.pyplot as plt

plt.style.use('seaborn')
inputs = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
# ax.plot(inputs, squares, linewidth=3)
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=24)
ax.set_ylabel('Square', fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=14)

# for i, input in enumerate(inputs):
#     ax.scatter(input, squares[i])

# zip组合键和值来创建字典
# for k, v in dict(zip(inputs, squares)).items():
#     ax.scatter(k, v, s=200)
# ax.scatter(inputs, squares, s=400)
x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]
ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0))
# color map
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)
ax.axis([0, 1100, 0, 1100000])
plt.savefig('square.png', bbox_inches='tight')
plt.show()