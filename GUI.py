#GUI.py

from tkinter import  * 
from tkinter import  messagebox , ttk 

friend =    {'somchai' : 'สมชาย ดีมาก',
            'somsak' : 'สมศักดิ์ เก่งมาก',
            'somsri' : 'สมศรี เยี่ยมมาก'}

GUI = Tk()
GUI.title('โปรแกรมของฉัน')
GUI.geometry('500x300')

v_text = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_text ,font=('Angsana New',20))
E1.pack(pady=10)

def Click():
        text = v_text.get() #ดึงข้อความที่ user พิมพ์ออกมา
        print('Text: ',text)
        if text in friend:
            result = friend[text]
            messagebox.showinfo('Result','รหัส: {} คือชื่อ : {}'.format(text,result) )
        else:
            print('ไม่มีข้อมูลของคนนี้')
            messagebox.showinfo('Result: Error','ไม่มีข้อมูลในระบบ กรุณากรอกใหม่ หรือ เพิ่มข้อมูลในระบบ')
B1 = ttk.Button(GUI, text='Click me!',command=Click)
B1.pack(ipadx=50,ipady=30,pady=30) #ทำให้ติดเข้าไปในหน้าจอหลัก

GUI.mainloop()