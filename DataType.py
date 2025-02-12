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
a1, a2 = 15, True
# 输出内容：a1+a2=16
print(f'{a1+a2=}')

# 下面a3是int类型，a4是string类型，无法兼容因此执行会报错
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
a3, a4 = 15, '5'
# print(f'{a3+a4=}')
# 我们可以通过强制类型转换，使计算能够执行
# 输出内容：a3+int(a4)=20
print(f'{a3+int(a4)=}')

a5, a6, a7 = 20, [], 10.2
a8, a9, a10 = bool(a5), bool(a6), int(a7)
# 输出内容：a8=True,a9=False,a10=10
print('a8=%s,a9=%s,a10=%s' % (a8, a9, a10))

# 7.python中有以下基本数据类型
# str、number、bool、list、tuple、dict、set
# 其中不可变的数据类型有：str、number、bool、tuple
# 可变的数据类型有：list、dict、set

# 8.python中集合类型的使用总结
#                            list                                           tuple                                               dict                                                set
# 数据结构              有序、可修改列表                                有序、不可修改列表                                    key-value结构                                  无序、不重复的数据集合
# 定义方式              l1=[e1,e2,e3]                                t1=(e1,e2,e3)、t1=e1,e2,e3                          d1={key1:value1,key2:value2}                  s1={e1,e2,e3}、s1=set((e1,e2,e3))
# 访问元素              list[index]、list[start:end]                 tuple[index]、tuple[start:end]                      dict[key]、dict.get(key)                       不支持随机访问，只能用for循环进行遍历
# 增加元素              list.append(e)                                   不支持                                          dict[newKey]=value                             set.add(e)、set.update(e)
# 删除元素              del list[index]                                  不支持                                          del dict[key]                                  set.remove(e)、set.discard(e)、set.pop()
# 更新元素              list[index]=e                                    不支持                                          dict[key]=value                                不支持随机修改某一元素
# 存储数据要求       list中数据可以是任意类型的，且可以是不同类型的       tuple中数据可以是任意类型的，且可以是不同类型的              key必须是不可变类型的数据，value无要求              set中的数据必须是不可变类型的
