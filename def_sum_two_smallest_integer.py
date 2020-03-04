# -*- coding: UTF-8 -*-
 
# 定义函数
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# 调用函数
print(sum_two_smallest_numbers([1, 10, 15, 12, 2]))