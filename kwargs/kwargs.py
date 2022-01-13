# We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.

def adder(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(adder(1, 2, 3, 4))
numbers = (1, 23, 4)
numbers2 = [1, 23, 4, 8]
print(adder(*numbers))
print(adder(*numbers2))

values = {'first': 1, 'second': 2}
print(f"{values}")


def listing(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} ++ {value}")


listing(**values)


# * must always be before **
def together(*args, **kwargs):
    for n in args:
        for k, v in kwargs.items():
            print(f"{n} + {k} + {v}")


together(*numbers, **values)
