#lambda
sum = lambda num1, num2 : num1 + num2   #引号前面是传入参数，引号后面是返回值
print(sum(1, 2))

#局限性
#引号后只能接单个表达式
#不能使用return，import，raise，while等，if-else要转化为三元表达式
#不能注解传入参数类型，普通函数可以num1：int，表示传入的是int类型
#调试困难，报错不会报函数名

#作用域陷阱
funcs1 = []
for i in range(3):
    funcs1.append(lambda: i)  # 没有传入参数，所有函数都引用同一个变量 i
print([f() for f in funcs1])  # 输出 [2, 2, 2]（非预期结果），f()是函数对象

funcs2 = [lambda i=i: i for i in range(3)]  # 输出 [0, 1, 2]， 对于每个i创建一个函数，默认值为当前的i
print([f() for f in funcs2])