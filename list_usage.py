import operator
from operator import eq

# 定义list
# 1.使用[]定义list，list中的元素使用【,】分割
# 2.list中数据的类型可以是不同的
l1 = [1, 2, 'hello', 'world', 15.3]
# 输出内容：l1=[1, 2, 'hello', 'world', 15.3]
print(f'{l1=}')

# 访问list中的某个位置的值
# 输出内容：l1[1]=2
print(f'{l1[1]=}')
# 输出内容：l1[3]='world'
print(f'{l1[3]=}')
# 输出内容：l1[-1]=15.3
print(f'{l1[-1]=}')
# 输出内容：l1[-3]='hello'
print(f'{l1[-3]=}')

# 截取子list
# 输出内容：l1[1:4]=[2, 'hello', 'world']
print(f'{l1[1:4]=}')
# 输出内容：l1[-4:3]=[2, 'hello']
print(f'{l1[-4:3]=}')
# 如果没给出:左边的参数，则会给默认值0
# 输出内容：l1[:3]=[1, 2, 'hello']
print(f'{l1[:3]=}')
# 如果没给出:右边的参数，则是默认截到list的结尾，包含最后一个元素。
# 输出内容：l1[2:]=['hello', 'world', 15.3]
print(f'{l1[2:]=}')
# 因此如果:左右两边的参数都没给出，就是获取列表中的全部元素
# 输出内容：l1[:]=[1, 2, 'hello', 'world', 15.3]
print(f'{l1[:]=}')

# 列表中新增元素
l1.append(True)
l1.append(15)
# 输出内容：向列表中添加元素后，列表中的内容：l1=[1, 2, 'hello', 'world', 15.3, True, 15]
print(f'向列表中添加元素后，列表中的内容：{l1=}')

# 更新列表中的元素
tmp = l1[1]
l1[1] += 3
# 输出内容：修改前l1[1]=2,修改后l1[1]=5
print('修改前l1[1]=%s,修改后l1[1]=%s' % (tmp, l1[1]))

# 删除列表中的元素
# py会将指定位置的元素删除，然后后续元素的位置依次往前提一格
# 输出内容：删除元素前，列表的内容是[1, 5, 'hello', 'world', 15.3, True, 15]，要删除的元素是hello
print('删除元素前，列表的内容是%s，要删除的元素是%s' % (l1, l1[2]))
del l1[2]
# 输出内容：删除元素后，列表的内容是[1, 5, 'world', 15.3, True, 15]，l1[2]=world
print('删除元素后，列表的内容是%s，l1[2]=%s' % (l1, l1[2]))

# 列表长度
# 输出内容：len(l1)=6
print(f'{len(l1)=}')

# 列表拼接
# 可以对两个list进行+操作，这样会形成一个新的list，将两个list的内容拼接在一起
l2=[19,'python']
# 输出内容：l1=[1, 5, 'world', 15.3, True, 15],l2=[19, 'python'],l1+l2=[1, 5, 'world', 15.3, True, 15, 19, 'python']
print(f'{l1=},{l2=},{l1+l2=}')

# 列表重复
# 可以对一个list进行*操作，这样会形成一个新的list。list中的内容是原list中的内容重复N遍。
# 输出内容：l2=[19, 'python'],l2*3=[19, 'python', 19, 'python', 19, 'python']
print(f'{l2=},{l2*3=}')

# 判断元素是否存在于列表中
# 输出内容："python"存在于列表[19, 'python']中
if 'python' in l2:
    print('"python"存在于列表%s中' % l2)
else:
    print('"python"不存在于列表%s中' % l2)

# 遍历列表
# 输出内容：
# x=19
# x='python'
for x in l2:
    print(f'{x=}')

# 判断两个列表中元素是否相同，需要引用operator模块的eq方法
l3=[19,'python']
# 输出内容：l2=[19, 'python'],l3=[19, 'python'],operator.eq(l2,l3)=True
print(f'{l2=},{l3=},{operator.eq(l2,l3)=}')
# 输出内容：l2=[19, 'python'],l1=[1, 5, 'world', 15.3, True, 15],operator.eq(l2,l1)=False
print(f'{l2=},{l1=},{operator.eq(l2,l1)=}')