#列表
names = ['Yi', 'Er', 'San', 'si', 1234]
print(names)
#打印结果为['Yi', 'Er', 'San', 'si', 1234]

#访问列表中的值
print(names[2])     #注意下标从0开始
print(names[0:2])   #注意范围是[0,2)下标的数据，左闭右开
print(names[:2])    #不指定时默认从0开始

#列表的删除和插入
del(names[2])
print(names)        #仅仅删除对应元素
names.insert(2, 'san')
print(names)        #2是插入的索引位置，对应元素又恢复了

# 语句                          结果                             作用
# len([1, 2, 3])        	    3	                            计算元素个数
# [1, 2, 3] + [4, 5, 6] 	    [1, 2, 3, 4, 5, 6]	            组合
# ['Hi!'] * 4	                ['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制
# 3 in [1, 2, 3]	            True	                        元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3	                        迭代


# 函数&方法	描述
# len(list)	列表元素个数
# max(list)	返回列表元素最大值
# min(list)	返回列表元素最小值
# list(seq)	将元组转换为列表
# list.append(obj)	在列表末尾添加新的对象
# list.count(obj)	统计某个元素在列表中出现的次数
# list.extend(seq)	在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)	从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)	将对象插入列表
# list.pop(obj=list[-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)	移除列表中的一个元素（参数是列表中元素），并且不返回任何值
# list.reverse()	反向列表中元素
# list.sort([func])	对原列表进行排序
