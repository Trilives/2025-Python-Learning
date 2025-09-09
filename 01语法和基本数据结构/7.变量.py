#Python不需要声明变量
#同一变量可以反复赋值，甚至是不同类型的

x = 2
print(x)
x = 'Trlives'
print(x)

#可以如同链表指针一般变化
a = 'A'
b = a
a = 123

#支持多变量赋值
a = b = 23
x, y, z = 1, 2, '你好'
print(a, b)
print(x, y, z)