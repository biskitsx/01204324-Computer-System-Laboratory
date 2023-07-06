# DO NOT ERASE THIS CELL - to be graded

class DMux(Component):
    IN = [w.In, w.sel]
    OUT = [w.a, w.b]

    PARTS = [
        Not(In=w.sel, out=w.s_out),
        And(a=w.s_out , b=w.In, out=w.a),
        And(a=w.In , b=w.sel, out=w.b),

    ]