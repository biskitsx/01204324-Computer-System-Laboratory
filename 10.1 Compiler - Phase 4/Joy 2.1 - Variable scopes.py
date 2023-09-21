# DO NOT ERASE THIS CELL - to be graded

class Joy21(Joy20):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._scope = None
        self._globals = set()

    def get_var_label(self, var, func=None):
        if func is not None:
            return f'.local.{func}.{var}'
        elif self._scope == None or var in self._globals:
            return f'.global.{var}'
        else:
            return f'.local.{self._scope}.{var}'

    def stmt_assign(self, tree):
        [id, expr] = tree.children
        self.visit(expr)
        if (id in self._globals):
          return self.gen_move(self.get_var_label(id), 'THIS')
        self.gen_move(self.get_var_label(id, func=self._scope), 'THIS')

    def expr_id(self, tree):
        [id] = tree.children
        if (id in self._globals):
          return self.gen_move('THIS', self.get_var_label(id))
        self.gen_move('THIS', self.get_var_label(id, func=self._scope))

    # แก้ไขเมท็อดที่สร้างโค้ดสำหรับตัวดำเนินการ &
    # *** ใส่โค้ดของตนเอง ***
    def expr_deref(self, tree):
        [ID] = tree.children
        if self._scope == None or ID in self._globals:
          self._asm.append(f'''
            @.global.{ID}
          ''')
        else :
          self._asm.append(f'''
            @.local.{self._scope}.{ID}
          ''')

        self._asm.append(f'''
          D=A
          @THIS
          M=D
        ''')
