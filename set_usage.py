# 定义集合
# 1.可以使用{}定义集合，但不能使用{}定义一个空集合，此时需要使用set定义空集合
s1= {'hello', 'world', 'hello', 19, (True, 11.7), 30, (True, 11.7)}
# 可以看到，重复的内容被删除了
# 输出内容：s1={'world', 'hello', 19, 30, (True, 11.7)}
print(f'{s1=}')
# 2.也可以使用set定义集合
s2=set((19.7,'hello','world','hello',19.7))
# 输出内容：s2={'world', 19.7, 'hello'}
print(f'{s2=}')

# 无法随机访问元素
# 集合是无序的，不重复的数据结构。因此无法使用索引位置来从集合中获取元素。

# 添加元素
# 1.add
s2.add(20)
s2.add('hello')
# 输出内容：add后,s2={'hello', 19.7, 20, 'world'}
print(f'add后,{s2=}')

# 2.update.可以一次向set添加多个元素
# 输出内容：update后,s2={40, 'hello', 19.7, 20, 30, 'world'}
s2.update([30,40,'hello'],[40,'world'])
print(f'update后,{s2=}')

# 移除元素
# 1.remove。移除指定元素，如果不存在则报错。
s2.remove(19.7)
# 输出内容：remove后，s2={40, 'hello', 20, 30, 'world'}
print(f'remove后，{s2=}')
# 2.discard。移除指定元素，不存在也不会报错。
s2.discard('test')
# 输出内容：discard后，s2={40, 'hello', 20, 30, 'world'}
print(f'discard后，{s2=}')
# 3.pop。从集合中拿取一个元素，并删除。注意：由于set是无序的，因此每次拿取的顺序是随机的，不是固定的。
x = s2.pop()
# 输出内容：pop后，x=40,s2={'hello', 20, 30, 'world'}
print(f'pop后，{x=},{s2=}')

# 判断元素在集群中是否存在
# 输出内容：s2={'world', 'hello'},20 in s2=False
print(f'{s2=},{20 in s2=}')
# 输出内容：s2={'world', 'hello'},'world' in s2=True
print(f'{s2=},{'world' in s2=}')

# 遍历set中的元素
# 输出内容：
# x='hello'
# x=20
# x=30
# x='world'
for x in s2:
    print(f'{x=}')

# set中只能存放不可变元素
# 原因应该是set底层复用的dict，将集合中的元素存储到dict的key。由于dict要求key必须是不可变的，那么set中的元素自然也就必须是不可变的。
# 因此下面这些都是可以的
s3=set()
s3.add('hello')
s3.add((15,'test'))
# 输出内容：s3={(15, 'test'), 'hello'}
print(f'{s3=}')
# 而下面这几个执行时都会报错
# 报错内容：unhashable type: 'list'
s3.add([20,'world'])
# 报错内容：unhashable type: 'dict'
s3.add({'hello':'world'})