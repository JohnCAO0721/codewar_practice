# -*- coding: UTF-8 -*-
 
# 定义函数
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

# 调用函数
print(persistence(39))