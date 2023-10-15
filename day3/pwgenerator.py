import random
import tkinter

def passw():
    
    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num=['1', '2', '3', '4', '5', '6', '7', '8', '9']
    spl=['!','@','#','$','%','^','&','*','_']

    acount=random.randint(3,6)
    ncount=random.randint(3,6)
    scount=random.randint(2,4)

    pw_gen=[]

    for i in range(acount):
        pw_gen+=random.choice(alph)
    for i in range(ncount):
        pw_gen+=random.choice(num)
    for i in range(scount):
        pw_gen+=random.choice(spl)
    random.shuffle(pw_gen)
    joined=''.join(pw_gen)
   # print("Password: "+joined)
    entry1.delete(0,tkinter.END)
    entry1.insert(0,f"{joined}")

win=tkinter.Tk()
win.title="Password Generator"
win.minsize(500,400)
win.config(bg="#29453f")

l1=tkinter.Label(text="Password Generator ",bg="#29453f",font="Verdana 20",foreground="#edf2f1")
l1.grid(pady=20,padx=25,row=3,column=5)

entry1=tkinter.Entry()
entry1.grid(pady=15,padx=20,row=5,column=5)

btn=tkinter.Button(text="Generate" ,height=1,width=16,command=passw)
btn.grid(pady=15,padx=20,row=4,column=5)


win.mainloop()