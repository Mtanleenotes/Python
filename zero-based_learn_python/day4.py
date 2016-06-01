# coding=utf-8
# 自定义模块


# def func():
#     print("MyModule.func()")
#
#
# class MyClass:
#     def myFunc(self):
#         print("MyModule.MyClass.myFunc()")

# count = 1
#
#
# def func():
#     global count
#     count = count + 1
#     return count

# def func(x):
#     if x > 0:
#         return x
#
# print(filter(func, range(-9, 10)))          # 调用filter函数，返回filter对象
# print(list(filter(func, range(-9, 10))))    # 将filter对象转为列表

# def sum(x, y):
#     return x + y
# from functools import reduce
# print(reduce(sum, range(0, 10)))
# print(reduce(sum, range(0, 10), 10))
# print(reduce(sum, range(0, 0), 10))

# def power(x):
#     return x ** x
# print(map(power, range(1, 5)))
# print(list(map(power, range(1, 5))))
#
#
# def power2(x, y):
#     return x ** y
# print(map(power2, range(1, 5), range(5, 1, -1)))
# print(list(map(power2, range(1, 5), range(5, 1, -1))))

# 函数的默认参数
# def arithmetic(x=1, y=1, operator="+"):
#     result = {
#         "+": x + y,
#         "-": x - y,
#         "*": x * y,
#         "/": x / y
#     }
#     return result.get(operator)
# print(arithmetic(1, 2))
# print(arithmetic(1, 2, "-"))
# print(arithmetic(y=3, operator="-"))
# print(arithmetic(x=4, operator="-"))
# print(arithmetic(y=3, x=4, operator="-"))

# 列表作为参数传递
# def arithmetic(args=[], operator="+"):
#     x = args[0]
#     y = args[1]
#     result = {
#         "+": x + y,
#         "-": x - y,
#         "*": x * y,
#         "/": x / y
#     }
#     return result.get(operator)
# print(arithmetic([1, 2]))

# def append(args=[]):
#     args.append(0)
#     print(args)

# def append(args=[]):
#     if len(args) <= 0:
#         args = []
#     args.append(0)
#     print(args)
#
# append()
# append([1])
# append()

# 传递可变参数
# def func(*args):
#     print args
# func(1, 2, 3)

def search(*t, **d):
    keys = d.keys()
    values = d.values()
    print(keys)
    print(values)
    for arg in t:
        for key in keys:
            if arg == key:
                print("find:", d[key])
search("one", "three", one="1", two="2", three="3")





