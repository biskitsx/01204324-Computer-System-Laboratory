class JumpHelper(Component):
  IN=[w.c, w.j2, w.j1, w.j0, w.ng, w.zr]
  OUT=[w.out]

  PARTS = [
      Or(a=w.ng, b=w.zr, out=w.psDumb),
      Not(In=w.psDumb, out=w.ps),
      And(a=w.j2, b=w.ng, out=w.out1),
      And(a=w.j1, b=w.zr, out=w.out2),
      And(a=w.j0, b=w.ps, out=w.out3),
      Or(a=w.out1, b=w.out2, out=w.out4),
      Or(a=w.out3, b=w.out4, out=w.out5),
      And(a=w.c, b=w.out5, out=w.out)
  ]
  
class CPU(Component):
    """
    Template for building CPU.
    """

    IN = [
        w(16).instruction,
        w(16).inM,
        w.reset,
    ]
    OUT = [
        w(16).outM,
        w(15).addressM,
        w.writeM,
        w(15).pc,
        w(16).outA,
        w(16).outD,
    ]

    PARTS = [
        # PC
        PC(In=w.outA, load=w.loadPc, reset=w.reset, inc=w.one ,out=w(16).pcOut),
        Buffer15(In=w.pcOut[0:15], out=w.pc),

        # Register A
        And(a=w.instruction[5], b=w.instruction[15], out=w.contRegisterA1),
        Not(In=w.instruction[15], out=w.contRegisterA2),
        Or(a=w.contRegisterA1, b=w.contRegisterA2, out=w.contRegisterA),


        Mux16(a=w.instruction, b=w(16).aluOut, sel=w.instruction[15], out=w(16).registerAinput),
        RegisterA(In=w.registerAinput, out=w.outA, load=w.contRegisterA),

        # Register D
        And(a=w.instruction[4], b=w.instruction[15], out=w.contRegisterD),
        Register(In=w.aluOut, out=w.outD, load=w.contRegisterD),

        # ALU
        And(a=w.instruction[15], b=w.instruction[12], out=w.selMuxAlu),
        Mux16(a=w.outA, b=w.inM, sel=w.selMuxAlu, out=w(16).aluRegisterA), 
        ALU(x=w.outD, y=w.aluRegisterA, out=w.aluOut, zx=w.instruction[11], nx=w.instruction[10], zy=w.instruction[9], ny=w.instruction[8] ,f=w.instruction[7], no=w.instruction[6], zr=w.zr, ng=w.ng),
        JumpHelper(c=w.instruction[15], j2=w.instruction[2], j1=w.instruction[1], j0=w.instruction[0], ng=w.ng, zr=w.zr, out=w.loadPc),

        # address M & Write M
        Buffer15(In=w.outA[0:15], out=w.addressM),
        And(a=w.instruction[3], b=w.instruction[15], out=w.writeM),
        Buffer16(In=w.aluOut, out=w.outM),
    ]
