# DO NOT ERASE THIS CELL - to be graded

# replace with fast implementation
RAM4K = gen_fast_ram_component(12)

class RAM16K(Component):
    IN = [w(16).In, w(14).address, w.load]
    OUT = [w(16).out]

    PARTS = [
        DMux4Way(In=w.load, sel=w.address[0:2], a=w.l0, b=w.l1, c=w.l2, d=w.l3),
    ]

    for i in range(4):
        PARTS.append(RAM4K(In=w.In, load=getattr(w, f"l{i}"), address = w.address[2:14], out=getattr(w(16), f"r{i}")))

    PARTS.append(Mux4Way16(a=w.r0, b=w.r1, c=w.r2, d=w.r3, sel=w.address[0:2], out=w.out))