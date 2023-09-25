# DO NOT ERASE THIS CELL - to be graded
class RAM8(Component):
    IN = [w(16).In, w(3).address, w.load]
    OUT = [w(16).out]

    PARTS = [
        DMux8Way(In=w.load, sel=w.address, a=w.l0, b=w.l1, c=w.l2, d=w.l3, e=w.l4, f=w.l5, g=w.l6, h=w.l7),
    ]

    for i in range(8):
      PARTS.append(Register(In=w.In, load=getattr(w, f"l{i}"), out=getattr(w(16), f"reg{i}")))

    
    PARTS.append(Mux8Way16(a=w.reg0, b=w.reg1, c=w.reg2, d=w.reg3, e=w.reg4, f=w.reg5, g=w.reg6, h=w.reg7, sel=w.address, out=w.out))
