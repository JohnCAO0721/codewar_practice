# -*- coding: UTF-8 -*-
 
# 定义函数
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

# 调用函数
print(rgb(3, 4, 5))