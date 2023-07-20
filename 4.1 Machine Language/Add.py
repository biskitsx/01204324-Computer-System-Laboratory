# DO NOT ERASE THIS CELL - to be graded
Add_asm = '''
  @R0
    D=M
  @R1
    D=D+M
  @R2
    M=D

// Do not remove the following three lines
(END)
    @END
    0;JMP
'''