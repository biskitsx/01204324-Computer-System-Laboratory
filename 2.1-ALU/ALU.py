# DO NOT ERASE THIS CELL - to be graded

class ALU(Component):
    IN = [w(16).x, w(16).y,
          w.zx, w.nx,
          w.zy, w.ny,
          w.f,
          w.no]

    OUT = [w(16).out, w.zr, w.ng]

    PARTS = [
        ALUwoStatus(x=w.x, y=w.y, zx=w.zx, nx=w.nx, zy=w.zy, ny=w.ny, f=w.f, no=w.no, out=w.out),
        
        # negative
        Buffer(In=w.out[15], out=w.ng),

        # Zero
        Or8Way(In= w.out[0:8],out=w.z1 ),
        Or8Way(In= w.out[8:16],out=w.z2 ),
        Or(a=w.z1, b=w.z2, out=w.z3),
        Not(In=w.z3, out=w.zr)
    ]