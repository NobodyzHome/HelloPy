# 推导式可以对一个【可迭代的】对象进行迭代和加工，生成一个新的【可迭代的】对象。
# 当我们需要遍历一个数据集合，并根据遍历数据进行加工，生成一个新的数据集合时，就可以使用推导式。
# 具体生成的新的可迭代对象的类型是什么，取决于推导式左右两边的符号。

# 下面是迭代一个list对象并进行乘2的加工，将加工后的结果生成为一个新的list对象（推导式左右两边使用[]括起来）
list1=[15,20,'hello','world',(True,'test')]
list1_process1 = [x * 2 for x in list1]
# 输出内容：遍历list对象，生成list对象：list1=[15, 20, 'hello', 'world', (True, 'test')],list1_process1=[30, 40, 'hellohello', 'worldworld', (True, 'test', True, 'test')]
print(f'遍历list对象，生成list对象：{list1=},{list1_process1=}')
# 在推导式中，可以增加if条件，过滤出需要的元素，不需要的元素则抛弃
list1_process2 = [x * 1.5 for x in list1 if type(x) == int]
# 输出内容：遍历list对象，过滤出需要的数据，生成list对象：list1=[15, 20, 'hello', 'world', (True, 'test')],list1_process2=[22.5, 30.0]
print(f'遍历list对象，过滤出需要的数据，生成list对象：{list1=},{list1_process2=}')

# 下面是迭代一个dict对象并进行key乘2与value乘3的加工，将加工后的结果生成为一个新的dict对象（推导式左右两边使用{}括起来，并且是key:value的形式）
# 注意：迭代dict对象时，变量x是字典的key，通过dict[x]来获取对应的value
dict1={'hello':'python',21:'test',True:10}
dict1_process1 = {x * 2: dict1[x] * 3 for x in dict1}
# 输出内容：遍历dict对象，生成dict对象：dict1={'hello': 'python', 21: 'test', True: 10},dict1_process1={'hellohello': 'pythonpythonpython', 42: 'testtesttest', 2: 30}
print(f'遍历dict对象，生成dict对象：{dict1=},{dict1_process1=}')

dict1_process2={x*2:dict1[x]*3 for x in dict1 if isinstance(x,str)}
# 输出内容：遍历dict对象，过滤出需要的数据，生成dict对象：dict1={'hello': 'python', 21: 'test', True: 10},dict1_process2={'hellohello': 'pythonpythonpython'}
print(f'遍历dict对象，过滤出需要的数据，生成dict对象：{dict1=},{dict1_process2=}')

# 下面是迭代一个set对象并进行乘2的加工，将加工后的结果生成为一个新的set对象（推导式左右两边使用{}括起来）
s1={12,26,False,19,('hello',28)}
s1_process1 = {x * 2 for x in s1}
# 输出内容：遍历set对象，生成set对象：s1={False, 19, 26, ('hello', 28), 12},s1_process1={0, 38, ('hello', 28, 'hello', 28), 52, 24}
print(f'遍历set对象，生成set对象：{s1=},{s1_process1=}')

s1_process2={x*x for x in s1 if isinstance(x,int) and x<20}
# 输出内容：遍历set对象，过滤出需要的数据，生成set对象：s1={False, 19, 26, ('hello', 28), 12},s1_process2={0, 361, 144}
print(f'遍历set对象，过滤出需要的数据，生成set对象：{s1=},{s1_process2=}')

# 推导式生成的tuple对象，实际是一个生成器对象，需要使用tuple()来将推导结果转换成tuple对象
tuple1='hello','python',15.2,('test','10'),61
tuple1_process1 = (y * 2 for y in tuple1)
# 输出内容：遍历tuple对象，生成tuple对象：tuple1=('hello', 'python', 15.2, ('test', '10'), 61),tuple1_process1=<generator object <genexpr> at 0x100e3aa80>,tuple(tuple1_process1)=('hellohello', 'pythonpython', 30.4, ('test', '10', 'test', '10'), 122)
print(f'遍历tuple对象，生成tuple对象：{tuple1=},{tuple1_process1=},{tuple(tuple1_process1)=}')

tuple1_process2=(x*2 for x in tuple1 if isinstance(x,str))
# 输出内容：遍历tuple对象，过滤出需要的数据，生成tuple对象：tuple1=('hello', 'python', 15.2, ('test', '10'), 61),tuple1_process2=<generator object <genexpr> at 0x1012c1000>,tuple(tuple1_process2)=('hellohello', 'pythonpython')
print(f'遍历tuple对象，过滤出需要的数据，生成tuple对象：{tuple1=},{tuple1_process2=},{tuple(tuple1_process2)=}')

# 推导后生成的对象类型可以和迭代的对象不一致
# 下面是迭代一个list对象，生成一个dict对象的推导式
list2=[19,31,'hello','world',25.1,12.2]
list2_process1={x:x*2 for x in list2 if not isinstance(x,str)}
# 输出内容：遍历list对象，生成dict对象：list2=[19, 31, 'hello', 'world', 25.1, 12.2],list2_process1={19: 38, 31: 62, 25.1: 50.2, 12.2: 24.4}
print(f'遍历list对象，生成dict对象：{list2=},{list2_process1=}')

# 由于推导式生成的对象也是一个【可迭代的】对象，那么使用另一个推导式来迭代一个推导式的结果，来对一个推导式的结果做进一步处理
# 下面使用{x*x for x in s2}这个推导式生成一个数据平方的集合。再对这个集合进行+1的处理，但将小于等于200的过滤掉
s2={10,12,20,23,30,35}
s2_process1={y:y+1 for y in {x*x for x in s2} if y >200}
# 输出内容：推导式后再接推导：s2={35, 20, 23, 10, 12, 30},s2_process1={900: 901, 1225: 1226, 400: 401, 529: 530}
print(f'推导式后再接推导：{s2=},{s2_process1=}')

# 使用案例：将一个html的get请求的参数转换成一个dict对象
# 参数：多个参数用&分隔，每个参数中是key=value的格式
para='type=1&status=0,1&heartBeatCheck=0,1&masterStr=0,1&page=1&rows=10&isNewVersion=true&version=4'
# 1.先用&拆开字符串，形成一个list
# 2.遍历这个list中的元素，加工成dict对象
params = {x.split('=')[0]: x.split('=')[1] for x in para.split('&')}
print(params)