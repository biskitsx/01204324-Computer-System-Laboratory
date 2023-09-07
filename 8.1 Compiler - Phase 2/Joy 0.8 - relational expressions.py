
# DO NOT ERASE THIS CELL - to be graded

class Joy08(Joy07):

    GRAMMAR = r'''
        program: statements
        statements: statement*
        statement: stmt_assign
                 | stmt_if
                 | stmt_if_else
        stmt_assign: "let" ID "=" expr ";"
        stmt_if: "if" expr "{" statements "}"
        stmt_if_else: "if" expr "{" statements "}" "else" "{" statements "}"
        expr: expr_const
            | expr_id
            | expr_add
            | expr_sub
            | expr_negate
            | "(" expr ")"
            | expr_compare
        expr_const: NUMBER
        expr_id: ID
        expr_add: expr "+" expr
        expr_sub: expr "-" expr
        expr_negate: "-" expr
        expr_compare: expr COMPARE_OP expr

        COMPARE_OP: ">=" | "<=" | "==" | ">" | "<" | "!="
        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /-?[0-9]+/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''

    def expr_compare(self, tree):
      [expr1, op, expr2] = tree.children
      self.visit(expr1)
      self.gen_push('THIS')
      self.visit(expr2)
      self.gen_pop('THAT')
      self._asm.append('''
        // [THIS] <- [THAT] - [THIS]
          @THAT
          D=M
          @THIS
          D=D-M
      ''')

      label = self.gen_label_no()
      self._asm.append(f'''
          // check condition
          @.truestart.{label}
      ''')

      if (op == ">="):
        self._asm.append('''
          D;JGE
        ''')
      elif (op == "<="):
        self._asm.append('''
          D;JLE
        ''')
      elif (op == "=="):
        self._asm.append('''
          D;JEQ
        ''')
      elif (op == ">"):
        self._asm.append('''
          D;JGT
        ''')
      elif (op == "<"):
        self._asm.append('''
          D;JLT
        ''')
      elif (op == "!="):
        self._asm.append('''
          D;JNE
        ''')
      # false part
      self._asm.append(f'''
          @THIS
          M=0
          @.trueend.{label}
          0;JMP
      ''')

      # true part
      self._asm.append(f'''
          (.truestart.{label})
          @THIS
          M=1
          (.trueend.{label})
      ''')