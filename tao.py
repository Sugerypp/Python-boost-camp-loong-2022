import turtle
import random
#สร้างตัวเต่า
t = turtle.Pen()

#เปลี่ยนรูปให้กลายเป็นเต่า
t.shape('turtle')

#เปลี่ยนสี
t.color('red')

#กลุ่มสี
color_list = ['red','green','blue','orange']

def rectangle(size):
    ''' ฟั่งชั่นนี้ใช้สำหรับวาดสี่เหลี่ยม โดยใส่ size ลงไปด้วย
    วิธีการรันทำได้เหมือนตัวอย่างดังนี้ '''
    t.fd(size)
    t.left(90)
    t.fd(size)
    t.left(90)
    t.fd(size)
    t.left(90)
    t.fd(size)
    t.left(90)

def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# Run
for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    z = random.choice(color_list)
    s = random.randint(50,100)
    t.color(z)
    goto(x,y)

    #เทสีหรือไม่เทสี
    f = random.choice([True,False])
    Sh = random.choice([True,False])
    if f == True:
        t.begin_fill()
        if Sh == True:
            rectangle(s)
        else :
            t.circle(s)
        t.end_fill()
    else :
        if Sh == True:
            rectangle(s)
        else :
            t.circle(s)
        




