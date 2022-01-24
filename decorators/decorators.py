# everything in python is object so we can pass function as arg to another fucntiuon

# example
def inc(x):
    return x + 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 6))


# func inside func

def print_msg(message):
    greeting = "Hello"

    def printer():  # closure -  inner function that remembers values in scope even if outer function is done executing
        print(greeting, message)

    return printer


func = print_msg("Python is awesome")
func()


# decorators - takes inner func and add functionality

def display_info(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished executing")

    return inner


# this causes printer to be passed as argument to display_info function
@display_info
def printer():
    print("hello world")


# printer()
# decorated_func = display_info(printer)
# decorated_func()

# instead of this we can write decorator in a nicer way
printer()


# decorator for function with parameters

def smart_divide(func):
    def inner(a, b):  # arguments such as of cdecorated function
        print("Dividing", a, "by", b)
        if b == 0:
            print("Cannot divide by zero")
            return
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


value = divide(15, 3)
print(value)
value = divide(15, 0)
print(value)


# in python we can chain decorators

def no_15_divide(func):
    def inner(a, b):
        if a == 15:
            print("Cannot divide 15")
            print("*" * 10)
            return
        return func(a, b)

    return inner


#order matters
@no_15_divide
@smart_divide
def new_divide(a, b):
    return a / b

value = new_divide(15,0)