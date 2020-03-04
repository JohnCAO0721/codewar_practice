# -*- coding: UTF-8 -*-
 
# 定义函数
def array_diff(a, b):
    return [x for x in a if x not in b]

# 调用函数
print(array_diff([1,2],[2]))