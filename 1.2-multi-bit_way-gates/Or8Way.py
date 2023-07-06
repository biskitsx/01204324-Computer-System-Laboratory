# DO NOT ERASE THIS CELL - to be graded

class Or8Way(Component):
    IN = [w(8).In]
    OUT = [w.out]

    PARTS = [
        Or(a=w.In[0], b=w.In[1], out=w(4).or_out[0]),
        Or(a=w.In[2], b=w.In[3], out=w.or_out[1]),
        Or(a=w.In[4], b=w.In[5], out=w.or_out[2]),
        Or(a=w.In[6], b=w.In[7], out=w.or_out[3]),
        Or(a=w.or_out[0], b=w.or_out[1], out=w(2).or_out2[0]),
        Or(a=w.or_out[2], b=w.or_out[3], out=w.or_out2[1]),
        Or(a=w.or_out2[0], b=w.or_out2[1], out=w.out)
    ]
