def list_len():
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return len(mylist)


def list_count():
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist.count('cow')


def list_index():
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist[4]


def list_range():
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist[1:4]


def list_range2():
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist[-4:]


def list_stride_1():
    """
    Default stride is 1
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist[1:4:1]


def list_stride_2():
    """
    Try stride as 2
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist[1:4:2]


def list_stride_3():
    """
    Try stride as -1
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist[1:4:-1]


def list_join():
    """
    Now we want to join
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return ' '.join(mylist)


def list_pop_1():
    """
    Now pop first item
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist.pop()


def list_pop_2():
    """
    Now pop at index
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist.pop(0)


def list_insert_1():
    """
    insertion
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    mylist.insert(0, 'rabbit')
    return mylist


def list_insert_2():
    """
    insertion
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    mylist.insert(3, 'rabbit')
    return mylist


def list_in():
    """
    in
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return 'rabbit' in mylist


def list_append():
    """
    append
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    mylist.append('pony')
    return mylist


def list_extend():
    """
    extend
    """
    mylist = ['dog', 'lion', 'snake']
    ext = ['elephant', 'cow', 'donkey', 'goat', 'duck']
    mylist.extend(ext)
    return mylist


def list_addition():
    """
    extend
    """
    mylist = ['dog', 'lion', 'snake']
    ext = ['elephant', 'cow', 'donkey', 'goat', 'duck']
    return mylist + ext


def list_multiplication():
    """
    extend
    """
    mylist = ['dog', 'lion', 'snake']
    return mylist * 3


def list_remove():
    """
    remove
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    mylist.remove('lion')
    return mylist


def list_del():
    """
    del
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    del mylist[2]
    return mylist


def list_reverse():
    """
    reverse
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    mylist.reverse()
    return mylist


def list_sort():
    """
    sort
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    mylist.sort()
    return mylist


def list_print():
    """
    print
    """
    mylist = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    for item in mylist:
        print(item)


def list_nested():
    """
    print
    """
    mylist = [['dog', 'lion'], ['snake', 'elephant'], ['cow', 'donkey'], ['goat', 'duck']]
    for item in mylist:
        print(item)
