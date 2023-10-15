import tkinter
win=tkinter.Tk()

def text():
    txt=float(name.get())
    km=1.60934*txt
    label1.config(text=f"{km} Km")
win.title="Miles to Kilometers"
win.minsize(600,400)

label2=tkinter.Label(text="Miles:")
label2.grid(row = 4, column = 1,padx=30,pady=40)
win.config(bg="#41434f")
label1=tkinter.Label(text="")
label1.grid(row = 10, column = 5)
name=tkinter.Entry()
name.grid(row = 4, column = 5)

btn=tkinter.Button(text="Submit",command=text,bg='#121047',foreground='#f2f2f2')
btn.grid(row = 6, column = 5)

win.mainloop()