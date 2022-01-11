import dataclasses


class Feature:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def __str__(self):
        """
        :return: sting repr of dict of attributes
        """
        return str(vars(self))

    def __getattribute__(self, item):
        """
        Called for every attribute lookuo
        :param item:
        :return:
        """
        print(f"Called __getattribute__ for {item} and got ... ")
        return super().__getattribute__(item)  # use parent function

    def __getattr__(self, item):
        """
        Called on attribute missing - can intercept and e.g. add it
        :param item:
        :return:
        """
        print(f"Intecepted with  __getattr__ on missing attribute: {item}")
        print(f"Adding attribute")
        super().__setattr__(item, [])


f = Feature(age=12, weight=33)
print(f.weight)
print(f" accessing missing attribute:  {f.missing_attribute}")
print(f" accessing missing attribute again: {f.missing_attribute}")
print("My instance has the following attributes")
print(f)
