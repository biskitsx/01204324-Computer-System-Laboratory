# DO NOT ERASE THIS CELL - to be graded

from lark import Tree, Token

class Joy23(Joy22):

    # ปรับปรุงแกรมมาร์จาก Joy 2.2 โดยเพิ่มกฎสำหรับนิพจน์ *, /, % ตามที่อธิบายไว้ข้างต้นให้เรียบร้อย
    # *** ใส่โค้ดของตนเอง ***
    GRAMMAR = r'''
        program: (funcdef | statement)*
        statements: statement*
        funcdef: "def" ID "(" params ")" "{" globals statements "}"
        statement: stmt_assign
                 | stmt_if
                 | stmt_if_else
                 | stmt_while
                 | stmt_until
                 | stmt_assign_deref
                 | stmt_call
                 | stmt_return
        stmt_call: expr_call ";"
        stmt_return: "return" expr ";"
                 
        stmt_assign: "let" ID "=" expr ";"
        stmt_assign_deref: "let" "*" expr "=" expr ";"
        stmt_if: "if" expr "{" statements "}"
        stmt_if_else: "if" expr "{" statements "}" "else" "{" statements "}"
        stmt_while: "while" expr "{" statements "}"
        stmt_until: "until" expr "{" statements "}"
        params: ID ("," ID)*
              |
        globals: ("global" ID ";")*
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
            | expr_call
            | expr_muldiv
    
        expr_muldiv: expr MULDIV_OP expr    
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
        expr_call: ID "(" args ")"
        args: expr ("," expr)* 
            |

        MULDIV_OP: "*" | "/" | "%"
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

    RUNTIME = '''
        def _mul(a, b) {
            let result = 0;
            while b {
                let result = result + a;
                let b = b-1;
            }
            return result;
        }

        def _div(a, b) {
            let result = 0;
            until a < b {
                let result = result + 1;
                let a = a-b;
            }
            return result;
        }

        def _mod(a, b) {
            until a<b {
                let a = a-b;
            }
            return a;
        }
        '''

    def expr_muldiv(self, tree):
        [expr1, op, expr2] = tree.children
        funcmap = {
            '*' : '_mul',
            '/' : '_div',
            '%' : '_mod',
        }
        func = funcmap[op]
        tree = Tree('expr_call', [
            Token('ID', func),
            Tree('args', [expr1, expr2]),
        ])
        self.visit(tree)