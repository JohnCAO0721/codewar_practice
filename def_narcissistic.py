# -*- coding: UTF-8 -*-
 
# 定义函数
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

# 调用函数
print(narcissistic(1634))