# DO NOT ERASE THIS CELL - to be graded

# replace with fast implementation
RAM512 = gen_fast_ram_component(9)

class RAM4K(Component):
    IN = [w(16).In, w(12).address, w.load]
    OUT = [w(16).out]

    PARTS = [
        DMux8Way(In=w.load, sel=w.address[0:3], a=w.l0, b=w.l1, c=w.l2, d=w.l3, e=w.l4, f=w.l5, g=w.l6, h=w.l7),
    ]

    for i in range(8):
        PARTS.append(RAM512(In=w.In, load=getattr(w, f"l{i}"), address = w.address[3:12], out=getattr(w(16), f"r{i}")))

    PARTS.append(Mux8Way16(a=w.r0, b=w.r1, c=w.r2, d=w.r3, e=w.r4, f=w.r5, g=w.r6, h=w.r7, sel=w.address[0:3], out=w.out))