#for
for i in 'ab':
    print(i)        #i代表目标中的元素
for i in {'Q':'1', 'W':'2'}:
    print(i)        #对于字典，只打印键（标签）
#所以，不能将目标设置成数，要设置成一个范围

#range
for i in range(0, 10, 2):
    print(i)        #range(0, 10, 2)，表示0~10这个范围，步进为2
for i in range(5):
    print(i)        #默认从0开始，步进为1

#while没有多少改变
a = 0
while a < 100:
    print(a)
    a += 20

#嵌套循环
for i in range(0, 10, 2):
    for j in range(5):
        print(i, j)