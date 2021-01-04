# from collections import Iterable
import os


def fib(max2):
    n, a, b = 0, 0, 1
    while n < max2:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


''' [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''


def triangles():
    result = []
    n = 1
    while True:
        # n =1 0        [1]
        # n =2 0,1      [1] [1]
        # n=3 0,1,2     [1] [2] [1]
        # n=4 0,1,2,3   [1] [3] [3] [1]
        list2 = [1 if x == 0 or x == n - 1 else result[x] + result[x - 1] for x in range(0, n)]
        n += 1
        result = list2
        yield result


if __name__ == '__main__':
    print(list(range(1, 11)))
    # print((range(11, 12), Iterable))

    L = []
    for i in list(range(1, 11)):
        L.append(i * i)

    print(L)
    # 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
    print([x * x for x in list(range(1, 11))])

    # 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
    # for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
    print([x * x for x in list(range(1, 11)) if x % 2 == 0])

    # 还可以使用两层循环，可以生成全排列：
    print([m + n for m in '123' for n in 'abc'])

    # 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
    print([d for d in os.listdir('.')])

    d = {'a': '1', 'b': '2', 'c': '3'}
    print([k + '=' + v for k, v in d.items()])

    print("---------------------------------------")

    #  这里的%运算速度慢，可以采用按位与 & 运算题高速度
    print([x * x for x in list(range(1, 11)) if x & 1 == 0])

    #  这里的if是for的筛选条件，不能使用else，
    #    print([x * x for x in list(range(1, 11)) if x & 1 == 0 else x])

    # 这里的if跟else是条件，缺一不可
    print([x * x if x & 1 == 0 else 'odd' for x in list(range(1, 11))])

    print("---------------------------------------")

    # print([x * x if x & 1 == 0 for x in list(range(1, 11))])

    # =====================================================================================
    # 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
    print([x if x != 0 else 'is zero' for x in range(0, 11)])
    g = (x if x != 0 else 'is zero' for x in range(0, 11))
    print()
    # next(g)  打印出不来
    print(g)
    for x in g:
        print(x, end=' ')

    print()
    print()
    generator = fib(4)
    for x in generator:
        print(x)

    while True:
        try:
            x = next(generator)
            print('x:', x)
        except StopIteration as e:
            print(e.value)
            break

    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    a = [1, 2, 3, 4, 5, 6]
    print(a[3:3])
    s = 'abcdefghijklmnopqrstuvwxyz'
    print(s[-1:6:-1])
    print(s[-1:-6:-1])


    def plus(a, b):
        return a + b


    def compose(func, array):
        return func(array[0], array[1])


    result = compose(plus, [1, 2])
    print(result)


    def add(x, y, f):
        return f(x) + f(y)


    print(add(1, 2, abs))
