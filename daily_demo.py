
"""

python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。这种方式相当于传值和传引用的一种综合。

如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。

如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。

"""


def a(list_nums):
    print(id(list_nums))
    list_nums.append('a')


def b(list_nums):
    print(id(list_nums))
    list_nums.append('b')


def c(tuple_nums):

    print(id(tuple_nums))
    nums = tuple_nums + ("c",)


def d(tuple_nums):
    print(id(tuple_nums))
    nums = tuple_nums + ("d",)


if __name__ == '__main__':

    list_nums = [1, 2, 3, 4, 'wakaka']
    print("list_nums :", list_nums)
    a(list_nums)
    print("list_nums :", list_nums)
    b(list_nums)
    print("list_nums :", list_nums)

    tuple_nums = (1, 2, 3, 4, 5, "wakaka",)
    print("tuple_nums :", tuple_nums)
    c(tuple_nums)
    print("tuple_nums :", tuple_nums)
    d(tuple_nums)
    print("tuple_nums :", tuple_nums)




