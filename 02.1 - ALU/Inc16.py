# DO NOT ERASE THIS CELL - to be graded
class Inc16(Component):
    IN = [w(16).In]
    OUT= [w(16).out]

    PARTS = [
        Add16(a=w.In, b=w(16).int_one, out=w.out)
    ]