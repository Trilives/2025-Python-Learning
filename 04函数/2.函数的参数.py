#默认参数
def print_user(name, age, health = '健康'):  #如果不特别赋值，默认输入参数为健康
    "对输入的参数分类型打印"
    print('姓名: {}'.format(name), end = ' ')
    print(f"年龄：{age} 健康情况：{health}")
    return
print_user('Trlives', '未知')

#默认参数不能为可变量，否则会混乱
def print_info(a , b = []):     #函数建立时就创建了列表
    print(b)                    #每次调用不会再创建
    return b
result = print_info(1)          #指向的是默认参数
result.append('error')          #修改了默认参数，append：列表新增
print_info(2)                   #此时默认参数已经变成了新值

#关键字调用，可以不按照顺序来，结果是一样的
print_user(age = '未知', name = 'Trlives')

#不定长参数，将后面所有传入的参数都视为同一个（元组）
def print_user2(name, age, *hobby):  #如果不特别赋值，默认输入参数为健康
    "对输入的参数分类型打印"
    print('姓名: {}'.format(name), end = ' ')
    print('年龄: {}'.format(age), end = ' ')
    print('爱好: {}'.format(hobby))
    return
print_user2('Trlives', '未知', '篮球', '乒乓球')

#只接受关键字参数
def print_user3(name, *, age, health = '健康'): # “ * ”后面的参数必须用关键字传入
    "对输入的参数分类型打印"
    print('姓名: {}'.format(name), end = ' ')
    print(f"年龄：{age} 健康情况：{health}")
    return
print_user3('Trlives', age = '未知')

#参数也分为可变和不可变，如同C语言的传入是形参还是指针一样