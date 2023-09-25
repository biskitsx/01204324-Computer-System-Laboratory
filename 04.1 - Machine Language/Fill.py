# DO NOT ERASE THIS CELL - to be graded
Fill_asm = '''
// Put your code here.

(WHILE)
  @KBD
    D=M
  @BLACK
    D;JNE
  @WHITE
    0;JMP

(BLACK)
  @j
    M=0
  @i
    D=M
  @SCREEN
    A=D+A     // A = SCREEN+i
    M=-1      // M[SCREEN+i] = -1 
  @i
    M=M+1
  @WHILE
    0;JMP

 (WHITE)
  @i
    M=0
  @j
    D=M
  @SCREEN
    A=D+A     // A = SCREEN+j
    M=0      // M[SCREEN+j] = 0
  @j
    M=M+1
  @WHILE
    0;JMP
'''