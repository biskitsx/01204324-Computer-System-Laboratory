# DO NOT ERASE THIS CELL - to be graded

class DMux8Way(Component):
    IN = [w.In, w(3).sel]
    OUT = [w.a, w.b, w.c, w.d, w.e, w.f, w.g, w.h]

    PARTS = [
        DMux(In=w.In, sel= w.sel[2], a=w.out1, b=w.out2),
        DMux4Way(In=w.out1, sel= w.sel[0:2], a=w.a, b=w.b, c=w.c, d=w.d),
        DMux4Way(In=w.out2, sel= w.sel[0:2], a=w.e, b=w.f, c=w.g, d=w.h)
    ]