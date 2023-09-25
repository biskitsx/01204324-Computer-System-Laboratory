# DO NOT ERASE THIS CELL - to be graded

class Or(OrLayoutMixin, Component):
    IN = [w.a, w.b]
    OUT = [w.out]

    PARTS = [
      Not(In=w.a, out=w.not_out1),
      Not(In=w.b, out=w.not_out2),
      Nand(a=w.not_out1, b=w.not_out2, out=w.out),
    ]