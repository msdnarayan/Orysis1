import tkinter
window=tkinter.Tk()
def print_hello():
    print("Hey there")
    
window.title("GUI Application")

window.minsize(600,450)
#window.geometry("600x450")

label1=tkinter.Label(text="Hello World",font=('Helvetica 15 bold'))
#label1["text"]="HeY"
label1.pack()
def conf():
    
      label1.config(text="HeLLo")
      label1.pack()


button=tkinter.Button(text='click me',command=conf,bg='#121047',foreground='#f2f2f2')
button.place(x=56,y=67)


window.mainloop()