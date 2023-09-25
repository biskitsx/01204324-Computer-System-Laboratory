# DO NOT ERASE THIS CELL - to be graded
class HalfAdder(Component):
    IN = [w.a, w.b]
    OUT = [w.sum, w.carry]

    PARTS = [
        Xor(a=w.a, b=w.b, out=w.sum),
        And(a=w.a,b=w.b,out=w.carry)
    ]