from tkinter import*
import tkinter
from random import*
#---------------------------------root-------------------------------
root = Tk()
root.title("Тараканы")
root.geometry("1600x700")
root["bg"] = "darkred"

def go():
    global x1, x2, x3, x4
    canvas.coords(pic11, x1, 60)
    x1 += randint(1,10)
    canvas.coords(pic22, x2, 190)
    x2 += randint(1,10)
    canvas.coords(pic33, x3, 320)
    x3 += randint(1,10)
    canvas.coords(pic44, x4, 445)
    x4 +=randint(1,10)
    if x1<1500 and x2<1500 and x3<1500 and x4<1500:
        canvas.after(5, go)
    else:
        if x1>x2 and x1>x3 and x1>x4:
            win='первый победил'
        elif x2>x3 and x2>x4:
            win='второй победил'
        elif x3>x4:
            win='третий победил'
        else:
            win='четвертый победил'
        winner = Toplevel()
        winner.geometry("400x400")
        label1=Label(winner, text='Результат: ' + str(win))
        label1.place(x=150,y=100)
        winner.mainloop()

def rest():
    pass

#---------------------------------Canva------------------------------
canvas = Canvas(root, width=1600, height=510, bg='white')
canvas.place(x=0, y=190)
canvas.create_line(0, 128, 1600, 128, width=2)
canvas.create_line(0, 256, 1600, 256, width=2)
canvas.create_line(0, 384, 1600, 384, width=2)
canvas.create_line(1500, 0, 1500, 600, width=10)

#---------------------------------tarakani---------------------------
pic1 = PhotoImage(file='tar1.png')
pic11 = canvas.create_image(70, 60, image=pic1)
pic2 = PhotoImage(file='tar2.png')
pic22 = canvas.create_image(70, 190, image=pic2)
pic3 = PhotoImage(file='tar3.png')
pic33 = canvas.create_image(70, 320, image=pic3)
pic4 = PhotoImage(file='tar4.png')
pic44 = canvas.create_image(70, 445, image=pic4)

#======================functions=====================
x1 = 70
x2 = 70
x3 = 70
x4 = 70

#--------------------------------Button------------------------------
bt1 = Button(root, text='Старт', bg='white', fg='black', width=30, height=5, command=go)
bt1.place(x=1100, y=20)
bt2 = Button(root, text='Рестарт', bg='white', fg='black', width=30, height=5, command= rest)
bt2.place(x=1350, y=20)

#------------------------------Radiobutton---------------------------
selpo = tkinter.StringVar(value = 1)
bt3 = Radiobutton(bg='darkred', text='1', width=10, height=5, variable=selpo, value=1)
bt3.place(x=10, y=10)
bt4 = Radiobutton(bg='darkred', text='2', width=10, height=5, variable=selpo, value=2)
bt4.place(x=110, y=10)
bt5 = Radiobutton(bg='darkred', text='3', width=10, height=5, variable=selpo, value=3)
bt5.place(x=10, y=110)
bt6 = Radiobutton(bg='darkred', text='4', width=10, height=5, variable=selpo, value=4)
bt6.place(x=110, y=110)

#---------------------------------Lable------------------------------
many = 1000
label = tkinter.Label(root ,text='Деньга: '+str(many), bg='darkred', fg='black', font=('Arial', 20))
label.place(x=250, y=50)

#---------------------------------Scale------------------------------
slider = Scale(root, from_=0, to=1000, orient="horizontal", width=50, resolution=100, label='Выберите ставку:', bg = 'magenta', length=350)
slider.place(x=700,y=20)

root.mainloop()