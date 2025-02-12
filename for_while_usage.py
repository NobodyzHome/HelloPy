# for循环语法
# 1.可以遍历任何【可迭代】的对象，包括：string、list、tuple、set、dict等类型都是可迭代的。
# 2.else中的代码是在遍历结束后执行的
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>

# 输出内容：
# h
# e
# l
# l
# o
# _
# w
# o
# r
# l
# d
# 数据遍历完了
for x in 'hello_world':
    print(x)
else:
    print('数据遍历完了')

# range函数
# for循环经常与range函数配合使用。range函数会生成一个range对象，该对象是可迭代的。从start开始迭代，每次执行固定步长，当迭代值>=end时结束迭代。
# range(5)创建一个range对象，从0开始，每次迭代时步长是1，迭代到4(5-1)是最后一次迭代。
# 输出内容：
# 0
# 1
# 2
# 3
# 4
# 数据遍历完了
for x in range(5):
    print(x)
else:
    print('数据遍历完了')

# range(3,10)创建一个range对象，从3开始，每次迭代时步长是1，迭代到9(10-1)是最后一次迭代。
# 输出内容：
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 数据遍历完了
for x in range(3, 10):
    print(x)
else:
    print('数据遍历完了')

# range(2,10,3)创建一个range对象，从2开始，每次迭代时步长是3，迭代到8(2、5、8)是最后一次迭代。
# 输出内容：
# 2
# 5
# 8
# 数据遍历完了
for x in range(2, 10, 3):
    print(x)
else:
    print('数据遍历完了')

# 结合range与列表，可以通过索引位置迭代列表
# 下面实现的是从第0个元素开始遍历，步长为2
# 输出内容：
# x=0,l1[x]=10
# x=2,l1[x]=30
# x=4,l1[x]='world'
# x=6,l1[x]=False
# 数据遍历完了
l1 = [10, 20, 30, 'hello', 'world', (5, 'test'), False]
for x in range(0, len(l1), 2):
    print(f'{x=},{l1[x]=}')
else:
    print('数据遍历完了')

# 下面是实现了从0开始遍历，步长为1，遍历列表
for x in range(len(l1)):
    print(f'{x=},{l1[x]=}')
else:
    print('数据遍历完了')

# while循环语法
# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>

# 输出内容：
# start=0,10
# start=1,20
# start=2,30
# start=3,hello
# start=4,world
# start=5,(5, 'test')
# start=6,False
# 遍历完毕
start, end = 0, len(l1)
while start < end:
    print(f'{start=},{l1[start]}')
    start += 1
else:
    print('遍历完毕')

# 针对break和循环(for和while)中的else
# 如果是通过break结束循环的，是不会走到else的。也就是说：只有在完全遍历完的情况下，才会走else。
# 因此下面代码是不会输出【遍历完毕】的。
# 输出内容：
# x=0,l1[x]=10
# x=1,l1[x]=20
# x=2,l1[x]=30
# x=3,l1[x]='hello'
for x in range(len(l1)):
    if x>3 :
        break

    print(f'{x=},{l1[x]=}')
else:
    print('遍历完毕')

# 输出内容：
# i=0,l1[i]=10
# i=1,l1[i]=20
# i=2,l1[i]=30
# i=3,l1[i]='hello'
i=0
while i<len(l1):
    if i>3:
        break

    print(f'{i=},{l1[i]=}')
    i+=1
else:
    print('遍历完毕')