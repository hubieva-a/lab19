from tkinter import *

def func_sum(event):
    s1 = entry1.get()
    s1 = float(s1)
    s2 = entry2.get()
    s2 = float(s2)
    result1 = s1 + s2
    result1 = str(result1)
    label1['text'] = ' '.join(result1)

def func_difference(event):
    s1 = entry1.get()
    s1 = float(s1)
    s2 = entry2.get()
    s2 = float(s2)
    result2 = s1 - s2
    result2 = str(result2)
    label1['text'] = ' '.join(result2)

def func_multiplication(event):
    s1 = entry1.get()
    s1 = float(s1)
    s2 = entry2.get()
    s2 = float(s2)
    result3 = s1 * s2
    result3 = str(result3)
    label1['text'] = ' '.join(result3)

def func_splitting(event):
    s1 = entry1.get()
    s1 = float(s1)
    s2 = entry2.get()
    s2 = float(s2)
    result4 = s1 / s2
    result4 = str(result4)
    label1['text'] = ' '.join(result4)

root = Tk()

entry1 = Entry(width=20)
entry2 = Entry(width=20)
but1 = Button(width=20,text=" + ")
but2 = Button(width=20,text=" - ")
but3 = Button(width=20,text=" * ")
but4 = Button(width=20,text=" / ")
label1 = Label(width=20)
but1.bind('<Button-1>', func_sum)
but2.bind('<Button-1>', func_difference)
but3.bind('<Button-1>', func_multiplication)
but4.bind('<Button-1>', func_splitting)

entry1.pack()
entry2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
label1.pack()

root.mainloop()