# DO NOT ERASE THIS CELL - to be graded

class Joy11(Joy10):
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
        expr_const: NUMBER
        expr_id: ID
        expr_add: expr "+" expr
        expr_sub: expr "-" expr
        expr_negate: "-" expr
        expr_compare: expr COMPARE_OP expr
        expr_and: expr "&&" expr
        expr_or: expr "||" expr
        expr_not: "!"expr


        COMPARE_OP: ">=" | "<=" | "==" | ">" | "<" | "!="
        ID: /[_A-Za-z][_0-9A-Za-z]*/
        NUMBER: /-?[0-9]+/
        WS: /[ \t\f\r\n]+/
        COMMENT: "//" /[^\r\n]*[\r\n]?/
        %ignore COMMENT
        %ignore WS
    '''