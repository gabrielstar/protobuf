def generator():
    for i in range(1,10):
        yield i*i

g=generator()
print(next(g))
print(next(g))