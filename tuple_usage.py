# tuple类似list，但有以下不同
# 1.tuple使用()来定义元素，list使用[]来定义元素
# 2.tuple中元素是不可以被修改的，但list中的元素可以被修改

# 定义tuple
# 注意：由于括号除了用于定义元组，还用来作为计算的括号使用，并且当作括号使用的优先级比定义元组要高。因此(1)实际定义的是一个int值，而不是元组
tuple1 = (1)
# 输出内容：type(tuple1)=<class 'int'>,tuple1=1
print(f'{type(tuple1)=},{tuple1=}')
# 如果想定义一个只有一个元素的元祖，可以使用以下方式
# 输出内容：type(tuple2)=<class 'tuple'>,tuple2=(2,)
tuple2 = (2,)
print(f'{type(tuple2)=},{tuple2=}')
# 还可以不使用括号来定义一个元祖
tuple3 = 'hello', 15, 'world', 22, True
# 输出内容：type(tuple3)=<class 'tuple'>,tuple3=('hello', 15, 'world', 22, True)
print(f'{type(tuple3)=},{tuple3=}')

# 获取元组中指定位置的元素
# 输出内容：tuple3=('hello', 15, 'world', 22, True),tuple3[-2]=22
print(f'{tuple3=},{tuple3[-2]=}')

# 从一个tuple中截取子tuple
# 虽然tuple不可以被修改，但是可以从一个tuple中进行截取，截取出一个新的子tuple
# 输出内容：tuple3=('hello', 15, 'world', 22, True),tuple3[1:-2]=(15, 'world')
print(f'{tuple3=},{tuple3[1:-2]=}')

# 元祖拼接
# 和list一样，元祖也可以使用+进行两个元祖的拼接，形成一个新的元祖
tuple5 = 'hello', 'world'
tuple6 = 19, 'python'
# 输出内容：tuple5=('hello', 'world'),tuple6=(19, 'python'),tuple5+tuple6=('hello', 'world', 19, 'python')
print(f'{tuple5=},{tuple6=},{tuple5+tuple6=}')

# 元祖重复
# 输出内容：tuple5=('hello', 'world'),tuple5*3=('hello', 'world', 'hello', 'world', 'hello', 'world')
print(f'{tuple5=},{tuple5*3=}')

# 判断指定元素在元祖中是否存在
# 输出内容："hello" in tuple5=True
print(f'{"hello" in tuple5=}')

# 遍历元祖
# 输出内容
# x='hello'
# x='world'
for x in tuple5:
    print(f'{x=}')

# 尝试修改tuple中的元素，会报以下错误：'tuple' object does not support item assignment
tuple5[0]='hi'