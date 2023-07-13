# DO NOT ERASE THIS CELL - to be graded

class Not16(Component):
    IN = [w(16).In]
    OUT = [w(16).out]

    PARTS = [ # แนะนำให้สร้างเกท 16 ตัวด้วย for-loop

    ]

    for i in range(16):
        PARTS.append(Not(In=w.In[i], out=w.out[i]))