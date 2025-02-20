import sys

# 输出内容：
# 即将开始执行try中的代码
# 报错了:ZeroDivisionError division by zero
# 无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行
try:
    print('即将开始执行try中的代码')
    a = 1 / 0
# 可以使用except 异常名 as 变量名的方式，来获取具体的异常对象
except ZeroDivisionError as e:
    print('报错了:ZeroDivisionError', e)
# 如果没有as 变量名，也可以使用sys.exc_info()[0], sys.exc_info()[1]来分别获取当前抛出的异常类型以及异常对象
except ValueError:
    print('报错了:ValueError', sys.exc_info()[0], sys.exc_info()[1])
# 可以使用(异常1,异常2)的方式来在一个except里捕获多种异常
except (TypeError, NameError) as e:
    print('报错了:TypeError或NameError', e)
# 如果不加异常名，则代表捕获除上面这些异常以外的所有异常
except:
    print("抛出的异常跟上面的都匹配不上，就走到这里了:", sys.exc_info()[0], sys.exc_info()[1])
# 如果try中内容正常执行完了，没有抛出异常，则会走到else的部分
else:
    print('try中内容正常处理完了')
# 在try或except执行完毕后，最终都会走到finnaly
finally:
    print('无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行')

# 输出内容：
# 即将开始执行try中的代码
# 报错了:TypeError或NameError test
# 无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行
try:
    print('即将开始执行try中的代码')
    # 可以使用raise关键字来抛出指定类型的异常
    raise TypeError('test')
except ZeroDivisionError as e:
    print('报错了:ZeroDivisionError', e)
except ValueError:
    print('报错了:ValueError')
except (TypeError, NameError) as e:
    print('报错了:TypeError或NameError', e)
finally:
    print('无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行')

# 输出内容：
# 即将开始执行try中的代码
# try中处理逻辑正常
# 当try中代码正常执行完，就会走到else的代码
# 无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行
try:
    print('即将开始执行try中的代码')
    print('try中处理逻辑正常')
except ZeroDivisionError as e:
    print('报错了:ZeroDivisionError', e)
except ValueError:
    print('报错了:ValueError')
except (TypeError, NameError) as e:
    print('报错了:TypeError或NameError', e)
else:
    print('当try中代码正常执行完，就会走到else的代码')
finally:
    print('无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行')

# 输出内容：
# 即将开始执行try中的代码
# 抛出的异常跟上面的都匹配不上，就走到这里了: <class 'NameError'> test
# 无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行，并且是在最后执行
try:
    print('即将开始执行try中的代码')
    raise NameError('test')
except ZeroDivisionError as e:
    print('报错了:ZeroDivisionError', e)
except ValueError:
    print('报错了:ValueError')
except:
    print("抛出的异常跟上面的都匹配不上，就走到这里了:", sys.exc_info()[0], sys.exc_info()[1])
else:
    print('try中内容正常处理完了')
finally:
    print('无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行，并且是在最后执行')

# 最精简的异常处理是try finally，也就是不管有没有异常或不管抛出的是什么异常，都需要在最后执行一些清理内容。
# 输出内容：
# 即将开始执行try中的代码
# 处理代码逻辑
# 无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行，并且是在最后执行
try:
    print('即将开始执行try中的代码')
    print('处理代码逻辑')
finally:
    print('无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行，并且是在最后执行')

# 输出内容：
# 即将开始执行try中的代码
# 发生了TypeError异常，即将把该异常再次往上抛 can only concatenate str (not "int") to str
# 收到了里层抛出的异常
try:
    print('即将开始执行try中的代码')
    try:
        # str类型无法直接和int类型进行加法操作，因此会抛出ypeError异常
        a = '5' + 1
    except TypeError as e:
        print('发生了TypeError异常，即将把该异常再次往上抛', e)
        # 当我们在except中捕获到了异常，我们可以只用raise，直接将捕获到的异常往上抛
        raise
except:
    print('收到了里层抛出的异常')

# 关于try finally的一个细节。假设在try中出异常了，但是没有使用except捕获异常。这样即使finally被执行了，但是因为异常没有被捕获，也会在finally执行完毕后停止程序，而不会继续执行后面的代码。
# 也就是说：只有抛出的异常被捕获了，才能执行后续的代码，否则程序将停止。加上finally只是在停止前执行下finally中的代码。
# 输出内容：
# 先是输出以下内容：
# 即将开始执行try中的代码
# 无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行，并且是在最后执行
# 然后是输出报错，程序结束：
# Traceback (most recent call last):
#   File "/Users/maziqiang/PycharmProjects/HelloPy/异常处理.py", line 123, in <module>
#     raise ValueError('test')
# ValueError: test
try:
    print('即将开始执行try中的代码')
    raise ValueError('test')
finally:
    print('无论如何是在try中执行完，还是在except中执行完，最终都会走到这行，并且是在最后执行，并且是在最后执行')

# 这行因为走不到这儿，所以不会产生任何输出内容
print('程序因为上面的异常没有捕获而停止，走不到这里了')