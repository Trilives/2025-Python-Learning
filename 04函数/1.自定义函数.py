#自定义函数
def sum(a, b):          #定义函数名称
    "求和函数"           #函数描述
    return a + b        #函数主体
x = y = 1
print(sum(x,y))

#raise主动抛出异常，搭配isinstance
def sum1(a, b):
    "求和函数优化"
    if not(isinstance(a, (int, float)) and isinstance(b, (int, float))):    #当a,b既不是整型也不是浮点数时
        raise TypeError('参数类型错误')                                      #返回类型错误
    return a + b

# ValueError值错误
# TypeError类型错误
# IndexError索引越界
# KeyError字典键不存在
# FileExistsError文件未找到