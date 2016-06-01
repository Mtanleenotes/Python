# coding=utf-8
# return返回多个值,将这些值“打包”到元组中


# def func(x, y, z):
#     l = [x, y, z]
#     l.reverse()
#     numbers = tuple(l)
#     return numbers

# 法二
# def func(x, y, z):
#     l = [x, y, z]
#     l.reverse()
#     a, b, c = tuple(l)
#     return a, b, c
#
# x, y, z = func(0, 1, 2)
# print(x, y, z)

# 多个return语句的重构
# def func(x):
#     if x > 0:
#         result = "x > 0"
#     elif x == 0:
#         result = "x == 0"
#     else:
#         result = "x < 0"
#     return result
# print(func(-2))

# 嵌套函数
# def sum(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def func():
#     x = 1
#     y = 2
#     m = 3
#     n = 4
#     return sum(x, y) * sub(m, n)
# print(func())

# def func():
#     x = 1
#     y = 2
#     m = 3
#     n = 4
#
#     def sum(a, b):      # 内部函数
#         return a + b
#
#     def sub(a, b):
#         return a - b
#     return sum(x, y) * sub(m, n)
# print(func())

# def func():
#     x = 1
#     y = 2
#     m = 3
#     n = 4
#
#     def sum():      # 内部函数,直接调用外部函数的变量
#         return x + y
#
#     def sub():
#         return m - n
#     return sum() * sub()
# print(func())

# 计算阶乘
# def refunc(n):
#     i = 1
#     if n > 1:                   # 递归结束判断
#         i = n
#         n = n * refunc(n-1)
#     print "%d! = " % i, n
#     return n
# refunc(5)

# 使用reduce计算阶乘
# from functools import reduce
# print "5! = ", reduce(lambda x, y: x * y, range(1, 6))

# lambda
# def func():
#     x = 1
#     y = 2
#     m = 3
#     n = 4
#     sum = lambda x, y: x + y
#     print(sum)
#     sub = lambda x, y: x - y
#     print(sub)
#     return sum(x, y) * sub(m, n)
# print(func())

# 定义Generator函数
# def func(n):
#     for i in range(n):
#         yield i
# # 在for循环中输出
# for i in func(3):
#     print(i)
# # 使用next输出
# r = func(3)
# print(r.next())
# print(r.next())
# print(r.next())

# return和yield区别
# def func(n):
#     for i in range(n):
#         return i
#
#
# def func2(n):
#     for i in range(n):
#         yield i
#
# print(func(3))
# f = func2(3)
# print(f)        # 返回函数地址
# print(f.next())
# print(f.next())

# 格式化字符串
# str1 = "version"
# num = 1.0
# format = "%s" % str1
# print(format)
# format = "%s %d" % (str1, num)
# print(format)

# 带精度的格式化
# print "浮点型数字：%f" % 1.25
# print "浮点型数字：%.1f" % 1.25
# print "浮点型数字：%.2f" % 1.254

# 使用字典格式化字符串
# print "%(version)s:%(num).1f" % {"version": "version", "num": 2}

# 字符串对齐
# word = "version3.0"
# print(word.center(20))
# print(word.center(20, "*"))
# print(word.ljust(0))
# print(word.rjust(20))
# print("%30s" % word)

# 输出转义字符
# path = "hello\tworld\n"
# print(path)
# print(len(path))
# path = r"hello\tworld\n"
# print(path)
# print(len(path))

# strip()去掉转义符
# word = "\thello world\n"
# print "直接输出：", word
# print "strip()后输出:", word.strip()
# print "lstrip()后输出：", word.lstrip()     # 去掉前面转义字符
# print "rstrip()后输出：", word.rstrip()     # 去掉后面转义字符

# 使用+连接字符串
# str1 = "hello "
# str2 = "world "
# str3 = "hello "
# str4 = "China"
# result = str1 + str2 + str3
# result += str4
# print(result)

