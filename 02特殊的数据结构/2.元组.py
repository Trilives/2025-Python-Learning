##元组内部的元素不可修改

tuple1 = (123,'Hello')  #使用括号定义，元素之间隔开
tuple2 = 123,'Hello'    #可以不用括号
tuple3 = 123,           #必须要有逗号
tuple4 = ()             #空元组
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)


print(tuple1[1])        #通过下标访问元组

#元组的元素不能修改，但是元素内部的值可以修改
list1 = ['q', 'w']
tuple5 = (list1, '23', 'Hello')
list1[1] = 'e'
print(tuple5)

#元组只能整个删除

del(tuple1)

# 方法	描述
# len(tuple)	计算元组元素个数
# max(tuple)	返回元组中元素最大值
# min(tuple)	返回元组中元素最小值
# tuple(seq)	将列表转换为元组

# len((1, 2, 3))	        3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	    (1, 2, 3, 4, 5, 6)	连接
# ('Hi!',) * 4	            ('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	        True	元素是否存在
# for x in (1, 2, 3): print(x)	1 2 3	迭代