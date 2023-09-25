# DO NOT ERASE THIS CELL - to be graded

class Joy12(Joy11):
    GRAMMAR = r'''
        program: statements
        statements: statement*
        statement: stmt_assign
                 | stmt_if
                 | stmt_if_else
                 | stmt_while
                 | stmt_until
        stmt_assign: "let" ID "=" expr ";"
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
        expr_const: CONST
        expr_id: ID
        expr_add: expr "+" expr
        expr_sub: expr "-" expr
        expr_negate: "-" expr
        expr_compare: expr COMPARE_OP expr
        expr_and: expr "&&" expr
        expr_or: expr "||" expr
        expr_not: "!"expr

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

    # override Joy11's expr_const
    def expr_const(self, tree):
        [const] = tree.children
        length = len(const)
        # print(const, length)
        if length == 3: # character
            if const[0] == "'":        
              return self.gen_load_const('THIS', ord(const[1]))        
        if (const[0:2] == "0x"):  
          return self.gen_load_const('THIS', int(const, 16))
        if (const[0:2] == "0b"):  
          return self.gen_load_const('THIS', int(const, 2))
        self.gen_load_const('THIS', int(const))
