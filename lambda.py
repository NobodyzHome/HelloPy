from functools import reduce

# lambda函数
# lambda函数是一种轻型的函数定义方式，不需要使用def来定义。通常是联合map、reduce等方法来使用。
# lambda 函数特点：
# lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
# lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。

# 下面定义了一个lambda函数，这个函数有两个入参，其功能是将两个函数加在一起。
# 将lambda函数对象赋值给my_sum变量，就可以使用该变量来调用lambda函数了。
my_sum = lambda x, y: x + y
# 调用lambda函数
rst1 = my_sum(5, 6)
# 输出内容：rst1=11
print(f'{rst1=}')

# lambda函数通常与map、reduce等方法联用，通过入参一个lambda函数对象和一个可迭代对象来进行数据的转换
rst2 = map(lambda x: {x: x * 3}, range(10))
# 输出内容：list(rst2)=[{0: 0}, {1: 3}, {2: 6}, {3: 9}, {4: 12}, {5: 15}, {6: 18}, {7: 21}, {8: 24}, {9: 27}]
print(f'{list(rst2)=}')

# 下面实现了对一个list中的元素进行相互乘起来的功能，也就是：1 * 2 * 3 * 4 * 5=120
rst3 = reduce(lambda prev, cur: prev * cur, [1, 2, 3, 4, 5])
# 输出内容：rst3=120
print(f'{rst3=}')
