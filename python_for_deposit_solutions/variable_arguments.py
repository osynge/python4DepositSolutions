"""
Example of *argv **kwargs usage
"""


def args_static(apple, banana, grape):
    print(apple)
    print(banana)
    print(grape)


def calling_static():
    args_static(1, 2, 3)


def args_variable(*argv):
    for arg in argv:
        print("another arg through *argv :", arg)


def calling_variable():
    arg_list = [1, 2, 3, 4]
    args_variable(*arg_list)


def kargs_variable(**kwargs):
    session = kwargs.get('session', None)
    if session is None:
        session = "we have no sessione variable"
    for key, value in kwargs.items():
        print("kargs_variable: %s == %s" % (key, value))


def calling_kargs_variable():
    arg_dic = {
        'apple': 1,
        'pair': 2,
        'orange': 3,
        }
    kargs_variable(**arg_dic)
    kargs_variable()


def run_all():
    calling_static()
    calling_variable()
    calling_kargs_variable()
