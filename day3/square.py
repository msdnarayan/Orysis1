import tkinter
win=tkinter.Tk()

def text():
    txt=int(name.get())
    sq=txt**2
    label1.config(text=f"square:{sq}")
win.title="GUI!"
win.minsize(600,400)

label2=tkinter.Label(text="Number:")
label2.grid(row = 4, column = 1)

label1=tkinter.Label(text="")
label1.grid(row = 10, column = 5)
name=tkinter.Entry()
name.grid(row = 4, column = 5)

btn=tkinter.Button(text="Submit",command=text,bg='#121047',foreground='#f2f2f2')
btn.grid(row = 6, column = 5)

win.mainloop()