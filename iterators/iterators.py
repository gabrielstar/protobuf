from faker import Faker

# https://www.programiz.com/python-programming/iterator

# example of sth impolementing 'iterable'
tup = (1, 2, 3)
for t in tup:  # for will actually call iter() on tup
    print(t)

# another way
tup_iterator = iter(tup)  # makes iterator of sth that is iterable
print(next(tup_iterator))
print(next(tup_iterator))
print(next(tup_iterator))

# In fact this is how for is implemented in python
# create an iterator object from that iterable
iter_obj = iter((9, 8, 7))

# infinite loop - for
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break


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


fake_name = FakeNames(2,3)
i = iter(fake_name)  # create iterable from the object
try:
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
except StopIteration:
    print("StopIteration caught")

#we can also use it this way

print("Looping through all items")
for name in FakeNames(1,4):
    print(name)

#Iterators can be infinite, they safe memorym, easier way of creating iterators is through generators