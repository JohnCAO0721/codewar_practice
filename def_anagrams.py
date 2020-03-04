# -*- coding: UTF-8 -*-
 
# 定义函数
def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]

# 调用函数
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))