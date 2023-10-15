import tkinter

win=tkinter.Tk()
win.title=""
win.minsize(500,400)
win.config(bg='#231329')


label1=tkinter.Label(text="To-Do",width=43,font="Recoleta 15",bg='#231329',foreground='#d4c3c4')
label1.grid()

todo=tkinter.Entry()
todo.grid(pady=18)

add=tkinter.Button(width=10,text='ADD TASK')
add.grid(column=0)

rem=tkinter.Button(width=10,text='REMOVE')
rem.grid(row=3)

save=tkinter.Text(width=30)
save.grid(pady=18)

#box_frame = tkinter.Frame()
#box_frame.grid(width=30)

win.mainloop()