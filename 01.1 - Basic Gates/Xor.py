# DO NOT ERASE THIS CELL - to be graded

class Xor(XorLayoutMixin, Component):
    IN = [w.a, w.b]
    OUT = [w.out]

    PARTS = [
      Nand(a=w.a, b=w.b, out=w.nand_out1),
      Nand(a=w.a, b=w.nand_out1, out=w.nand_out2),
      Nand(a=w.nand_out1, b=w.b, out=w.nand_out3),
      Nand(a=w.nand_out2, b=w.nand_out3, out=w.out),

    ]