# 一个string变量可以用单引号声明
a = 'hello'
# 一个string变量也可以用双引号声明
b = "world"
# 一个string变量也可以用三隐号声明，此时字符串的内容可以跨行
c = """hello
world
everyday
"""
# 输出内容a=hello,b=world,c=hello
# world
# everyday
print('a=%s,b=%s,c=%s' % (a, b, c))

# 一个单变量如果用单引号声明，那字符串中的双引号就被作为普通的字符串
d = 'hello "tom"'
# 反之，一个变量如果用双引号声明，那字符串中的单引号就被作为普通的字符串
e = "hello 'cat'"
# 输出内容：d=hello "tom",e=hello 'cat'
print('d=%s,e=%s' % (d, e))

# 字符串截取
# 字符位置从前往后依次是:0=w,1=e,2=i,3=g,4=h,5=t
# 字符位置从后往前依次是:-1=t,-2=h,-3=g,-4=i,-5=e,-6=w
word = 'weight'
# 我们可以通过word[x:y]的方式来从一个字符串中截取子字符串。x是起始位置，可以是【从前往后】的位置，也可以是【从后往前】的位置。y是结束位置，截取出的字符串不包含y那个位置的字符。
# 输出内容：word[1:3]='ei'
print(f'{word[1:3]=}')
# 输出内容：word[-4:-1]='igh'
print(f'{word[-4:-1]=}')
# 如果不给出x的默认值，那么x的默认值是0。因此word[:-3]相当于word[0:-3]
# 输出内容：word[:-3]='wei'
print(f'{word[:-3]=}')
# 如果不给出y的默认值，那么是截取到字符串的末尾，包含末尾的那个字符。这里有点特殊。因此word[2:]的值是ight，而不是igh。
# 输出内容：word[2:]='ight'
print(f'{word[2:]=}')

# 字符提取
# 输出内容：word[2]='i'
print(f'{word[2]=}')
# 输出内容：word[-3]='g'
print(f'{word[-3]=}')

# 字符串拼接
a, b = 'hello', "world"
# 输出内容：a+' '+b='hello world'
print(f'{a+' '+b=}')

# 字符串重复
# 对字符串做乘法，则可以将字符串重复拼接几次
s1 = 'hello'
# 输出内容：s1=hello,s2=hellohellohellohellohello
print('s1=%s,s1*5=%s' % (s1, s1 * 5))

# 原始字符串
# 在字符串前加上r，那么字符串的内容就是【原始字符串】，不会对字符串中的内容进行任何转义。反之，如果字符串前不加r，会对字符串中的\r、\n、\t等进行转义。
s2, s3 = r'hello\tword', 'hello\tword'
# 输出内容：s2=hello\tword,s3=hello	word
print('s2=%s,s3=%s' % (s2, s3))

# 格式化字符串
# 在一个字符串中可以设置格式化变量，可以使用%来给格式化变量赋值，形成一个新的字符串
s4 = '我是"%s"，我今年%d岁了'
s5 = s4 % ('张三', 20)
# 输出内容：s5='我是"张三"，我今年20岁了'
print(f'{s5=}')
# 输出内容："我是%s,我今年%d岁了"%('李四',25)='我是李四,我今年25岁了'
print(f'{"我是%s,我今年%d岁了"%('李四',25)=}')

# f-string
# f-string用于生成动态执行脚本并执行。我们可以在字符串前加上f，那么字符串中{}外的都是普通字符串，{}里的内容就是要执行的脚本，而不是普通的字符串。
# 脚本中可以访问变量并进行计算
s6 = f'this is {(a + b) * 3}'
# 输出内容：this is helloworldhelloworldhelloworld
print(s6)
# 输出内容：my name is hello
print(f'my name is {a}')

# 我们可以在脚本最后加入=，那么脚本的执行结果中会带着脚本的原始内容
# 输出内容：a+b='helloworld' is a function string result
print(f'{a+b=} is a function string result')
# 输出内容：my name is word[-5:-2]='eig'
print(f'my name is {word[-5:-2]=}')
# 注意：f-string与格式化字符串的区别是
# f-string是变量定义完就开始执行脚本了，因此变量中获取到的是脚本的执行结果。
# f-string变量在被定义出来后，就立即执行了。输出内容：this is a function string,value is 我是"张三"，我今年20岁了
s7 = f'this is a function string,value is {s5}'
print(s7)
# 而格式化字符串是定义了一个格式化模版，通过%才会进行模版值的替换，形成一个新的字符串。
# 格式化字符串的内容是可以被输出出来的。输出内容：this is a format string,value is %s
s8 = f'this is a format string,value is %s'
print(s8)
# 通过%后，才会执行格式化字符串中变量的替换，形成新的字符串。输出内容：this is a format string,value is hellohellohello
print(s8 % (s1 * 3))
