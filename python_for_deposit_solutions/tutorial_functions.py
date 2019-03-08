"""
Example of flow control and the case statement
"""


def conditional_example():
    x = int(raw_input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')


def flow_control_while():
    # Fibonacci series:
    # the sum of two elements defines the next
    a, b = 0, 1
    while b < 10:
        print(b)
        a, b = b, a+b


def flow_control_for():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))


def flow_control_prime():
    """
    example of nested loops and break statement
    """
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n/x)
                break
            else:
                # loop fell through without finding a factor
                print(n, 'is a prime number')


def one():
    return "January"


def two():
    return "February"


def three():
    return "March"


def four():
    return "April"


def five():
    return "May"


def six():
    return "June"


def seven():
    return "July"


def eight():
    return "August"


def nine():
    return "September"


def ten():
    return "October"


def eleven():
    return "November"


def twelve():
    return "December"


def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print(func())
