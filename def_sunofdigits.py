# -*- coding: UTF-8 -*-
 
# 定义函数
def digital_root(n):
    return n%9 or n and 9 

# 调用函数
print(digital_root(16))