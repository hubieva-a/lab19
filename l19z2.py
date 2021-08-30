from tkinter import *

def color_red(event):
    text1.delete(1.0, "end")
    text1.insert(1.0,'Красный')
    label1['text'] = '#ff0000'

def color_orange(event):
    text1.delete(1.0, "end")
    text1.insert(1.0,'Оранжевый')
    label1['text'] = '#ff7d00'

def color_yellow(event):
    text1.delete(1.0, "end")
    text1.insert(1.0,'Жёлтый')
    label1['text'] = '#ffff00'

def color_green(event):
    text1.delete(1.0, "end")
    text1.insert(1.0,'Зеленый')
    label1['text'] = '#00ff00'

def color_blue(event):
    text1.delete(1.0, "end")
    text1.insert(1.0,'Голубой')
    label1['text'] = '#007dff'

def color_indigo(event):
    text1.delete(1.0, "end")
    text1.insert(1.0,'Синий')
    label1['text'] = '#0000ff'

def color_purple(event):
    text1.delete(1.0, "end")
    text1.insert(1.0,'Фиолетовый')
    label1['text'] = '#7d00ff'

root = Tk()

text1 = Text(width=20,height=1)
label1 = Label(width=20)
but1 = Button(width=20, bg='#ff0000')
but2 = Button(width=20, bg='#ff7d00')
but3 = Button(width=20, bg='#ffff00')
but4 = Button(width=20, bg='#00ff00')
but5 = Button(width=20, bg='#007dff')
but6 = Button(width=20, bg='#0000ff')
but7 = Button(width=20, bg='#7d00ff')

but1.bind('<Button-1>', color_red)
but2.bind('<Button-1>', color_orange)
but3.bind('<Button-1>', color_yellow)
but4.bind('<Button-1>', color_green)
but5.bind('<Button-1>', color_blue)
but6.bind('<Button-1>', color_indigo)
but7.bind('<Button-1>', color_purple)
text1.pack()
label1.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()

root.mainloop()
