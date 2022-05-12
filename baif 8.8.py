from tkinter import*
a=Tk()
a.title('welcome')
a.geometry('300x400')
a.attributes("-topmost", True)

name1=Label(a,font=('Arial',10),text='Họ tên:')
name1.place(x=10,y=10)
entry1=Entry(a,width=30,font=('Times New Roman',10))
entry1.place(x=80,y=10)
entry1.focus()

name2=Label(a,font=('Arial',10),text='Ngày sinh:')
name2.place(x=10,y=50)
entry2=Entry(a,width=30,font=('Times New Roman',10))
entry2.place(x=80,y=50)
entry2.focus()

name3=Label(a,font=('Arial',10),text='MSV:')
name3.place(x=10,y=90)
entry3=Entry(a,width=30,font=('Times New Roman',10))
entry3.place(x=80,y=90)
entry3.focus()

name4=Label(a,font=('Arial',10),text='Ngành học:')
name4.place(x=10,y=130)
entry4=Entry(a,width=30,font=('Times New Roman',10))
entry4.place(x=80,y=130)
entry4.focus()



a.mainloop()
