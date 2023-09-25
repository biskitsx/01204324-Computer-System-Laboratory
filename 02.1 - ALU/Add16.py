# DO NOT ERASE THIS CELL - to be graded
class Add16(Component):
    IN = [w(16).a, w(16).b]
    OUT= [w(16).out]

    PARTS = [
        HalfAdder(a=w.a[0], b=w.b[0], sum=w.out[0], carry=w.c0),
        FullAdder(a=w.a[1], b=w.b[1], c=w.c0, sum=w.out[1], carry=w.c1),
        FullAdder(a=w.a[2], b=w.b[2], c=w.c1, sum=w.out[2], carry=w.c2),
        FullAdder(a=w.a[3], b=w.b[3], c=w.c2, sum=w.out[3], carry=w.c3),
        FullAdder(a=w.a[4], b=w.b[4], c=w.c3, sum=w.out[4], carry=w.c4),
        FullAdder(a=w.a[5], b=w.b[5], c=w.c4, sum=w.out[5], carry=w.c5),
        FullAdder(a=w.a[6], b=w.b[6], c=w.c5, sum=w.out[6], carry=w.c6),
        FullAdder(a=w.a[7], b=w.b[7], c=w.c6, sum=w.out[7], carry=w.c7),
        FullAdder(a=w.a[8], b=w.b[8], c=w.c7, sum=w.out[8], carry=w.c8),
        FullAdder(a=w.a[9], b=w.b[9], c=w.c8, sum=w.out[9], carry=w.c9),
        FullAdder(a=w.a[10], b=w.b[10], c=w.c9, sum=w.out[10], carry=w.c10),
        FullAdder(a=w.a[11], b=w.b[11], c=w.c10, sum=w.out[11], carry=w.c11),
        FullAdder(a=w.a[12], b=w.b[12], c=w.c11, sum=w.out[12], carry=w.c12),
        FullAdder(a=w.a[13], b=w.b[13], c=w.c12, sum=w.out[13], carry=w.c13),
        FullAdder(a=w.a[14], b=w.b[14], c=w.c13, sum=w.out[14], carry=w.c14),
        FullAdder(a=w.a[15], b=w.b[15], c=w.c14, sum=w.out[15], carry=w.c15),
    ]