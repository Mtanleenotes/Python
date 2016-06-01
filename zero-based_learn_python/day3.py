# coding=utf-8
# 调用sorted排序
# dict = {"a": "apple", "b": "grape", "c": "orange", "d": "banana"}
# print(dict)
# # 按key排序
# print(sorted(dict.items(), key=lambda d: d[0]))
# # 按value排序
# print(sorted(dict.items(), key=lambda d: d[1]))

# 字典的浅拷贝
# dict = {"a": "apple", "b": "grape"}
# dict2 = {"c": "orange", "d": "banana"}
# dict2 = dict.copy()
# print(dict2)

# 字典的深拷贝
# import copy
#
# dict = {"a": "apple", "b": {"g": "grape", "o": "orange"}}
# dict2 = copy.deepcopy(dict)     # 深拷贝
# dict3 = copy.copy(dict)         # 浅拷贝
# dict2["b"]["g"] = "orange"
# print(dict)
# dict3["b"]["g"] = "orange"
# print(dict)

# 索引操作
# tuple = ("apple", "banana", "grape", "orange")
# list = ["apple", "banana", "grape", "orange"]
# str = "apple"
# print(tuple[0])
# print(tuple[-1])
# print(list[0])
# print(list[-1])
# print(str[0])
# print(str[-1])

# 切片操作
# print(tuple[:3])
# print(tuple[3:])
# print(tuple[1:-1])
# print(tuple[:])
#
# print(list[:3])
# print(list[3:])
# print(list[1:-1])
# print(list[:])
#
# print(str[:3])
# print(str[3:])
# print(str[1:-1])
# print(str[:])

# import day4
#
# day4.func()
# myClass = day4.MyClass()
# myClass.myFunc()

import day4
print("count = ", day4.func())
day4.count = 10
print("count = ", day4.count)

import day4
print("count = ", day4.func())


