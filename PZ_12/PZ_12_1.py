# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу
# https://www.devlounge.net/wp-content/uploads/2011/02/24ways.jpg

from tkinter import *

window = Tk()
window.title('Практическая работа')
width = 500
height = 1000
window.geometry(f'{width}x{height}+500+500')
window.resizable(False, False)

var = IntVar()

def makealbewithtext(panel, name, desc, posY1, posY2, customHeight):
    label = Label(panel, text=name, font=('Arial', 12), bg='#afc447')
    label.place(x=24, y=posY2 - 36)
    entry = Entry(width=18, font='arial 15')
    buff = 0
    if customHeight == TRUE:
        entry.place(x=width * 0.5, y=posY2 - 36, height=96)

        buff = 72
    else:
        entry.place(x=width * 0.5, y=posY2 - 36)

    entry.insert(0, desc)
    canvas.create_rectangle(20, posY1, width * 0.9, posY2 + buff, outline='white', width=1)

Canvas(window, bg='#afc447', width=width, height=height, highlightbackground='#afc447').place(x=0, y=0)
canvas = Canvas(window, height=height, width=470, bg='#afc447', highlightbackground='#afc447')
canvas.pack()

label1 = Label(canvas, text="Step 1: Your details", font=('Arial', 18), bg='#afc447')
label1.place(x=24, y=24)

makealbewithtext(canvas, "Name", "First and last name", 64, 108, FALSE)
makealbewithtext(canvas, "Email", "example@domain.com", 121, 165, FALSE)
makealbewithtext(canvas, "Phone", "Eg. +4475000000000", 178, 222, FALSE)

label2 = Label(canvas, text="Step 2: Delivery address", font=('Arial', 18), bg='#afc447')
label2.place(x=24, y=234)

makealbewithtext(canvas, "Address", "", 270, 314, TRUE)
makealbewithtext(canvas, "Post Code", "", 399, 443, FALSE)
makealbewithtext(canvas, "Country", "", 455, 499, FALSE)

label2 = Label(canvas, text="Step 3: Card Type", font=('Arial', 18), bg='#afc447')
label2.place(x=24, y=511)

label = Label(canvas, text='Card type', font=('Arial', 12), bg='#afc447')
label.place(x=24, y=547)

Radiobutton(canvas, text="VISA", variable=var, value=1, bg='#afc447').place(x=24, y=571)
Radiobutton(canvas, text="AmEx", variable=var, value=2, bg='#afc447').place(x=96, y=571)
Radiobutton(canvas, text="Mastercard", variable=var, value=3, bg='#afc447').place(x=168, y=571)
canvas.create_rectangle(20, 545, width * 0.9, 607, outline='white', width=1)

makealbewithtext(canvas, "Card number", "", 619, 663, FALSE)
makealbewithtext(canvas, "Post Code", "", 675, 719, FALSE)
makealbewithtext(canvas, "Name on card", "Exact name as on the card", 731, 775, FALSE)


Button(canvas, text='BUY IT!', width=24, height = 4, fg='black', bd=0, bg='#C0C0C0', font='arial 11').place(x=width * 0.25, y=height * 0.9)

window.mainloop()
