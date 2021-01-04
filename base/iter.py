from collections import Iterable


def iteration():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key)
        print(d[key])
    for value in d.values():
        print(value)
    for key, value in d.items():
        print(key)
        print(value)
    print()
    instance = isinstance(d, Iterable)
    print(instance)
    for i, value in enumerate(d):
        print(i, value)


# 判断是否可以迭代


if __name__ == '__main__':
    iteration()
    # 定义一个list
    classmates = ['Michael', 'Bob', 'Tracy', 'Tracy']
    print(classmates)
    print(len(classmates))

    # 定义一个tuple
    t = (1, 2)
    t1 = (1,)
    # t[2] = 2
    print(t)

    # 在set中，没有重复的key。
    s = set(classmates)
    print(s)

    d = {'a': 1, 'b': 2, 'c': 3}

    # 字符串也是iterable，
    # 只要是能for循环遍历的都是iterable，