# 使用join()连接字符串
# strs = ["hello ", "world ", "hello ", "China"]
# result = "".join(strs)
# print(result)

# 使用reduce()连接字符串
# from functools import reduce
# import operator
# strs = ["hello ", "world ", "hello ", "China"]
# result = reduce(operator.add, strs, "")
# print(result)

# 使用索引截取子串
# word = "world"
# print(word[4])

# 使用切片截取子串
# str1 = "hello world"
# print(str1[0:3])
# print(str1[::2])
# print(str1[1::2])

# 使用split()获取子串
# split([char] [,num])
# char表示用于分割的字符，默认分割字符时空格
# num表示分割的次数，如果num=2，将源字符分割为3个子串，默认情况下，将根据字符char在字符中出现的个数分割子串
# sentence = "Bob said:1, 2, 3, 4"
# print "使用空格取子串：", sentence.split()
# print "使用逗号取子串：", sentence.split(",")
# print "使用两个逗号取子串：", sentence.split(",", 2)

# 字符串连接后，python将分配新的空间给连接后的字符串，源字符串保持不变
# str1 = "a"
# print(id(str1))
# print(id(str1 + "b"))

# 字符串的比较
# str1 = 1
# str2 = "1"
# if str1 == str2:
#     print("相同")
# else:
#     print("不相同")
# if str(str1) == str2:
#     print("相同")
# else:
#     print("不相同")

# 比较字符串的开始和结束处
# word = "hello world"
# print("hello" == word[0:5])
# print(word.startswith("hello"))
# print(word.endswith("ld", 6))
# print(word.endswith("ld", 6, 10))
# print(word.endswith("ld", 6, len(word)))

# 循环输出反转的字符串
# def reverse(s):
#     out = ""
#     li = list(s)
#     for i in range(len(li), 0, -1):
#         out += "".join(li[i-1])
#     return out

# 使用list的reverse()
# def reverse(s):
#     li = list(s)
#     li.reverse()
#     s = "".join(li)
#     return s

# 使用切片
# def reverse(s):
#     return s[::-1]
#
# print(reverse("hello"))

# 查找字符串
# sentence = "This is a apple."
# print(sentence.find("a"))
# print(sentence.rfind("a"))

# 字符串的替换
# replace(old, new [,max])
# sentence = "hello world, hello China"
# print(sentence.replace("hello", "hi"))
# print(sentence.replace("hello", "hi", 1))
# print(sentence.replace("abc", "hi"))

# import time, datetime
# # 时间到字符串转换
# print(time.strftime("%Y-%m-%d %X", time.localtime()))
# # 字符串到时间的转换
# t = time.strptime("2008-08-08", "%Y-%m-%d")
# y, m, d = t[0:3]
# print(datetime.datetime(y, m, d))

import re
# # ^与$的使用
# s = "HELLO WORLD"
# print(re.findall(r"^hello", s))
# print(re.findall(r"^hello", s, re.I))
# print(re.findall("WORLD$", s))
# print(re.findall(r"WORLD$", s, re.I))
# print(re.findall(r"\b\w+\b", s))

# sub()先创建变量s的拷贝，然后在拷贝中替换字符串，并不会改变变量s的内容
# s = "hello world"
# print(re.sub("hello", "hi", s))
# print(re.sub("hello", "hi", s[-4:]))
# print(re.sub("world", "China", s[-5:]))

