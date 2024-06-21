from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)
root.configure(background='#282828')

numero1 = ''
divisao = False
multiplicacao = False
adicao = False
subtracao = False

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#ffffff', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(row=0, column=0, columnspan=3, pady=2)
def botao_click(num):
    e.insert(END, num)
def botao_divisao():
    global numero1, divisao
    divisao = True
    numero1 = e.get()
    e.delete(0, END)
def botao_multiplicacao():
    global numero1, multiplicacao
    multiplicacao = True
    numero1 = e.get()
    e.delete(0, END)
def botao_subtracao():
    global numero1, subtracao
    subtracao = True
    numero1 = e.get()
    e.delete(0, END)
def botao_adicao():
    global numero1, adicao
    adicao = True
    numero1 = e.get()
    e.delete(0, END)
def botao_limpa():
    e.delete(0, END)
def botao_igual():
    global subtracao, adicao, multiplicacao, divisao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == True:
        e.insert(0, int(numero1) + int(numero2))
        adicao = False
    if subtracao == True:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = False
    if multiplicacao == True:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = False
    if divisao == True:
        e.insert(0, int(numero1) / int(numero2))
        divisao = False



divide = Button(root, text='÷', padx=41, pady=20, command=botao_divisao, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
divide.grid(row=0, column=3)

um = Button(root, text='1', padx=41, pady=20, command=lambda: botao_click(1), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
um.grid(row=1, column=0)

dois = Button(root, text='2', padx=41, pady=20, command=lambda: botao_click(2), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
dois.grid(row=1, column=1)

tres = Button(root, text='3', padx=43, pady=20, command=lambda: botao_click(3), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
tres.grid(row=1, column=2)

multiplicacao = Button(root, text='x', padx=42, pady=20, command=botao_multiplicacao, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
multiplicacao.grid(row=1, column=3)

quatro = Button(root, text='4', padx=41, pady=20, command=lambda: botao_click(4), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
quatro.grid(row=2, column=0)

cinco = Button(root, text='5', padx=41, pady=20, command=lambda: botao_click(5), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
cinco.grid(row=2, column=1)

seis = Button(root, text='6', padx=43, pady=20, command=lambda: botao_click(6), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
seis.grid(row=2, column=2)

subtracao = Button(root, text='-', padx=44, pady=20, command=botao_subtracao, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
subtracao.grid(row=2, column=3)

sete = Button(root, text='7', padx=41, pady=20, command=lambda: botao_click(7), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
sete.grid(row=3, column=0)

oito = Button(root, text='8', padx=41, pady=20, command=lambda: botao_click(8), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
oito.grid(row=3, column=1)

nove = Button(root, text='9', padx=43, pady=20, command=lambda: botao_click(9), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
nove.grid(row=3, column=2)

adicao = Button(root, text='+', padx=42, pady=20, command=botao_adicao, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
adicao.grid(row=3, column=3)

zero = Button(root, text='0', padx=93, pady=20, command=lambda: botao_click(0), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
zero.grid(row=4, column=0, columnspa=2)

igual = Button(root, text='=', padx=43, pady=20, command=botao_igual, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
igual.grid(row=4, column=2)

c = Button(root, text='C', padx=41, pady=20, command=botao_limpa, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
c.grid(row=4, column=3)
root.mainloop()
