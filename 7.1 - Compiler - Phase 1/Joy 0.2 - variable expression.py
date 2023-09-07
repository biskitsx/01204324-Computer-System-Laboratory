class Joy02(Joy01):

    GRAMMAR = r'''
        program: statements
        statements: statement*
        statement: stmt_assign
        stmt_assign: "let" ID "=" expr ";"
        expr: expr_const
            | expr_id
        expr_const: NUMBER
        expr_id: ID

        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /[0-9]+/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''

    # override Joy01's stmt_assign
    def stmt_assign(self, tree):
        [id, expr] = tree.children
        self.visit(expr)
        # THIS should store expr's value; move it to id
        self.gen_move(f'.var.{id}', 'THIS')

    def expr_const(self, tree):
        [const] = tree.children
        value = int(const)
        self.gen_load_const('THIS', value)

    def expr_id(self, tree):
        [id] = tree.children
        # make THIS store the value referenced by id
        self.gen_move('THIS', f'.var.{id}')