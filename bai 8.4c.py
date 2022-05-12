from tkinter import*
a=Tk()
a.title('welcome')
a.geometry('300x400')
a.attributes("topmost", True)
name=Label(a,font=('Arial',14),text='Vi du',bg='red',fg='while')
name.place(x=30,y=30)

a.mainloop()
