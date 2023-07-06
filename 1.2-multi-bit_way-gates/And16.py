# DO NOT ERASE THIS CELL - to be graded

class And16(Component):
    IN = [w(16).a, w(16).b]
    OUT = [w(16).out]

    PARTS = [ # แนะนำให้สร้างเกท 16 ตัวด้วย for-loop
    ]
    for i in range(16):
        PARTS.append(And(a=w.a[i], b=w.b[i], out=w.out[i]))