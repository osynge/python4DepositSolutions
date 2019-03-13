"""
Restrictions on Dictionary Keys

* can appear in a dictionary only once. Duplicate keys are not allowed
* must be hashable, which means it can be passed to a hash function

Should the key apear twice in definition second instance overrides.

Examples of allowable keys in dict.

* integers, strings, float, bool, touples, classes can all be keys.
* list, dictionaries cannot be keys.

There are no restrictions on dictionary values
"""


def dict_len():
    """
    Removes all elements of dictionary dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return len(mydict)


def dict_square_b_set():
    """
    Removes all elements of dictionary dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    mydict['elephant'] = 4
    return mydict


def dict_square_b_get_1():
    """
    get value from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict['cow']


def dict_square_b_get_2():
    """
    get value from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict['elephant']


def dict_del():
    """
    Removes all elements of dictionary dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    del mydict['cow']
    return mydict


def dict_in():
    """
    use 'in' as haskey() is depricated.
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return 'cow' in mydict


def dict_pop():
    """
    pop by key
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict.pop('dog')


def dict_popitem():
    """
    pop by choice of dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict.popitem()


def dict_get_1():
    """
    get value from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict.get('cow')


def dict_get_2():
    """
    get value from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict.get('elephant')


def dict_get_3():
    """
    get value from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict.get('elephant', 'default')


def dict_keys():
    """
    get keys from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict.keys()


def dict_values():
    """
    get values from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    return mydict.values()


def dict_items():
    """
    get value from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    for key, value in mydict.items():
        print("key=%s,value=%s" % (key, value))


def dict_update():
    """
    get value from dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    updict = {'lion': 1, 'elephant': 2, 'sheep': 3}
    mydict.update(updict)
    return mydict


def dict_clear():
    """
    Removes all elements of dictionary dict
    """
    mydict = {'cow': 1, 'dog': 2, 'lion': 3}
    mydict.clear()
    return mydict
