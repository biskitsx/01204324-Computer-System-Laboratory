# DO NOT ERASE THIS CELL - to be graded
class Joy04(Joy03):

    GRAMMAR = r'''
        program: statements
        statements: statement*
        statement: stmt_assign
                 | stmt_if
        stmt_assign: "let" ID "=" expr ";"
        stmt_if: "if" expr "{" statements "}"
        expr: expr_const
            | expr_id
        expr_const: NUMBER
        expr_id: ID

        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /(-[0-9]+)|([0-9]+)/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''

    # Override Joy 0.3's gen_load_const()
    def gen_load_const(self, mem, val):

        if val < -32768 or val > 65535:
            raise Exception("Invalid integer literal")

        if (val == 65535):
            val = 0
            self._asm.append(f'''
              // [{mem}] <- {val}
              @{val}
              D=!A
              @{mem}
              M=D
          ''')

        elif (val >= 32768):
            val = val - 32767
            self._asm.append(f'''
              // [{mem}] <- {val}
              @{32767}
              D=A
              @{val}
              D=D+A
              @{mem}
              M=D
          ''')

        elif (val >= 0):
          self._asm.append(f'''
              // [{mem}] <- {val}
              @{val}
              D=A
              @{mem}
              M=D
          ''')

        elif (val >= -32767):
          val = val * -1
          self._asm.append(f'''
              // [{mem}] <- {val}
              @{val}
              D=-A
              @{mem}
              M=D
          ''')
        elif (val == -32768):
          val = 1
          self._asm.append(f'''
              // [{mem}] <- {val}
              @{32767}
              D=A
              @{val}
              D=D+A
              @{mem}
              M=D
          ''')
          


