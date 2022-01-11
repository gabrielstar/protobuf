# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# it is simpler than iterators and less work
from faker import Faker


def simple_generator():  # generator function
    n = 1  # n will be rememberd between each call e.g. next()
    yield n
    n += 2
    yield n
    n += 3
    yield n


numbers = simple_generator()  # return an object - iterator so we can call next on it

try:
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
except StopIteration as err:
    print("Stopped")

# state is remebered so we need or create new one for second use, generator object can only be iterated once
numbers2 = simple_generator()
for i in numbers2:
    print(i)

# another iterator over tuple Uppercase items
t = ("John Kindy", "Joe Rome", "Eva", "Robo Maxi")


def upper(tup: tuple):
    length = len(tup)
    for i in range(length):
        parts = str(tup[i]).split()
        for part in parts:
            yield str(part).upper()


# iterates over names chunks in uppercase - tokenizes data
for item in upper(t):
    print(item)

# python generator expressions .. enclosed with () while list comprehensions ar ewith []
# major difference is that generator expression will produce item 1 at a time while list expression will produce entire thing
my_list = [3, 4, 5]

list_ = [x ** 2 for x in my_list]
print(list_)  # entire thing in memory

generator = (x ** 2 for x in my_list)
print(next(generator))  # just the next value
print(next(generator))

# when given as arguments in function () can be dropped e.g.
assert max((x ** 2 for x in my_list)) == max(x ** 2 for x in my_list)


# generator represntations of sequences are preferred

# genrators can be pipelined

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))  # this pipelining is very efficient


# it is also simpler, this is the same result as in our fakenames iterator

# custom iterators need to implement __iter__ and __next__
class FakeNames():
    """
        return fake names until max, then return no more data
        when max_abort is reached rais estop iteration
    """

    def __init__(self, max, max_abort):
        self.max = max
        self.max_abort = max_abort
        self._fake = Faker()

    # counter
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= self.max_abort:
            raise StopIteration
        elif self.n < self.max:
            self.n += 1
            return str(self.n) + "." + self._fake.name()
        else:
            self.n += 1
            return "No more names"


# same as generator
def fake_names(max, max_abort):
    fake = Faker()
    n = 0
    for i in range(max_abort):
        if n < max:
            n += 1
            yield str(n) + "." + fake.name()
        else:
            n += 1
            yield "No more names"


for name in fake_names(2, 4):
    print(name)
