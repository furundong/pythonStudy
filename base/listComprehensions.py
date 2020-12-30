from collections import Iterable
import os

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

    #  这里的%运算速度慢，可以采用按位与 & 运算题高速度
    print([x * x for x in list(range(1, 11)) if x & 1 == 0 ])

    #  这里的if是for的筛选条件，不能使用else，
    #    print([x * x for x in list(range(1, 11)) if x & 1 == 0 else x])

