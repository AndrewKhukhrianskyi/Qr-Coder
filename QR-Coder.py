import pyqrcode
from PIL import Image
import tkinter
from tkinter import messagebox as mb

"""  Ф-и(Functions) """


def qr_create_svg():
    code = qr_text.get(1.0, tkinter.END)
    coding = pyqrcode.create(code)
    coding.svg('QR-file.svg', scale = 8)
    mb.showinfo("Окошко", "Данные закодированы!")

def qr_create_eps():
    code = qr_text.get(1.0, tkinter.END)
    coding = pyqrcode.create(code)
    coding.eps('QR-file.eps', scale = 8)
    mb.showinfo("Окошко", "Данные закодированы!")

def qr_create_png():
    code = qr_text.get(1.0, tkinter.END)
    coding = pyqrcode.create(code)
    coding.eps('QR-file.eps', scale = 8)
    img = Image.open('QR-file.eps')
    img.save('QR-file.png')
    mb.showinfo("Окошко", "Данные закодированы!")
    

def func():
    if var.get() == 1:
        qr_create_svg()
    elif var.get() == 2:
        qr_create_eps()
    else:
        qr_create_png()


    

    
""" Работа с Интерфейсом (GUI Part) """

root = tkinter.Tk()
root.title('QR-Coder')
root.geometry('250x250')
root.resizable(False,False)

var = tkinter.IntVar()
rb_1 = tkinter.Radiobutton(variable = var, text = 'SVG', value = 1)
rb_2 = tkinter.Radiobutton(variable = var, text = 'EPS', value = 2)
rb_3 = tkinter.Radiobutton(variable = var, text = 'PNG', value = 3)
lab = tkinter.Label(text = 'Введите данные для кодировки ниже: ')
qr_text = tkinter.Text(width = 20, height = 5)
button = tkinter.Button(text = 'Кодим!', command = func)
lab.pack(anchor = tkinter.W)
qr_text.pack(anchor = tkinter.N)
rb_1.pack(anchor = tkinter.W)
rb_2.pack(anchor = tkinter.W)
rb_3.pack(anchor = tkinter.W)
button.pack(anchor = tkinter.S)

root.mainloop()
