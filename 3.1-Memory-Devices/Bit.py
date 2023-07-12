# DO NOT ERASE THIS CELL - to be graded
class Bit(Component):
    IN = [w.In, w.load]
    OUT = [w.out]

    PARTS = [
      Mux(a=w.out, b=w.In, sel=w.load, out=w.omux),
      DFF(In=w.omux, out=w.out),
    ]