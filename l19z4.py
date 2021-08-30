from tkinter import *

def open_file(event):
    s1 = entry1.get()
    s1 = str(s1)
    new_tuple = (s1, '.txt')
    complete_name = ''.join(new_tuple)
    hi = open(complete_name, 'r')
    contents_hi = hi.read()
    hi.close()
    text2.delete(1.0, "end")
    text2.insert(1.0, contents_hi)

def close_file(event):
    s2 = text2.get(1.0, "end")
    s1 = text1.get(1.0, "end-1c")
    s1 = str(s1)
    new_tuple = (s1, '.txt')
    complete_name = ''.join(new_tuple)
    bye = open(complete_name, 'w')
    bye.write(s2)
    bye.close()

root = Tk()

label1 = Label(width=40,text='Имя файла, который нужно открыть')
label2 = Label(width=40,text='Имя файла, в который нужно сохранить')
entry1 = Entry(width=40)
text1 = Text(height=1,width=40)
text2 = Text(height=5,width=40)
but1 = Button(width=20,text="Открыть")
but2 = Button(width=20,text="Сохранить")

but1.bind('<Button-1>', open_file)
but2.bind('<Button-1>', close_file)
label1.pack()
entry1.pack()
label2.pack()
text1.pack()
text2.pack()
but1.pack(side='left')
but2.pack(side='left')

root.mainloop()


