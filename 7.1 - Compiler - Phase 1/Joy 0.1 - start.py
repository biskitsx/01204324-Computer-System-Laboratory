class Visitor(BaseVisitor):
    def program(self, tree):
        print('program node')
        self.visit(tree.children[0])  # 'program' has only one child

    def stmt_assign(self, tree):
        [id, number] = tree.children
        print(f'stmt_assign node: id={id.value}, number={number.value}')

class Joy01(BaseVisitor):

    GRAMMAR = r'''
        program: statements
        statements: statement*
        statement: stmt_assign
        stmt_assign: "let" ID "=" NUMBER ";"

        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /[0-9]+/
        WS: /[ \t\f\r\n]+/
        %ignore WS
    '''

    def __init__(self):
        self._asm = []  # for storing generated instructions
        self._parser = Lark(self.GRAMMAR, start='program')

    def parse(self, code):
        'Generate a parse tree from the specified Joy code'
        return self._parser.parse(code)

    def compile(self, code):
        'Generate Hack Assembly from the specified Joy code'
        tree = self.parse(code)
        self.visit(tree)
        return '\n'.join(self._asm)

    def gen_load_const(self, mem, val):
        '''
        Generate Hack assembly to load the memory location mem with the specified
        integer val, where 0 <= val <= 32767.
        '''
        if val < 0 or val > 32767:
            raise Exception("Invalid integer literal")
        self._asm.append(f'''
            // [{mem}] <- {val}
            @{val}
            D=A
            @{mem}
            M=D
        ''')

    def gen_move(self, dst, src):
        '''
        Generate Hack assembly to copy the memory location src to the memory
        location dst.
        '''
        self._asm.append(f'''
            // [{dst}] <- [{src}]
            @{src}
            D=M
            @{dst}
            M=D
        ''')

    def stmt_assign(self, tree):
        [id, number] = tree.children
        number = int(number)
        self.gen_load_const(id, number)