# DO NOT ERASE THIS CELL - to be graded

class Selecter(Component):
  IN = [w(15).In]
  OUT = [w.ram, w.screen, w.kbd]

  PARTS =[
      DMux4Way(In=w.one, a=w.ram1, b=w.ram2, c=w.screen, d=w.kbd, sel=w.In[13:15]),
      Or(a=w.ram1, b=w.ram2, out=w.ram)
  ]

class Encoder3To2(Component):
  IN = [w.In1, w.In2, w.In3]
  OUT = [w(2).out]

  PARTS = [
      Or(a=w.In1, b=w.In3, out=w.out[0]),
      Or(a=w.In2, b=w.In3, out=w.out[1])
  ]

class Memory(Component):
    IN = [w(16).In, w.load, w(15).address]
    OUT = [w(16).out]

    PARTS = [
      Selecter(In=w.address, ram=w.ram, screen=w.screen, kbd=w.kbd),
      And(a=w.load, b=w.ram, out=w.loadRam),
      And(a=w.load, b=w.screen, out=w.loadScreen),
      Encoder3To2(In1=w.ram, In2=w.screen, In3=w.kbd, out=w(2).selOut),
      RAM16K(In=w.In, address=w.address[0:14], load=w.loadRam, out=w(16).ramOut),
      Screen(In=w.In, address=w.address[0:13], load=w.loadScreen, out=w(16).screenOut),
      Keyboard(out=w(16).keyboardOut),
      Mux4Way16(a=w(16).zero, b=w.ramOut, c=w.screenOut, d=w.keyboardOut, sel=w.selOut, out=w.out)
  ]