# coding=utf-8
# if __name__ == '__main__':
#     print("hello world")


# class Student:                      # 类名大写
#     __name = ""                     # 私有实例变量前必须有两个下划线
#
#     def __init__(self, name):
#         self.__name = name          # self相当于java中this
#
#     def get_name(self):
#         return self.__name
#
# if __name__ == '__main__':
#     student = Student("sun")        # 对象名小写
#     print(student.get_name())

# import random
#
#
# def compare_num(num1, num2):
#     if num1 > num2:                   # if后面没有括号
#         return 1
#     elif num1 == num2:
#         return 0
#     else:
#         return -1
# num1 = random.randrange(1, 9)
# num2 = random.randrange(1, 9)
# print("num1 =", num1)
# print("num2 =", num2)
# print(compare_num(num1, num2))

# x = 1
# if x == 1:
#     print("x = ", x)
# else:
#     print("x = ", x)
# x = x + 1
# print("x = ", x)

# import sys            # 在当前程序的命名空间中创建导入模块的引用
#
#
# print(sys.path)
# print(sys.argv)


# from sys import path    # 导入模块中一部分内容，并在当前的命名空间中创建导入对象的引用
# from sys import argv
# # 这种写法不够规范，如果程序复杂，导入很多模块，阅读程序的人并不了解path，argv来自哪个模块
#
# print(path)
# print(argv)

# 字符串的换行
# 写法一
# sql = "select id,name " \
#       "from dept " \
#       "where name = 'a'"
# print(sql)
#
# # 写法二
# sql2 = "select id,name \
#       from dept \
#       where name = 'a'"
# print(sql2)

# 一次新的赋值操作，将创建一个新的变量
# x = 1
# print(id(1))
# x = 2
# print(id(x))

# 给多个变量赋值
# a = (1, 2, 3)
# (x, y, z) = a
# print x, y, z

# 在文件的开头定义全局变量
# _a = 1
# _b = 2


# def add():
#     global _a           # global用于引用全局变量
#     _a = 3              # 对全局变量_a重新赋值
#     return "_a + _b = ", _a + _b
#
#
# def sub():
#     global _b
#     _b = 4
#     return "_a - _b = ", _a - _b
#
# print(add())
# print(sub())

# def add():
#     _a = 3              # _a不是前面定义的全局变量
#     return "_a + _b = ", _a + _b
#
#
# def sub():
#     _b = 4
#     return "_a - _b = ", _a - _b
#
# print(add())
# print(sub())
# 变量名相同的两个变量可能并不是同一个变量，变量的名称只是起标志的作用

# 调用全局变量
# import gl
#
#
# def fun():
#     print(gl._a)
#     print(gl._b)
# fun()

# 整型
# i = 1
# print(type(i))
# # 长整型
# l = 999999999999999990
# print(type(l))
# # 浮点型
# f = 1.2
# print(type(f))
# b = True
# print(type(b))
# # 复数类型,注意是j
# c = 7 + 8j
# print(type(c))

# 单引号和双引号的使用等价
# str = "hello world"
# print(str)
# str = 'hello world'
# print(str)

# 三引号的用法
# str = '''he say "hello world!"'''
# print(str)

# 三引号制作doc文档
# class Hello:
#     '''hello class'''
#     def printHello():
#         '''print hello world'''
#         print ("hello world!")
# print(Hello.__doc__)
# print(Hello.printHello.__doc__)

# 转义字符
# str = 'he say:\'hello world!\''
# print(str)
# 直接输出特殊字符
# str = "he say:'hello world!'"
# print(str)
# str = '''he say:'hello world!' '''     # 最后一个单引号后面留有一个空格
# print(str)

# print("1 / 2 = ", 1 / 2.0)
# print("2 ** 3 = ", 2 ** 3)

# 关系表达式
# print(2 > 1)
# print(1 <= 2)
# print(1 == 2)
# print(1 != 2)

# 逻辑表达式
# print(not True)
# print(False and True)
# print(True and False)
# print(True or False)

# x = input("x:")
# # x = int(x)
# x = x + 1
# print(x)

# 使用字典实现switch语句
# from __future__ import division     # 导入精确除法
# x = 1
# y = 2
# operator = '/'
# result = {
#     "+": x + y,
#     "-": x - y,
#     "*": x * y,
#     "/": x / y
# }
# print(result.get(operator))

# class Switch(object):
#     def __init__(self, value):
#         self.value = value
#         self.fall = False
#
#     def __iter__(self):
#         yield self.match
#         raise StopIteration
#
#     def match(self, *args):
#         if self.fall or not args:
#             return True
#         elif self.value in args:
#             self.fall = True
#             return True
#         else:
#             return False
#
# operator = "/"
# x = 1
# y = 2
# for case in Switch(operator):       # Switch只能用于for in循环中
#     if case('+'):
#         print(x + y)
#         break
#     if case('-'):
#         print(x - y)
#         break
#     if case('*'):
#         print(x * y)
#         break
#     if case('/'):
#         print(x / y)
#         break
#     if case():      # 默认分支
#         print ""

# while循环
# numbers = input("输入几个数字，用逗号分隔：").split(",")
# print(numbers)
# x = 0
# while x < len(numbers):
#     print(numbers[x])
#     x += 1

# 带else子句的while循环
# x = float(input("输入x的值："))
# i = 0
# while x != 0:
#     if x > 0:
#         x -= 1
#     else:
#         x += 1
#     i = i + 1
#     print("第%d次循环:" % i)
# else:
#     print("x等于0", x)

# for in 语句
# for x in range(-1, 2):
#     if x > 0:
#         print("+:", x)
#     elif x == 0:
#         print("0:", x)
#     else:
#         print("-:", x)
# else:
#     print("循环结束")

# break
# x = int(input("输入x的值:"))
# y = 0
# for y in range(0, 100):
#     if x == y:
#         print("find number:", x)
#         break
# else:
#     print("not find")

# continue
# x = 0
# for i in [1, 2, 3, 4, 5]:
#     if x == i:
#         continue
#     x += i
# print("x = ", x)

# 冒泡排序
# def bubble_sort(numbers):
#     for j in range(len(numbers) - 1, -1, -1):
#         for i in range(j):
#             if numbers[i] > numbers[i+1]:
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#             print(numbers)
#
# if __name__ == "__main__":
#     numbers = [23, 12, 9, 15, 6]
#     bubble_sort(numbers)












