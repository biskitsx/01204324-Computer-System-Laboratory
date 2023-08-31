class Joy05(Joy04):

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
        expr_const: NUMBER
        expr_id: ID

        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /(-[0-9]+)|([0-9]+)/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''

    def stmt_if_else(self, tree):
        [expr, if_body, else_body] = tree.children

        # if part
        label = self.gen_label_no()

        self._asm.append(f'''
            //## begin-if-{label} ##
        ''')

        self.visit(expr)
        self._asm.append(f'''
            @THIS
            D=M
            @.endif.{label}
            D;JEQ
        ''')

        self._asm.append(f'''
            //## if-body-{label} ##
        ''')

        self.visit(if_body)

        self._asm.append(f'''
            @.endelse.{label}
            0;JMP
        ''')

        self._asm.append(f'''
            //## end-if-{label} ##
            (.endif.{label})
        ''')

        # else part
        self._asm.append(f'''
            //## begin-else-{label} ##
            //## else-body-{label} ##
        ''')
        self.visit(else_body)
        self._asm.append(f'''
            //## end-else-{label} ##
            (.endelse.{label})
        ''')
