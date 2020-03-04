# -*- coding: UTF-8 -*-
 
# 定义函数
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# 调用函数
print(xo("xoxos"))