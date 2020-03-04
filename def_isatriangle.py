# -*- coding: UTF-8 -*-
 
# 定义函数
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

# 调用函数
print(is_triangle(3, 4, 5))