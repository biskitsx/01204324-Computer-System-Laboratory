# DO NOT ERASE THIS CELL - to be graded

class Joy22(Joy21):

    # วางแกรมมาร์ที่มีการปรับเปลี่ยนจาก Joy 2.0 ของตนเองให้รองรับฟังก์ชัน
    # ตามที่ระบุข้างต้นเรียบร้อยแล้ว
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
        # นิยามตัวแปรสมาชิกเพิ่มเติมตามต้องการ เช่น dict สำหรับเก็บรายการฟังก์ชันที่นิยามไปแล้ว
        # พร้อมข้อมูลพารามิเตอร์
        # *** ใส่โค้ดของตนเอง ***
        self._func = {}

    def expr_call(self, tree):
        [funcname, args] = tree.children

        # ตรวจสอบว่าฟังก์ชันที่เรียกมีการนิยามหรือยัง
        # หากไม่มีให้สั่ง raise JoyUndefinedFunctionException()
        # *** ใส่โค้ดของตนเอง ***
        parameters = self._func.get(funcname.value) 
        if parameters == None :
          raise JoyUndefinedFunctionException()

        # ตรวจสอบจำนวนอาร์กิวเมนต์ ซึ่งต้องเท่ากับจำนวนพารามิเตอร์
        # หากไม่เท่าให้สั่ง raise JoyParamMismatchException()
        # *** ใส่โค้ดของตนเอง ***
        parameterCount = len(parameters)
        argumentCount = len(args.children)
        if parameterCount != argumentCount:
          raise JoyParamMismatchException()

        self._asm.append(f'''
          // CALL FUNC => [{funcname.value}]
        ''')
        # สร้างโค้ดคำนวณอาร์กิวเมนต์แต่ละค่า แล้วบันทึกไว้ในพารามิเตอร์แต่ละตัวของฟังก์ชันผู้ถูกเรียก
        # (ใช้ get_var_label() แบบระบุชื่อฟังก์ชันได้)
        # *** ใส่โค้ดของตนเอง ***
        for i, arg in enumerate(args.children): 
          var_label = self.get_var_label(parameters[i], func=funcname.value)
          self.visit(arg)
          self._asm.append(f'''
            @THIS
            D=M
            @{var_label}
            M=D
          ''')

        # push ค่าปัจจุบันของ LCL ลงสแต็ก
        # *** ใส่โค้ดของตนเอง ***
        self.gen_push('LCL')

        # บันทึกค่า return address ไว้ใน LCL ซึ่งได้มาจากลาเบลที่กำลังจะ
        # วางไว้ต่อจากโค้ดกระโดดไปยังฟังก์ชัน
        # *** ใส่โค้ดของตนเอง ***
        label = self.gen_label_no()
        self._asm.append(f'''
          @.return.address.{label}
          D=A
          @LCL
          M=D
        ''')

        # สร้างโค้ดกระโดดไปยังจุดเริ่มต้นของฟังก์ชันผู้ถูกเรียก
        # *** ใส่โค้ดของตนเอง ***
        self._asm.append(f'''
          @.begin.func.{funcname.value}
          0;JMP
        ''')
        # วางลาเบลที่ใช้เป็น return address (ระวังอย่าให้ชื่อลาเบลซ้ำ)
        # *** ใส่โค้ดของตนเอง ***
        self._asm.append(f'''
            (.return.address.{label})
          ''')
        
        # pop ค่า LCL เดิมที่เคยบันทึกไว้ออกมาจากสแต็
        # *** ใส่โค้ดของตนเอง ***
        self.gen_pop('LCL')
        self._asm.append(f'''
          // CALL FUNC => [{funcname.value}]
          ''')
        

    def funcdef(self, tree):
        [funcname, params, globals, statements] = tree.children

        # ตรวจสอบว่าชื่อฟังก์ชันซ้ำกับที่เคยนิยามมาแล้วหรือไม่
        # หากพบว่าซ้ำให้สั่ง raise JoyMultiplyDefinedFunctionException()
        # *** ใส่โค้ดของตนเอง ***

        parameters = self._func.get(funcname.value) 
        if parameters != None :
          raise JoyMultiplyDefinedFunctionException()

        # ตั้ง _scope ให้เป็นชื่อฟังก์ชัน
        self._scope = funcname.value

        # เก็บรายชื่อตัวแปรโกลบอลลงในเซ็ต _global ที่นิยามไว้ใน ​Joy 2.1
        for g in globals.children:
            self._globals.add(g.value)

        # บันทีกข้อมูลเกี่ยวกับฟังก์ชัน เพื่อใช้ตรวจสอบในภายหลัง เช่น ชื่อฟังก์ชัน จำนวนพารามิเตอร์ ฯลฯ
        # *** ใส่โค้ดของตนเอง ***
        self._func[funcname.value] = []
        for p in params.children:
          self._func[funcname.value].append(p.value)

        # สร้างโค้ดให้กระโดดข้ามฟังก์ชันบอดี้ไปยังท้ายฟังก์ชัน
        # (เพื่อป้องกันไม่ให้ฟังก์ชันทำงานระหว่างการนิยาม)
        # *** ใส่โค้ดของตนเอง ***
        self._asm.append(f'''
          // DEF FUNC => [{funcname.value}]
          @.end.func.{funcname.value}
          0;JMP
        ''')

        # วางลาเบลระบุจุดเริ่มต้นของฟังก์ชันเพื่อให้ผู้เรียกกระโดดมาที่จุดนี้เมื่อพบคำสั่งเรียกฟังก์ชัน
        # (ระวังอย่าให้ชื่อลาเบลซ้ำ)
        # *** ใส่โค้ดของตนเอง ***
        self._asm.append(f'''
          (.begin.func.{funcname.value})
        ''')

        # สร้างโค้ดสำหรับบอดี้ของฟังก์ชัน (อยู่ในตัวแปร statements ที่ดึงมาจาก parse tree)
        # *** ใส่โค้ดของตนเอง ***
        self.visit(statements)

        # วางลาเบลเพื่อใช้เป็นจุดกระโดดออกจากฟังก์ชัน
        # *** ใส่โค้ดของตนเอง ***
        self._asm.append(f'''
          (.return.func.{funcname.value})
        ''')
        # สร้างโค้ดกระโดดกลับไปยังผู้เรียก โดยดึง return address จาก LCL
        # *** ใส่โค้ดของตนเอง ***

        self._asm.append(f'''
          @LCL
          A=M
          0;JMP
        ''')


        # วางลาเบลปิดท้ายฟังก์ชันเพื่อใช้เป็นจุดกระโดดข้ามฟังก์ชันบอดี้ระหว่างการนิยามฟังก์ชัน
        # *** ใส่โค้ดของตนเอง ***
        self._asm.append(f'''
          (.end.func.{funcname.value})
          // END DEF FUNC => [{funcname.value}]
        ''')
        # กำหนด _scope ให้เป็นโกลบอลดังเดิม และล้างรายการตัวแปรโกลบอลออกจากเซ็ต _globals
        self._scope = None
        self._globals.clear()

    def stmt_return(self, tree):
        # ตรวจสอบว่าอยู่ในสโคปของฟังก์ชันหรือไม่ หากเป็นโกลบอลสโคป (_scope เป็น None)
        # ให้สั่ง raise JoyReturnOutsideFunctionException()
        [expr] = tree.children
        if self._scope == None:
            raise JoyReturnOutsideFunctionException()

        # สร้างโค้ดประมวลผลค่า expr ซึ่งผลลัพธ์จะต้องอยู่ในรีจีสเตอร์ THIS ตามที่ต้องการอยู่แล้ว
        # *** ใส่โค้ดของตนเอง ***
        self.visit(expr)

        # สร้างโค้ดกระโดดไปยังลาเบลที่เตรียมออกจากฟังก์ชัน
        # *** ใส่โค้ดของตนเอง ***
        self._asm.append(f'''
          @.return.func.{self._scope}
          0;JMP
        ''')
