from tkinter import *

okno = Tk()

okno.title("Kalkulator")
inputokno = Entry(okno, width=50, borderwidth=35, bg="white")
inputokno.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
inputokno.config(state=DISABLED)
def nacisnij(number):
    inputokno.config(state=NORMAL)
    global x
    global new_number
    global a

    x = inputokno.get() + str(number)
    new_number = inputokno.get() + str(number)
    inputokno.delete(0, END)
    inputokno.insert(0, new_number)
    if "/0" in x:
        inputokno.delete(0, END)
    inputokno.config(state=DISABLED)



def dodaj():
    inputokno.config(state=NORMAL)
    global x
    global new_number
    inputokno.delete(0, END)
    inputokno.insert(0, "+")
    inputokno.insert(0, new_number)
    x = x + str("+")
    inputokno.config(state=DISABLED)

def odejmij():
    inputokno.config(state=NORMAL)
    global new_number
    inputokno.delete(0, END)
    inputokno.insert(0, "-")
    inputokno.insert(0, new_number)
    global x
    x = x + str("-")
    inputokno.config(state=DISABLED)

def podziel():
    inputokno.config(state=NORMAL)
    global new_number
    inputokno.delete(0, END)
    inputokno.insert(0, "/")
    inputokno.insert(0, new_number)
    global x
    x = x + str("/")
    inputokno.config(state=DISABLED)

def pomnoz():
    inputokno.config(state=NORMAL)
    global new_number
    inputokno.delete(0, END)
    inputokno.insert(0, "*")
    inputokno.insert(0, new_number)
    global x
    x = x + str("*")
    inputokno.config(state=DISABLED)

def czysc():
    inputokno.config(state=NORMAL)
    inputokno.delete(0, END)
    inputokno.config(state=DISABLED)
def rownasie():
    inputokno.config(state=NORMAL)
    global x
    global new_number
    inputokno.delete(0, END)
    y=(eval(x))
    inputokno.insert(0,y)
    x=eval(x)
    x=str(x)
    new_number=eval(x)
    inputokno.config(state=DISABLED)




l1 = Button(okno, text="1", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(1))
l2 = Button(okno, text="2", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(2))
l3 = Button(okno, text="3", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(3))
l4 = Button(okno, text="4", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(4))
l5 = Button(okno, text="5", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(5))
l6 = Button(okno, text="6", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(6))
l7 = Button(okno, text="7", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(7))
l8 = Button(okno, text="8", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(8))
l9 = Button(okno, text="9", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=lambda: nacisnij(9))
l0 = Button(okno, text="0", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink",  command=lambda: nacisnij(0))
lplus = Button(okno, text="+", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=dodaj)
lminus = Button(okno, text="-", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=odejmij)
lmnoz = Button(okno, text="*", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=pomnoz)
ldziel = Button(okno, text="/", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=podziel)
lrowne = Button(okno, text="=", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=rownasie)
lczysc = Button(okno, text="C", font="-weight bold", padx=40, pady=20, borderwidth = 5, bg="pink", command=czysc)

l1.grid(row=1, column=0)
l2.grid(row=1, column=1)
l3.grid(row=1, column=2)
lplus.grid(row=1, column=3)

l4.grid(row=2, column=0)
l5.grid(row=2, column=1)
l6.grid(row=2, column=2)
lminus.grid(row=2, column=3)

l7.grid(row=3, column=0)
l8.grid(row=3, column=1)
l9.grid(row=3, column=2)
lmnoz.grid(row=3, column=3)

l0.grid(row=4, column=0)
lczysc.grid(row=4, column=1)
lrowne.grid(row=4, column=2)
ldziel.grid(row=4, column=3)

okno.mainloop()