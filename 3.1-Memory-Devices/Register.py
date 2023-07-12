# DO NOT ERASE THIS CELL - to be graded
class Register(Component):
    IN = [w(16).In, w.load]
    OUT = [w(16).out]

    PARTS = [
    ]

    for i in range(16):
      PARTS.append(Bit(In=w.In[i], load=w.load, out=w.out[i]))