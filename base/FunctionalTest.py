from functools import reduce


def f(x):
    return pow(x, 2)


def add(x, y):
    return x + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num2(s):
        return DIGITS[s]

    return reduce(fn, map(char2num2, s))


if __name__ == '__main__':
    print(f(3))
    g = map(f, [1, 2, 3, 4, 5])
    print(g)
    print(list(g))
    # print(g.__next__())
    # print(next(g))
    # print(g.__next__())
    # print(g.__next__())

    print('-------------------')

    print(reduce(add, [1, 2, 3, 4]))
    print(sum([1, 2, 3, 4]))
    print('-------------------')

    # print(char2num('2123123'))
    print(list(map(char2num, "32141")))
    print(str2int('2123123'))
