# DO NOT ERASE THIS CELL - to be graded

class And(AndLayoutMixin, Component):
    IN = [w.a, w.b]
    OUT = [w.out]

    PARTS = [
      Nand(a=w.a, b=w.b, out=w.nand_out),
      Not(In=w.nand_out, out=w.out)
    ]