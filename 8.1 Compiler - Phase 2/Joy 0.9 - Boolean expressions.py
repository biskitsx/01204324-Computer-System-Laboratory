# DO NOT ERASE THIS CELL - to be graded

class Joy09(Joy08):

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
            | expr_not
            | expr_id
            | expr_add
            | expr_sub
            | expr_negate
            | "(" expr ")"
            | expr_compare
            | expr_and
            | expr_or
        expr_const: NUMBER
        expr_id: ID
        expr_add: expr "+" expr
        expr_sub: expr "-" expr
        expr_negate: "-" expr
        expr_compare: expr COMPARE_OP expr
        expr_and: expr "&&" expr
        expr_or: expr "||" expr
        expr_not: "!"expr


        COMPARE_OP: ">=" | "<=" | "==" | ">" | "<" | "!="
        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /-?[0-9]+/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''


    def expr_and(self, tree):
      [expr1, expr2] = tree.children
      self.visit(expr1)
      self.gen_push('THIS')
      self.visit(expr2)
      self.gen_pop('THAT')

      label = self.gen_label_no()
      # convert expr to 0 or 1
      self._asm.append(f'''
         @THIS
         D=M
         @.false.{label}
         D;JEQ
         @THAT
         D=M
         @.false.{label}
         D;JEQ

         @THIS
         M=1
         @.true.{label}
         0;JMP

         (.false.{label})
         @THIS
         M=0
         (.true.{label})
      ''')

    def expr_or(self, tree):
      [expr1, expr2] = tree.children
      self.visit(expr1)
      self.gen_push('THIS')
      self.visit(expr2)
      self.gen_pop('THAT')

      label = self.gen_label_no()
      # convert expr to 0 or 1
      self._asm.append(f'''
         @THIS
         D=M
         @.true.{label}
         D;JNE
         @THAT
         D=M
         @.true.{label}
         D;JNE

         @THIS
         M=0
         @.false.{label}
         0;JMP

         (.true.{label})
         @THIS
         M=1
         (.false.{label})
      ''')

    def expr_not(self, tree):
      [expr] = tree.children

      self.visit(expr)
      label = self.gen_label_no()

      self._asm.append(f'''
        @THIS
        D=M
        @.true.{label}
        D;JEQ

        @THIS
        M=0
        @.false.{label}
        0;JMP

        (.true.{label})
        @THIS
        M=1
        (.false.{label})
      ''')