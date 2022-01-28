class A:
    PATH = "/yo"
    def who_am_i(self):
        print(f'I am {self.PATH}')

class B(A):
    PATH = "/foo"
    pass

b = B()
b.who_am_i()