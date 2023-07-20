# DO NOT ERASE THIS CELL - to be graded
Mult_asm = '''
  @R1
    D=M
  @NEGATIVE
    D;JLT

  (CALCULATE)
    @R1
      M=M-1
      D=M
    @END
      D;JLT
    @R0
      D=M
    @R2
      M=D+M
    @CALCULATE
      0;JMP

  (NEGATIVE)
    @R0
      M=-M
    @R1
      M=-M
    @CALCULATE
    0;JMP

// Do not remove the following three lines
(END)
    @END
    0;JMP
'''