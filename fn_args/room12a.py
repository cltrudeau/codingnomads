def display_message(line1, line2, spacing=1, indent=4):
    print(indent*' ', line1)
    print(spacing * '\n')
    print(indent*' ', line2)


def add(*args):
    x = 0
    for arg in args:
        x += arg

    print('sum is', x)


def multiply(first, second, *args):
    print('multiplying', first, 'x', second)
    x = first * second

    for arg in args:
        print('multiplying', x, 'x', arg)
        x = x * arg

    print('=> total is', x)


def person(first, last, age):
    print(first, last, 'is', age, 'years old')


def address(**kwargs):
    print('The parts of the address are:')
    for key, value in kwargs.items():
        print(key, '=', value)


def combined(first, *args, phone='555-1212', **kwargs):
    print('first is:', first)
    print('args list is', args)
    print('phone is:', phone)
    print('kwargs dict is', kwargs)


if __name__ == '__main__':

    print(75*'*')
    print("===== Calling display_message('Hello', 'there')")
    display_message('Hello', 'there')

    print()
    print(75*'*')
    print("Named arguments that have defaults don't have to be specified")
    print("You can skip the 'spacing' positional argument by naming the ")
    print("'indent' one.")
    print("\n===== Calling display_message('Hello', 'there', indent=8)")
    display_message('Hello', 'there', indent=8)

    print()
    print(75*'*')
    print("You can specify '*arg' to have an arbitraty number of")
    print("positional arguments")
    print("\n===== Calling add(1, 2, 3)")
    add(1, 2, 3)
    print("\n===== Calling add(1, 2, 3, 4, 5, 6)")
    add(1, 2, 3, 4, 5, 6)

    print()
    print(75*'*')
    print("You can mix positional arguments with '*arg'")
    print("\n===== Calling multiply(2, 3, 5, 6)")
    multiply(2, 3, 5, 6)

    print()
    print(75*'*')
    print("You can use a dictionary and the '**' operator to dynamically")
    print("specify the arguments to a function")
    parms = {
        'first':'Bob',
        'last':'Roberts',
        'age':45,
    }
    print("\n===== 'parms' dict is:", parms)
    print("===== Calling person(**parms)")
    person(**parms)

    print()
    print(75*'*')
    print("You can use the '**' argument to allow arbitrarily named arguments")
    print("in a function definition. If you declare a function with '**kwargs'")
    print("the function will have a dictionary named 'kwargs' with the named")
    print("arguments passed into the function")

    print("\n===== Calling address(line1='123 Foo St', line2='Apt 12',")
    print("                  state='CA', zip=90210)")
    address(line1='123 Foo St', line2='Apt 12', state='CA', zip=90210)

    print()
    print(75*'*')
    print("All of these concepts can be combined")
    print("\n===== Calling combined('Bob', 'William', 'Roberts',")
    print("                  job='Senator', corruption='high')")
    combined('Bob', 'William', 'Roberts', job='Senator', corruption='high')
