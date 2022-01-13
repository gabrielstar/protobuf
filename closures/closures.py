def print_msg(msg):
    # This is the outer enclosing function

    # nested function
    def printer():
        # This is the nested function
        msg = 'hello from nested function. This modification is local only'
        print(msg)

    print(msg)
    printer()


# We execute the function
# Output: Hello
print_msg("Hello")


##return function and bind variables
def print_msg_2(msg):
    # This is the outer enclosing function

    # nested function
    def printer():
        # This is the nested function
        print(msg)

    return printer


another = print_msg_2("Hello 2")  # this techique in python is called closure
del print_msg_2  # you can even delete that and another() will leave
another()

print("Am I a closure?")
print(another.__closure__)  # yes
print(print_msg.__closure__)  # no

# closures sometimes help to avoid objects when it is just a method or a few to be implemented in a class, howevr when there are many attrbute san dmethods
# classes are better

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))
