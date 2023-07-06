# DO NOT ERASE THIS CELL - to be graded

class Mux4Way16(Component):
    IN = [w(16).a, w(16).b, w(16).c, w(16).d, w(2).sel]
    OUT = [w(16).out]

    PARTS = [
        Mux16(a=w.a, b=w.b, sel= w.sel[0], out=w(16).x),
        Mux16(a=w.c, b=w.d, sel= w.sel[0], out=w(16).y),
        Mux16(a=w.x, b=w.y, sel= w.sel[1], out=w.out),
    ]