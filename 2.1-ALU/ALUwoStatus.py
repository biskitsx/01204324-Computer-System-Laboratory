# DO NOT ERASE - to be graded
class ALUwoStatus(Component):
    IN = [w(16).x, w(16).y,
          w.zx, w.nx,
          w.zy, w.ny,
          w.f,
          w.no]

    OUT = [w(16).out]

    PARTS = [

        # part 1
        Mux16(a=w.x, b=w(16).zero, sel=w.zx, out=w(16).ox1),
        Mux16(a=w.y, b=w(16).zero, sel=w.zy, out=w(16).oy1),


        # part 2
        Not16(In=w.ox1, out=w(16).oxnot),
        Not16(In=w.oy1, out=w(16).oynot),
        Mux16(a=w.ox1, b=w.oxnot, sel=w.nx, out=w(16).ox2),
        Mux16(a=w.oy1, b=w.oynot, sel=w.ny, out=w(16).oy2),

        # part 3
        And16(a=w.ox2, b=w.oy2, out=w(16).o1),
        Add16(a=w.ox2, b=w.oy2, out=w(16).o2),
        Mux16(a=w.o1, b=w.o2, sel=w.f, out=w(16).o3),

        # part 4
        Not16(In=w.o3, out=w(16).o3not),
        Mux16(a=w.o3, b=w.o3not, sel=w.no, out=w.out),

    ]
