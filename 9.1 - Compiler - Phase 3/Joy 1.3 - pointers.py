# DO NOT ERASE THIS CELL - to be graded

class Joy13(Joy12):
    GRAMMAR = r'''
        program: statements
        statements: statement*
        statement: stmt_assign
                 | stmt_if
                 | stmt_if_else
                 | stmt_while
                 | stmt_until
                 | stmt_assign_deref
        stmt_assign: "let" ID "=" expr ";"
        stmt_assign_deref: "let" "*" expr "=" expr ";"
        stmt_if: "if" expr "{" statements "}"
        stmt_if_else: "if" expr "{" statements "}" "else" "{" statements "}"
        stmt_while: "while" expr "{" statements "}"
        stmt_until: "until" expr "{" statements "}"
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
            | expr_ref
            | expr_deref

        expr_const: CONST
        expr_id: ID
        expr_add: expr "+" expr
        expr_sub: expr "-" expr
        expr_negate: "-" expr
        expr_compare: expr COMPARE_OP expr
        expr_and: expr "&&" expr
        expr_or: expr "||" expr
        expr_not: "!"expr
        expr_ref: "*" expr
        expr_deref: "&" ID

        CONST:  BINARY| HEXADECIMAL| CHAR | NUMBER
        BINARY: /0b[01]+/
        HEXADECIMAL: /0x[0-9a-fA-F]+/
        NUMBER: /-?[0-9]+/
        CHAR: /'[^']'/

        COMPARE_OP: ">=" | "<=" | "==" | ">" | "<" | "!="
        ID: /[_A-Za-z][_0-9A-Za-z]*/
        WS: /[ \t\f\r\n]+/
        COMMENT: "//" /[^\r\n]*[\r\n]?/
        %ignore COMMENT
        %ignore WS
    '''

    # *
    def expr_ref(self, tree):
        [expr] = tree.children
        self.visit(expr)
        self._asm.append(f'''
          @THIS
          A=M
          D=M
          @THIS
          M=D
        ''')
    # &
    def expr_deref(self, tree):
        [ID] = tree.children
        self._asm.append(f'''
          @.var.{ID}
          D=A
          @THIS
          M=D
        ''')

    def stmt_assign_deref(self, tree):
        [expr1, expr2] = tree.children
        self.visit(expr1)
        self.gen_push('THIS')
        self.visit(expr2)
        self.gen_pop('THAT')

        # THAT = expr1 , THIS = expr2
        self._asm.append(f'''
          @THIS
          D=M
          @THAT
          A=M
          M=D
        ''')