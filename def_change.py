# -*- coding: UTF-8 -*-
 
# 定义函数
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# 调用函数
print(spin_words( "This is another test" ))