# DO NOT ERASE THIS CELL - to be graded

class Joy30(Joy23):

    # แก้ไขแกรมมาร์ Joy 2.2 เพื่อให้รองรับการตีความนิพจน์ให้เป็นไปตามลำดับความสำคัญของ
    # ตัวดำเนินการตามที่กำหนดไว้ข้างต้น
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
            | expr_id
            | "(" expr ")"
            | expr_deref
            | expr_string
            | expr_array
            | expr_call
            | expr_p5

        expr_p5: expr_or | expr_p4
        expr_p4: expr_and | expr_p3
        expr_p3: expr_compare | expr_p2
        expr_p2: expr_add| expr_sub | expr_p1
        expr_p1: expr_muldiv | expr_p0
        expr_p0: expr_not| expr_negate| expr_ref | expr
        
        // priority 5
        expr_or: expr_or "||" expr | expr "||" expr 

        // priority 4
        expr_and: expr_and "&&" expr | expr "&&" expr 

        // priority 3
        expr_compare: expr_compare COMPARE_OP expr |expr COMPARE_OP expr 

        // priority 2
        expr_add: expr_add "+" expr |expr "+" expr 
        expr_sub: expr_sub "-" expr | expr "-" expr 

        // priority 1
        expr_muldiv: expr_muldiv MULDIV_OP expr | expr MULDIV_OP expr 

        // priority 0
        expr_negate: "-" expr 
        expr_not: "!" expr 
        expr_ref: "*" expr 

        expr_deref: "&" ID
        expr_const: CONST
        expr_string: STRING
        expr_id: ID
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
