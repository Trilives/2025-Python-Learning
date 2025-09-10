#Set，无序不重复元素集
set1 = set([1, 2, 3, 2])   #需要一个列表作为接口传入数据
print(set1)             #输出的是无序的list内部的元素,重复元素自动过滤

#添加元素
set1.add(5)
print(set1)

#删除元素

set1.remove(1)
print(set1)

#运算
set2 = set([1, 4, 2])
print(set2 & set1)          #交集
print(set1 - set2)          #差集
print(set1 | set2)          #并集

#操作
list1 = [12, 1, 2, 54, 1, 54, 6]
print(set(list1))           #去重