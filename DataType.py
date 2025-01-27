# 1.同时定义三个变量a、b、c，给这三个变量赋值都是100
a = b = c = 100
# 输出内容：a=100,b=100,c=100
print('a=%d,b=%d,c=%d' % (a, b, c))

# 2.可以一次性给多个变量赋值，注意赋值顺序。在这里等同于d=a+1,e=b+2,f=300
d, e, f = a + 1, b + 2, 300
# 输出内容：d=101,e=102,f=300
print(f'd={d},e={e},f={f}')

# 3.由于py定义变量时不需要指定类型，因此可以使用type方法获取变量的类型
name, test = 'zhangsan', True
# 输出内容：<class 'int'> <class 'str'> <class 'bool'>
print(type(a), type(name), type(test))

# 4.使用isinstance函数获取变量是否是指定类型的实例
# 输出内容：变量name的值是zhangsan，类型是否为string：True，类型是否为int：False。
print('变量name的值是%s，类型是否为string：%s，类型是否为int：%s。' % (name, isinstance(name, str), isinstance(name, int)))

# 5.bool类型
# 5.1 bool类型是int类型的子类，且只有两个实例True和False。True相当于1，False相当于0。因此True和False可以与数字做计算。
# 输出内容：True + 1=2
print(f'{True + 1=}')
# 输出内容：False + 1=1
print(f'{False + 1=}')
# 5.2 可以使用bool函数，将其他类型转为bool类型
# 输出内容：bool(0)=False
print(f'{bool(0)=}')
# 输出内容：bool(100)=True
print(f'{bool(100)=}')
# 输出内容：bool('')=False
print(f'{bool('')=}')
# 输出内容：bool('test')=True
print(f"{bool('test')=}")
# 输出内容：bool([])=False
print(f"{bool([])=}")
# 输出内容：bool([1,'a'])=True
print(f"{bool([1,'a'])=}")
# 5.3 可以使用int函数，将bool类型转换为int类型
# 输出内容：int(bool(name))=1
print(f'{int(bool(name))=}')
# 输出内容：int(False)=0
print(f'{int(False)=}')
# 5.4 比较的值是True或False
# 输出内容：1>0=True
print(f'{1>0=}')
# 5.5 在py中可以使用多种类型表示True和False
# string类型：''代表False，其余代表True
# int类型：0代表False，其余代表True
# 数组：空数组[]代表False，其余代表True
# 以下式子中，if后面如果是0、''、[]，那么输出的都是False，否则输出的是True
if [0, 0]:
    print('true')
else:
    print('false')

# 6.数据类型转换
# 两个可以兼容的类型的变量进行计算，会进行隐式转换
# 下面a1是int类型，a2是bool类型，而bool是int的子类，所以这两个变量可以相加
a1,a2=15,True
# 输出内容：a1+a2=16
print(f'{a1+a2=}')

# 下面a3是int类型，a4是string类型，无法兼容因此执行会报错
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
a3,a4=15,'5'
# print(f'{a3+a4=}')
# 我们可以通过强制类型转换，使计算能够执行
# 输出内容：a3+int(a4)=20
print(f'{a3+int(a4)=}')

a5,a6,a7=20,[],10.2
a8,a9,a10=bool(a5),bool(a6),int(a7)
# 输出内容：a8=True,a9=False,a10=10
print('a8=%s,a9=%s,a10=%s'% (a8,a9,a10))