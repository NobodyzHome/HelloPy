# with as相当于try finally，只不过finally中要执行的代码不是用户自己提供的，而是执行with创建的对象的__exit__方法。
# 整体执行的顺序是：
# 1.先创建with声明的对象
# 2.执行with中的代码
# 3.不论with内的代码是正常执行完还是抛出了异常，都会触发执行预定义的清理动作

# 创建一个文件对象，并使用变量[f]对其进行引用
with open('/Users/maziqiang/Downloads/waybillcode.txt') as f:
    # 输出内容：开始读取文件，f.closed=False
    print(f'开始读取文件，{f.closed=}')
    readline = f.readline()
    # 执行完这行后，with内的代码就正常执行完了。此后会执行file对象的__exit__方法，进行预定义的清理工作。
    print(readline)

# with as语句后，看看创建的文件对象的状态，确认是否执行了预定义的清理动作。
# 输出内容：f.closed=True
print(f'{f.closed=}')
assert f.closed==True

# with as相当于try finally，也就是说没有进行异常捕获。当with as的上层没有try except时，此时程序会报错，程序结束运行。
# 也就是说with as只是帮我们自动执行最终的清理内容，并不负责捕获异常。
# 输出内容：
# 开始读取文件，f.closed=False
# 捕获到了with as语句抛出的异常
try:
    with open('/Users/maziqiang/Downloads/waybillcode.txt') as f:
        print(f'开始读取文件，{f.closed=}')
        readline = f.readline()
        raise ValueError('test')
except:
    print('捕获到了with as语句抛出的异常')

# with内的代码抛出了异常，由于with as并不会捕获异常，且外层并没有使用try except进行异常捕获，因此在预定义的清理动作执行完毕后会报出异常，并终止程序的运行。
# Traceback (most recent call last):
#   File "/Users/maziqiang/PycharmProjects/HelloPy/with_usage.py", line 41, in <module>
#     raise ValueError('test')
# ValueError: test
with open('/Users/maziqiang/Downloads/waybillcode.txt') as f:
    print(f.closed)
    readline = f.readline()
    raise ValueError('test')