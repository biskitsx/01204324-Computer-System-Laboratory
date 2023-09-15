# DO NOT ERASE THIS CELL - to be graded

class Joy20(Joy13):
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
            | expr_string
            | expr_array
            
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
        expr_string: STRING
        expr_array: "[" expr ("," expr)* "]"

        STRING: /"([^"]*)"/
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.string_count = 0 
        self.array_count = 0 
    
    def gen_string(self):
        self.string_count += 1
        return self.string_count
    
    def gen_array(self):
        self.array_count += 1
        return self.array_count

    def expr_string(self, tree):
        [stringWithDoubleQuoat] = tree.children
        string = stringWithDoubleQuoat[1:-1]
        size = len(string)
        string_number = self.gen_string()
        for i, char in enumerate(string):
          val = ord(char)
          self._asm.append(f'''
            @{val}
            D=A
            @.string.{string_number}.{i}
            M=D                          
          ''')
        self._asm.append(f'''
          @.string.{string_number}.{size}
          M=0 
          @.string.{string_number}.0
          D=A
          @THIS
          M=D
        ''')

    def expr_array(self, tree):
        array  = tree.children
        size = len(array)
        array_number = self.gen_array()

        # จองพื้นที่ !!!
        for i in range(size):
          self._asm.append(f'''
            @.array.{array_number}.{i}
          ''')

        # ใส่ค่า !
        for i, expr in enumerate(array):
          self.visit(expr)
          self._asm.append(f'''
            @THIS
            D=M
            @.array.{array_number}.{i}
            M=D
          ''')

        self._asm.append(f'''
          @.array.{array_number}.0
          D=A
          @THIS
          M=D
        ''')