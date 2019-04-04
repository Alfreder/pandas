def printentry():
    s = v1.get()
    s1 = v2.get()
    print( type(s1))
from tkinter import *
root=Tk()
v1=StringVar()
v2=StringVar()
e = Entry(root,textvariable=v1).pack() #设置输入框对应的文本变量为var
f = Entry(root,textvariable=v2).pack() #设置输入框对应的文本变量为var
Button(root,text="print entry",command=printentry).pack()
root.mainloop()