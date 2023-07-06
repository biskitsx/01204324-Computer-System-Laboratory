# DO NOT ERASE THIS CELL - to be graded

class Not(NotLayoutMixin, Component):
    IN = [w.In]
    OUT = [w.out]

    PARTS = [
        Nand(a=w.In, b=w.In, out=w.out)
    ]