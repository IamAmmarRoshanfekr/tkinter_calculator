from tkinter import *
from tkinter import ttk

root = Tk()
root.resizable(0,0)
root.title("Calculator with Tkinter")
frm = ttk.Frame(root,padding=10)
frm.grid()

# buttons func
def btn_insert(text):
    global expression
    expression += str(text)
    txtvar.set(expression)

def btn_clear():
    global expression
    expression = ""
    txtvar.set(expression)

def btn_sum():
    global expression
    try:
        sum = str(eval(expression))
        txtvar.set(sum)
        expression = ""
    except:
        # if equation has an Error
        txtvar.set("ERROR")
        expression = ""


# this is expression
expression = ""

# textvar - input
txtvar = StringVar()

# first row
input = ttk.Entry(frm,textvariable=txtvar,width=61).grid(row=0,column=0, columnspan=4)

# second row
btn1 = ttk.Button(frm, text=1,padding=10,command= lambda: btn_insert(1)).grid(row=1,column=0)
btn2 = ttk.Button(frm, text=2,padding=10,command= lambda: btn_insert(2)).grid(row=1,column=1)
btn3 = ttk.Button(frm, text=3,padding=10,command= lambda: btn_insert(3)).grid(row=1,column=2)
btnsum = ttk.Button(frm, text="=",padding=10,command= lambda: btn_sum()).grid(row=1,column=3)
# third row
btn4 = ttk.Button(frm, text=4,padding=10,command= lambda: btn_insert(4)).grid(row=2,column=0)
btn5 = ttk.Button(frm, text=5,padding=10,command= lambda: btn_insert(5)).grid(row=2,column=1)
btn6 = ttk.Button(frm, text=6,padding=10,command= lambda: btn_insert(6)).grid(row=2,column=2)
btnplus = ttk.Button(frm, text="+",padding=10,command= lambda: btn_insert("+")).grid(row=2,column=3)

# fourth row
btn7 = ttk.Button(frm, text=7,padding=10,command= lambda: btn_insert(7)).grid(row=3,column=0)
btn8 = ttk.Button(frm, text=8,padding=10,command= lambda: btn_insert(8)).grid(row=3,column=1)
btn9 = ttk.Button(frm, text=9,padding=10,command= lambda: btn_insert(9)).grid(row=3,column=2)
btnminus = ttk.Button(frm, text="-",padding=10,command= lambda: btn_insert("-")).grid(row=3,column=3)

# fifth row
btnclear = ttk.Button(frm, text="clear",padding=10,command=lambda: btn_clear()).grid(row=4,column=0)
btn0 = ttk.Button(frm, text=0,padding=10,command= lambda: btn_insert(0)).grid(row=4,column=1)
btnmulti =  ttk.Button(frm, text="*",padding=10,command= lambda: btn_insert("*")).grid(row=4,column=2)
btndivide = ttk.Button(frm, text="/", padding=10,command=lambda: btn_insert("/")).grid(row=4, column=3)


# the loop
root.mainloop()