# 特殊字符的使用
# s = "你好 WORLD2"
# print ("匹配字母数字:" + re.sub(r"\w", "hi", s))
# # 作用和sub()相同，返回一个二元元组，第一个元素是替换结果，第二个元素是替换次数
# print ("替换次数:" + str(re.subn(r"\W", "hi", s)[1]))
# print ("匹配非字母数字:" + re.sub(r"\W", "hi", s))
# print ("替换次数:" + str(re.subn(r"\W", "hi", s)[1]))
# print ("匹配空白字符:" + re.sub(r"\s", "*", s))
# print ("替换次数:" + str(re.subn(r"\s", "*", s)[1]))
# print ("匹配非空白字符:" + re.sub(r"\S", "*", s))
# print ("替换次数:" + str(re.subn(r"\S", "*", s)[1]))
# print ("匹配数字:" + re.sub(r"\d", "2.0", s))
# print ("替换次数:" + str(re.subn(r"\d", "2.0", s)[1]))
# print ("匹配非数字:" + re.sub(r"\D", "hi", s))
# print ("替换次数:" + str(re.subn(r"\D", "hi", s)[1]))
# print ("匹配任意字符:" + re.sub(r".", "hi", s))
# print ("匹配字母数字:" + str(re.subn(r".", "hi", s)[1]))

# 限定符的使用
# tell = "0791-1234567"
# print (re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tell))
# tel2 = "010-12345678"
# print(re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel2))
# tel3 = "(010)12345678"
# print(re.findall(r"[\(]?\d{3}[\)]?\d{8}|[\(]?\d{4}[\)]?\d{7}", tel3))

# compile()预编译
# s = "1abc23def45"
# p = re.compile(r"\d+")
# print(p.findall(s))
# print(p.pattern)

# 分组
# p = re.compile(r"(abc)\1")
# m = p.match("abcabcabc")
# print(m.group(0))
# print(m.group(1))
# print(m.group())

# p = re.compile(r"(?P<one>abc)(?P=one)")
# m = p.search("abcabcabc")
# print(m.group("one"))
# print(m.groupdict().keys())
# print(m.groupdict().values())
# print(m.re.pattern)

# 创建文件
# content = '''hello world'''
# f = open('hello.txt', 'w')
# f.write(content)
# f.close()

# readline()读文件
# f = open("hello.txt")
# while True:
#     line = f.readline()
#     if line:
#         print(line)
#     else:
#         break
# f.close()

# readlines()读文件
# f = file("hello.txt")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# read()读文件
# f = open("hello.txt")
# context = f.read()
# print(context)
# f.close()

# f = open("hello.txt")
# context = f.read(5)     # 读取文件前5个字节的内容
# print(context)
# print(f.tell())         # 返回文件对象当前指针的位置
# context = f.read(5)     # 继续读取文件5个字节的内容
# print(context)
# print(f.tell())         # 返回文件对象当前指针的位置
# f.close()

# writelines()写文件
# f = file("hello.txt", "w+")
# li = ["hello world\n", "hello China\n"]
# f.writelines(li)
# f.close()

# 追加新的内容到文件
# f = file("hello.txt", "a+")
# new_context = "goodbye"
# f.write(new_context)
# f.close()

# import os
# file("hello.txt", "w")
# if os.path.exists("hello.txt"):
#     os.remove("hello.txt")

# 使用read()、write()实现复制
# 创建hello.txt
# src = file("hello.txt", "w")
# li = ["hello world\n", "hello China\n"]
# src.writelines(li)
# src.close()
# # 把hello.txt复制到hello2.txt
# src = open("hello.txt", "r")
# dst = open("hello2.txt", "w")
# dst.write(src.read())
# src.close()
# dst.close()

# shutil实现文件复制
# import shutil
# shutil.copyfile("hello.txt", "hello2.txt")
# shutil.move("hello.txt", "../")
# shutil.move("hello2.txt", "hello3.txt")

# 修改文件名
import os
# li = os.listdir(".")    # 返回当前目录文件列表
# print(li)
# if "hello.txt" in li:
#     os.rename("hello.txt", "hi.txt")
# elif "hi.txt" in li:
#     os.rename("hi.txt", "hello.txt")

