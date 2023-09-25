# DO NOT ERASE THIS CELL - to be graded
class PriorityEncoder(Component):
    IN = [w.a, w.b, w.c, w.d]
    OUT = [w(2).out, w.v]

    PARTS = [
        Not(In=w.b, out=w.notb),
        And(a=w.notb, b=w.c, out=w.and1),
        Or(a=w.a, b=w.and1, out=w.out[0]),
        Or(a=w.a, b=w.b, out=w.out1),
        Or(a=w.out1, b=w.c, out=w.vv),
        Or(a=w.vv, b=w.d, out=w.v),
        Buffer(In=w.out1, out=w.out[1])
    ]
# put additional auxilary components here (if needed)

class PC(Component):
    IN = [w(16).In, w.load, w.inc, w.reset]
    OUT = [w(16).out]

    PARTS = [
        PriorityEncoder(a=w.reset, b= w.load, c=w.inc, d=w.zero, out=w(2).mode, v=w.v),
        Mux4Way16(a=w(16).zero, b=w(16).incx, c=w.In, d=w(16).zero, sel=w.mode, out=w(16).inreg),
        Register(In=w.inreg, load = w.v , out=w.out),
        Inc16(In=w.out, out=w.incx)
    ]