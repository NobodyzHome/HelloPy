import random

score = random.randint(1, 100)
if score<60:
    scoreName='不及格'
elif score<=80:
    scoreName = '普通'
elif score<=95:
    scoreName = '优秀'
else:
    scoreName='完美'
# 输出内容：score=100,scoreName='完美'
print(f'{score=},{scoreName=}')

# python 3.10后推出了match语法，类似java中的switch语法
def test_match(s):
    match s:
        # 在case内不用写break，匹配到以后就只走case那部分，不会走后续的case里的内容。这点和java不一样。
        case 1:
            print('当前是1')
        case 2:
            print('当前是2')
        case 3:
            print('当前是3')
        #  可以使用|来给出多个匹配的条件
        case 4 | 5 | 6:
            print('当前在4、5、6之中')
        # case _:就类似于java的default，没有匹配到的走这里
        case _:
            print('没有匹配上的，走default处理逻辑')

# 输出内容：当前是1
test_match(1)
# 输出内容：当前在4、5、6之中
test_match(5)
# 输出内容：没有匹配上的，走default处理逻辑
test_match(8)