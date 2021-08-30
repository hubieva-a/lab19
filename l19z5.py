from tkinter import *

def lavender():
    label1['text'] = "'Lavender' - это лаванда"
    label1['bg'] = '#d4abe8'

def daisy():
    label1['text'] = "'Daisies' - ромашки"
    label1['bg'] = 'white'

def lilac():
    label1['text'] = "'Lilac' значит сирень"
    label1['bg'] = '#f7bef8'

root = Tk()
variable1 = IntVar()
variable1.set(0)
Radiobutton(text="Lavender", command=lavender,
            variable=variable1, value=0, indicatoron=0,
            width=20, bg='#d4abe8').pack()
Radiobutton(text="Daisy", command=daisy,
            variable=variable1, value=1, indicatoron=0,
            width=20, bg='white').pack()
Radiobutton(text="Lilac", command=lilac,
            variable=variable1, value=2, indicatoron=0,
            width=20, bg='#f7bef8').pack()
label1 = Label(width=20, height=10)
label1.pack(side="left")

root.mainloop()