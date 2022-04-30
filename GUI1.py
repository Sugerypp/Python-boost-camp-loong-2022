# GUI.py

from tkinter import *
from tkinter import ttk , messagebox

friend = {'somchai':'สมชาย ดีมาก',
          'somsak':'สมศักดิ์ เก่งมาก',
          'somsri':'สมศรี เยี่ยมมาก'}

GUI = Tk()
GUI.title('โปรแกรมของฉัน')
GUI.geometry('500x300')

L = Label(GUI,text='กรุณากรอกรหัสชื่อ',font=('Angsana New',20)).pack(pady=30)


v_text=StringVar() #ตัวแปรเก็บของมูลใน interphase
E1 =ttk.Entry(GUI, textvariable=v_text,font=('Angsana New',20))
E1.pack(pady=10)

def Click():
	text = v_text.get() #ดึงข้อความที่ user พิมพ์ออกมา
	print('Text: ',text)
	if text in friend:
		result = friend[text]
		print(friend[text])
		messagebox.showinfo('Result','รหัส: {} คือชื่อ: {}'.format(text,result))
	else:
		print('ไม่มีข้อมูลของคนนี้')
		messagebox.showinfo('ResultError','ไม่มีข้อมูลในระบบกรุณากรอกใหม่ หรือ เพิ่มข้อมูลในระบบ')


B1 = ttk.Button(GUI,text='Search' ,command=Click)
B1.pack(ipadx=20,ipady=10,pady=50)

GUI.mainloop()