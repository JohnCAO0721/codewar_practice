# -*- coding: UTF-8 -*-
 
# 定义函数
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

# 调用函数
print(getCount("abscedg"))