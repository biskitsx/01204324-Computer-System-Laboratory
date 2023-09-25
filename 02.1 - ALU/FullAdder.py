# DO NOT ERASE THIS CELL - to be graded
class FullAdder(Component):
    IN = [w.a, w.b, w.c]
    OUT = [w.sum, w.carry]

    PARTS = [
      HalfAdder(a=w.a, b=w.b, sum=w.o1, carry=w.c1),
      HalfAdder(a=w.o1, b=w.c, sum=w.sum, carry=w.c2),
      Or(a=w.c1, b=w.c2, out=w.carry),
    ]