# coding=utf-8

# 创建一个元祖时逗号不能省略
# tuple = ("apple",)
# print(tuple[0])
# print(type(tuple))

# 元祖的访问
# tuple = ("apple", "banana", "grape", "orange")
# print(tuple[-1])
# print(tuple[-2])
# tuple2 = tuple[1:3]
# tuple3 = tuple[0:-2]
# tuple4 = tuple[2:-2]
# print(tuple2)
# print(tuple3)
# print(tuple4)

# 二元元祖
# fruit1 = ("apple", "banana")
# fruit2 = ("grape", "orange")
# tuple = (fruit1, fruit2)
# print(tuple)
# print("tuple[0][1] = ", tuple[0][1])
# print("tuple[1][1] = ", tuple[1][1])
# print("tuple[1][2] = ", tuple[1][2])    # 越界

# 打包
# tuple = ("apple", "banana", "grape", "orange")
# # 解包
# a, b, c, d = tuple
# print(a, b, c, d)

# 二元元祖遍历
# tuple = (("apple", "banana"), ("grape", "orange"), ("watermelon",), ("grapefruit",))
# # for i in range(len(tuple)):
# #     print("tuple[%d]:" % i, tuple[i])
# #     for j in range(len(tuple[i])):
# #         print(tuple[i][j])
#
# for i in tuple:
#     for j in i:
#         print(j)

# 列表
# list = ["apple", "banana", "grape", "orange"]
# print(list)
# print(list[2])
# list.append("watermelon")
# list.insert(1, "grapefruit")
# print(list)
# list.remove("grape")
# print(list)
# # list.remove("a")
# print(list.pop())
# print(list)
# print(list[-2])
# print(list[1:3])
# print(list[-3:-1])
# list = [["apple", "banana"], ["grape", "orange"], ["watermelon"], ["grapefruit"]]
# for i in range(len(list)):
#     print("list[%d]:" % i, list[i])
#     for j in range(len(list[i])):
#         print(list[i][j])

# 列表连接
# list1 = ["apple", "banana"]
# list2 = ["grape", "orange"]
# list1.extend(list2)     # list1连接list2
# print(list1)
# list3 = ["watermelon"]
# list1 = list1 + list3   # 将list1与list3连接后赋给list1
# print(list1)
# list1 += ["grapefruit"]     # 使用+=给list1连接["grapefruit"]
# print(list1)
# list1 = ["apple", "banana"] * 2
# print(list1)

# list = ["apple", "banana", "grape", "orange"]
# # print(list.index("grape"))
# # print(list.index("orange"))
# # print("orange" in list)
# list.sort()
# print("Sorted list:", list)
# list.reverse()
# print("Reversed list:", list)

# 堆栈实现
# list = ["apple", "banana", "grape"]
# list.append("orange")
# print(list)
# print("pop:", list.pop())
# print(list)

# 队列实现
# list = ["apple", "banana", "grape"]
# list.append("orange")
# print(list)
# print("pop:", list.pop(0))
# print(list)

# 字典的添加、删除、修改
# dict = {"a": "apple", "b": "banana", "g": "grape", "o": "orange"}
# dict["w"] = "watermelon"
# print(dict)
#
# del(dict["a"])
# print(dict)
#
# dict["g"] = "grapefruit"
# print(dict)
#
# print(dict.pop("b"))            # 弹出字典中键为b的元素
# print(dict)
#
# dict.clear()                    # 清除字典所有元素
# print(dict)

# for k in dict:
#     print("dict[%s] = " % k, dict[k])

# print(dict.items())

# for (k, v) in dict.items():
#     print "dict[%s] = " % k, v

# 使用列表， 字典作为字典的值
# dict = {"a": ("apple",), "bo": {"b": "banana", "o": "orange"}, "g": ["grape", "grapefruit"]}
# print(dict["a"])
# print(dict["a"][0])
# print(dict["bo"])
# print(dict["bo"]["o"])
# print(dict["g"])
# print(dict["g"][1])
# print(dict.keys())
# print(dict.values())

# dict = {"a": "apple", "b": "banana", "c": "grape", "d": "orange"}
# print(dict)
# print(dict.get("c", "apple"))
# print(dict.get("e", "apple"))       # 使用get获取键为e的值，若不存在返回默认值apple

# update()
# dict = {"a": "apple", "b": "banana"}
# print(dict)
# dict2 = {"c": "grape", "d": "orange"}
# dict.update(dict2)
# print(dict)

# 设置默认值
dict = {}
dict.setdefault("a")
print(dict)
dict["a"] = "apple"
dict.setdefault("a", "None")
print(dict)










