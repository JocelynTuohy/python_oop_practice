# MathDojo Assignment

# Part I
# Create a Python class called MathDojo that has the methods add and subtract.
# Have these 2 functions take at least 1 parameter. Then create a new instance
# called md.
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        self.result += sum(args)
        return self
    def subtract(self, *args):
        self.result -= sum(args)
        return self

class md(MathDojo):
    pass

print md().add(2).add(2, 5).subtract(3, 2).result

# Part II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter
# with any number of values passed into the list.
# Part III
# Make any needed changes in MathDojo in order to support tuples of values in
# addition to lists and singletons.
class MathDojo2(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for each in range(0, len(args)):
            if isinstance(args[each], int):
                self.result += args[each]
            if isinstance(args[each], list) or isinstance(args[each], tuple):
                for li in args[each]:
                    self.result += li
        return self
    def subtract(self, *args):
        for each in range(0, len(args)):
            if isinstance(args[each], int):
                self.result -= args[each]
            if isinstance(args[each], list) or isinstance(args[each], tuple):
                for li in args[each]:
                    self.result -= li
        return self

# print MathDojo2().add(1).add(1).result

print MathDojo2().add([1], 3, 4).add([3, 5, 7, 8],
                                     [2, 4.3, 1.25]).subtract(2, [2, 3],
                                                              [1.1, 2.3]).result
