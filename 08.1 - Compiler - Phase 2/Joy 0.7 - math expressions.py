# DO NOT ERASE THIS CELL - to be graded

class Joy07(Joy06):

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
        expr_const: NUMBER
        expr_id: ID
        expr_add: expr "+" expr
        expr_sub: expr "-" expr
        expr_negate: "-" expr

        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /-?[0-9]+/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''


    # add your rule processing methods here
    def expr_sub(self, tree):
        [expr1, expr2] = tree.children
        self.visit(expr1)
        self.gen_push('THIS')
        self.visit(expr2)
        self.gen_pop('THAT')
        self._asm.append('''
            // [THIS] <- [THAT] - [THIS]
            @THAT
            D=M
            @THIS
            M=D-M
        ''')
        
    def expr_negate(self, tree):
        [expr] = tree.children
        self.visit(expr)
        self._asm.append('''
            @THIS
            M=-M
        ''')
