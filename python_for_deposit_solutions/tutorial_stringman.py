def string_len():
    s = 'dog lion snake elephant cow donkey goat duck'
    return len(s)


def string_upper():
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.upper()


def string_lower():
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.upper()


def string_isupper():
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.isupper()


def string_islower():
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.islower()


def string_center():
    """
    Some options I have never used
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.center(56)


def string_partiton():
    """
    Some options I should have used
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.partiton(' ')


def string_index():
    s = 'dog lion snake elephant cow donkey goat duck'
    return s[4]


def string_range():
    s = 'dog lion snake elephant cow donkey goat duck'
    return s[4:8]


def string_range2():
    s = 'dog lion snake elephant cow donkey goat duck'
    return s[-4:]


def string_stride_1():
    """
    Default stride is 1
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s[4:8:1]


def string_stride_2():
    """
    Try stride as 2
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s[4:8:2]


def string_stride_3():
    """
    Try stride as -1
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s[7:3:-1]


def string_split_1():
    """
    Just split
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.split()


def string_split_2():
    """
    Split by letter 'o'
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.split('o')


def string_split_3():
    """
    split just once
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.split(' ', 1)


def string_split_4():
    """
    Ok now right split
    """
    s = 'dog lion snake elephant cow donkey goat duck'
    return s.rsplit(' ', 1)


def string_join():
    """
    Now we want to join
    """
    s = ['dog', 'lion', 'snake', 'elephant', 'cow', 'donkey', 'goat', 'duck']
    return ' '.join(s)


def string_from_byte_array():
    return b"abcde".decode("utf-8")
