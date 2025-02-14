# 定义函数时，可以定义以下类型的参数：
# 1.必须参数
# 2.默认参数
# 3.不定长参数。其中不定长参数包含*arg形式的(使用tuple存储)以及**arg形式(使用dict存储)的参数。
# 入参函数时，有以下两种方式：
# 1.位置形式：按照函数定义参数的顺序，对参数进行赋值。
# 2.关键字形式：按照函数定义参数的名称，对参数进行赋值。

# 定义一个函数，定义了两个必要参数
def fun_must_param(must_param1, must_param2):
    print(f'{must_param1+must_param2=}')

# 调用函数：
# 1.必须参数是必须要赋值的。
# 2.可以使用位置形式进行赋值，也可以使用关键字形式赋值，也可以混用。但按位置赋值时，一定主要好赋值的顺序和函数中参数定义的顺序一致。
# 输出内容：must_param1+must_param2=66.9
fun_must_param(15.2, must_param2=51.7)

# 定义一个函数，拥有两个必须参数和一个默认参数
def fun_default_param(must_param1, must_param2, default_param1=30):
    return must_param1 * must_param2 + default_param1

# 在调用函数时，默认参数可以不赋值，此时默认参数的值用的是默认值
fun_default_param_rst1 = fun_default_param(10, 2)
# 输出内容：fun_default_param_rst1=50
print(f'{fun_default_param_rst1=}')

# 在调用函数时，也可以给默认参数复赋值，来覆盖默认参数的值
fun_default_param_rst2 = fun_default_param(21, 3, 50)
# 输出内容：fun_default_param_rst2=113
print(f'{fun_default_param_rst2=}')

# 定义一个函数，拥有一个必须参数和一个不定长参数。不定长参数会以tuple结构存储。
def fun_multi_param1(must_param1, *multi_param):
    print(f'{type(multi_param)=}')
    return must_param1 * sum(multi_param)

# 在下面调用中，10是通过位置形式赋值给must_param1，其余参数都是复制给multi_param，以tuple形式存储
fun_multi_param1_rst1 = fun_multi_param1(10, 2, 3, 5, 11, 27,20)
# 输出内容fun_multi_param1_rst1=680
print(f'{fun_multi_param1_rst1=}')

# 也可以不给可变长参数传入任何入参，这样multi_param被赋值的就是一个空tuple
fun_multi_param1_rst2 = fun_multi_param1(50)
# 输出内容：fun_multi_param1_rst2=0（因为是个空tuple，所以sum(multi_param)=0，得到的结果自然也是0）
print(f'{fun_multi_param1_rst2=}')

# 可变长字段可以定义在参数列表中间，但是在调用赋值时，可变长参数后面的参数只能使用关键字形式赋值。
def fun_multi_param2(must_param1, *multi_param, must_param2, must_param3):
    print(f'{must_param1+sum(multi_param)+must_param2+must_param3=}')

# 在函数定义时，must_param2和must_param3在可变长参数multi_param的后面，那么这两个在调用时，只能通过关键字形式来赋值。
# 输出内容：must_param1+sum(multi_param)+must_param2+must_param3=105
fun_multi_param2(10, 1, 2, 3, 4, 5, must_param2=30, must_param3=50)

# 定义一个函数，拥有一个必须参数、两个default参数和一个dict格式的不定长参数。
def fun_multi_dict_param(must_param1, default_param1=20, default_param2=30, **multi_dict_param):
    print(f'{type(multi_dict_param)}')
    return must_param1 + default_param1 + default_param2 + (multi_dict_param.get('end',0) - multi_dict_param.get('start',0))

# 在调用此函数：
# 1.使用位置形式给must_param1、default_param1参数赋值的。
# 2.default_param2没有赋值，因此走默认值。
# 3.通过关键字形式，给dict形式的可变长字段multi_dict_param赋值。字段名是dict的key（在这里是start、end），字段值是dict的value（在这里是19、51）。
fun_multi_dict_param_rst1 = fun_multi_dict_param(15, 22, start=19, end=51)
# 输出内容：fun_multi_dict_param_rst1=99
print(f'{fun_multi_dict_param_rst1=}')

# 也可以不给multi_dict_param传入任何入参
# 但注意的是：函数定义时，获取dict的值应使用get的方式并给出默认值，而不是dict[key]的方式。避免获取不到dict的key而导致程序报错。
fun_multi_dict_param_rst2 = fun_multi_dict_param(20, 50)
# 输出内容：fun_multi_dict_param_rst2=100
print(f'{fun_multi_dict_param_rst2=}')