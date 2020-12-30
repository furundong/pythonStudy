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
