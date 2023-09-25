# DO NOT ERASE THIS CELL - to be graded

class DMux4Way(Component):
    IN = [w.In, w(2).sel]
    OUT = [w.a, w.b, w.c, w.d]

    PARTS = [
        DMux(In=w.In, sel= w.sel[1], a=w.out1, b=w.out2),
        DMux(In=w.out1, sel= w.sel[0], a=w.a, b=w.b),
        DMux(In=w.out2, sel= w.sel[0], a=w.c, b=w.d)
    ]