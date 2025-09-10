#经典条件语句，冒号和缩进替代了括号
a = 3
b = 2
if a > b:
    print(a)
else:
    print(b)

#elif == elseif
if b > a:
    print(1)
elif b > 0:
    print(2)
else:
    print(3)

#嵌套
if a > b:
    if a > 0:
        print('a是大于b的正数')
    else:
        print('a是大于b的负数')
else:
    print('a小于b')