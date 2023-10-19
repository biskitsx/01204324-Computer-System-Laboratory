# DO NOT ERASE THIS CELL - to be graded

LIB_STDIO = '''
// นิยามตัวแปรโกลบอลที่ต้องใช้ตามต้องการ
let cursor_x = 0;
let cursor_y = 0;

/////////////////////////////////////////////////////////////
def putc(c) {
  global cursor_x ;
  global cursor_y ;
  global FONT ;
  if (c == 10) {
    let cursor_y = cursor_y + 1 ;
  }

  if (c == 13) {
    let cursor_x = 0;
  }

  if (c >= 32 && c <= 126) {

    draw_glyph(cursor_x, cursor_y, *(FONT+c-32));
    let cursor_x = cursor_x + 1;
  }
  
  // drawn
  
  if (cursor_x > 31) {
    let cursor_x = 0;
    let cursor_y = cursor_y + 1 ;
  }
  if (cursor_y > 15) {
    scroll(1);
    let cursor_x = 0;
    let cursor_y = cursor_y -1 ;
  }
}

/////////////////////////////////////////////////////////////
def print(s) {
    let c = 0;
    let val = *(s+c);
    while (val != 0) {
        putc(val);
        let c = c + 1;
        let val = *(s+c);
    }
}

/////////////////////////////////////////////////////////////
def println(s) {
    print(s);
    putc(10);
    putc(13);
}

/////////////////////////////////////////////////////////////
def clrscr() {
    global cursor_x;
    global cursor_y;

    scroll(16);

    let cursor_x = 0;
    let cursor_y = 0;
}

'''
