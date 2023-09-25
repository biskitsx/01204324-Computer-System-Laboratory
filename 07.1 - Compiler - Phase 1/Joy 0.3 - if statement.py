class Joy03(Joy02):

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
        NUMBER: /[0-9]+/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._label_count = 0  # keep track of generated jump labels

    def gen_label_no(self):
        self._label_count += 1
        return self._label_count

    def stmt_if(self, tree):
        [expr, if_body] = tree.children
        label = self.gen_label_no()
        self._asm.append(f'''
            //## begin-if-{label} ##
        ''')
        self.visit(expr)
        # expr result is in THIS; if it is zero, jump over the body to the end-if label
        self._asm.append(f'''
            @THIS
            D=M
            @.endif.{label}
            D;JEQ
        ''')
        # generate the body by visiting the statements node
        self._asm.append(f'''
            //## if-body-{label} ##
        ''')
        self.visit(if_body)
        # place the end-if label here
        self._asm.append(f'''
            //## end-if-{label} ##
            (.endif.{label})
        ''')