# -*- coding: UTF-8 -*-
 
# 定义函数
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

# 调用函数
print(square_digits(9119))