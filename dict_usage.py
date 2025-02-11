# 定义dict
dict1 = {'hello': 'world', 19: 'zhang san', 'l1': [10, 30, 'hi', False]}
# 输出内容：dict1={'hello': 'world', 19: 'zhang san', 'l1': [10, 30, 'hi', False]}
print(f'{dict1=}')
# 定义一个空字典
tmp={}

# 获取dict中的元素
# 1.使用[]的方式。注意：此时需要指定的key在字典中必须存在。
e1 = dict1['hello']
# 输出内容：dict1[hello]=world
print(f'dict1[hello]={e1}')
# 下面尝试从字典中获取一个不存在的key，则会报错：KeyError: 'nobody'
# e2=dict1['nobody']
# 2.使用字典对象.get的方式
# 输出内容：dict1.get('hello')='world'
print(f"{dict1.get('hello')=}")
# 使用get方式从字典中获取一个没有的key，则会返回None对象
# 输出内容：dict1.get('nobody')=None,type(dict1.get('nobody'))=<class 'NoneType'>
print(f"{dict1.get('nobody')=},{type(dict1.get('nobody'))=}")
# 我们还可以使用get方法加一个默认值入参，当要找的key不存在，则返回指定的默认值
# 输出内容：.get('nobody','there is no match key')='there is no match key'
print(f"{dict1.get('nobody','there is no match key')=}")

# 修改dict中的元素
# dict是可变的，可以被添加、修改和删除元素
# 输出内容：修改前：dict1['hello']='world'
print(f"修改前：{dict1['hello']=}")
dict1['hello'] = 'python'
# 输出内容：修改后：dict1['hello']='python',dict1={'hello': 'python', 19: 'zhang san', 'l1': [10, 30, 'hi', False]}
print(f"修改后：{dict1['hello']=},{dict1=}")

# 删除dict中的元素
# 输出内容：删除l1前：dict1={'hello': 'python', 19: 'zhang san', 'l1': [10, 30, 'hi', False]}
print(f"删除l1前：{dict1=}")
del dict1['l1']
# 输出内容：删除l1后：dict1={'hello': 'python', 19: 'zhang san'}
print(f"删除l1后：{dict1=}")

# 向dict中添加元素
print(f"添加前：{dict1=}")
# 输出内容：添加前：dict1={'hello': 'python', 19: 'zhang san'}
dict1[True]=(50,'test')
# 输出内容：添加后：dict1={'hello': 'python', 19: 'zhang san', True: (50, 'test')}
print(f"添加后：{dict1=}")

# dict中对key的要求是不可变的值。因此string、int、tuple都可以，但list不行，因为可以修改list中的元素。
# 因此以下三个都是可以的
dict2 = {'hello': 'world'}
dict3 = {15.3: 23}
dict4 = {(15, 'test'): 19}
# 但是下面则会报错：unhashable type: 'list'
# dict5 = {[1, 2]: 15}

# dict中对value没有要求，因此value可以是任意类型
# 因此下面这些value都是可以的
dict6 = {'hello': [15, 'world']}
dict7 = {True: 'test'}
dict8 = {19: ('hello', 'world')}
dict9 = {(29, False): 19}
dict10 = {'no': False}

# 判断指定key是否在字典中存在
# 输出内容：dict6={'hello': [15, 'world']},"hello" in dict6=True
print(f'{dict6=},{"hello" in dict6=}')
# 输出内容：dict6={'hello': [15, 'world']},"world" in dict6=False
print(f'{dict6=},{"world" in dict6=}')

# 遍历一个dict。会将字典的key赋值给遍历的变量
# 输出内容
# key=hello,value=python
# key=19,value=zhang san
for x in dict1:
    print('key=%s,value=%s' % (x, dict1[x]))