# 修该后缀名
# files = os.listdir(".")
# for filename in files:
#     # pos = filename.find(".")
#     # if filename[pos+1:] == "html":
#     #     newname = filename[:pos+1] + "htm"
#     #     os.rename(filename, newname)
#
#     li = os.path.splitext(filename)
#     if li[1] == ".htm":
#         newname = li[0] + ".html"
#         os.rename(filename, newname)

# import glob
# print glob.glob("*.html")

# 文件查找
# f1 = file("hello.txt", "r")
# count = 0
# for s in f1.readlines():
#     li = re.findall("hello", s)
#     if len(li) > 0:
#         count = count + li.count("hello")
# print("查找到" + str(count) + "个hello")
# f1.close()

# 文件替换
# f1 = file("hello.txt", "r")
# f2 = file("hello2.txt", "w")
# for s in f1.readlines():
#     f2.write(s.replace("hello", "hi"))
# f1.close()
# f2.close()

# import difflib
#
# f1 = file("hello.txt", "r")
# f2 = file("hi.txt", "r")
# src = f1.read()
# dst = f2.read()
# print(src)
# print(dst)
# s = difflib.SequenceMatcher(lambda x: x == "", src, dst)
# for tag, i1, i2, j1, j2 in s.get_opcodes():
#     print("%s src[%d:%d]=%s dst[%d:%d]=%s" % (tag, i1, i2, src[i1:i2], j1, j2, dst[j1:j2]))

# 创建和删除目录
import os
# os.mkdir("hello")
# os.rmdir("hello")
# os.makedirs("hello/world")
# os.removedirs("hello/world")

# 递归遍历目录
# def VisitDir(path):
#     li = os.listdir(path)
#     for p in li:
#         pathname = os.path.join(path, p)    # 获取文件完整路径
#         if not os.path.isfile(pathname):
#             VisitDir(pathname)              # 递归，继续遍历底层目录
#         else:
#             print(pathname)

# os.walk()遍历
# def VisitDir(path):
#     for root, dirs, files in os.walk(path):
#         for filepath in files:
#             print(os.path.join(root, filepath))
#
# if __name__ == "__main__":
#     path = r"D:\Python\zero-based_learn_python"
#     VisitDir(path)

import sys, time
# sys.stdin = open("hello.txt", "r")
# for line in sys.stdin.read():
#     print (line)

# 通过stdout对象重定向输出，把输出的结果保存到文件中
# sys.stdout = open(r"./hello.txt", "a")
# print("goodbye")
# sys.stdout.close()

# sys.stderr = open("record.log", "a")
# f = open(r"./11.txt", "r")
# t = time.strftime("%Y-%m-%d %X", time.localtime())
# context = f.read()
# if context:
#     sys.stderr.write(t + " " + context)
# else:
#     raise Exception, t + "异常信息"

# 文件输入流
# def FileInputStream(filename):
#     try:
#         f = open(filename)
#         for line in f:
#             for byte in line:
#                 yield byte
#     except StopIteration, e:
#         f.close()
#         return
#
# # 文件输出流
# def FileOutputStream(inputStream, filename):
#     try:
#         f = open(filename, "w")
#         while True:
#             byte = inputStream.next()
#             f.write(byte)
#     except StopIteration, e:
#         f.close()
#         return
#
# if __name__ == "__main__":
#     FileOutputStream(FileInputStream("hello.txt"), "hello2.txt")

def showFileProperties(path):
    '''显示文件的属性。包括路径、大小、创建日期、最后修改时间、最后访问时间'''
    import time, os
    for root, dirs, files in os.walk(path, True):
        print("位置:" + root)
        for filename in files:
            state = os.stat(os.path.join(root, filename))
            info = "文件名:" + filename + " "
            info = info + "大小:" + ("%d" % state[-4]) + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-1]))
            info = info + "最后修改时间:" + t + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-3]))
            info = info + "最后访问时间:" + t + " "
            print (info)

if __name__ == "__main__":
    path = r"D:\Python\zero-based_learn_python"
    showFileProperties(path)
