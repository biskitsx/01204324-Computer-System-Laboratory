# DO NOT ERASE THIS CELL - to be graded

class Mux(Component):
    IN = [w.a, w.b, w.sel]
    OUT = [w.out]

    PARTS = [
      Not(In=w.sel, out=w.s_out),
      Nand(a=w.a, b=w.s_out, out=w.nand_out1),
      Nand(a=w.b, b=w.sel, out=w.nand_out2),
      Nand(a=w.nand_out1, b=w.nand_out2, out=w.out),
    ]