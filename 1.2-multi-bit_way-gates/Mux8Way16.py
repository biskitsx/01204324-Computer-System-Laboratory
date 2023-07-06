# DO NOT ERASE THIS CELL - to be graded

class Mux8Way16(Component):
    IN = [
        w(16).a,
        w(16).b,
        w(16).c,
        w(16).d,
        w(16).e,
        w(16).f,
        w(16).g,
        w(16).h,
        w(3).sel,
    ]
    OUT = [w(16).out]

    PARTS = [
        Mux4Way16(a=w.a, b=w.b, c=w.c, d=w.d, sel=w.sel[0:2], out=w(16).out1),
        Mux4Way16(a=w.e, b=w.f, c=w.g, d=w.h, sel=w.sel[0:2], out=w(16).out2),
        Mux16(a=w.out1, b=w.out2, sel=w.sel[2], out=w.out)
    ]