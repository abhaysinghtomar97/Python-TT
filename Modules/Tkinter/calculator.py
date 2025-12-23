from tkinter import * 
root = Tk()
root.geometry("400x500")
root.title("My Calculator")

# display 
display = Entry(root, width=30, font=("Arial", 14))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# operations
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))


def button_clear():
    display.delete(0, END)

def add():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "add"
    f_num = first_number
    display.delete(0, END)

def sub():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "subtract"
    f_num = first_number
    display.delete(0, END)

def multi():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "multiply"
    f_num = first_number
    display.delete(0, END)

def div():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "divide"
    f_num = first_number
    display.delete(0, END)

def button_equal():
    second_number = display.get()
    display.delete(0, END)
    
    if math_operation == "add":
        display.insert(0, f_num + int(second_number))
    
    if math_operation == "subtract":
        display.insert(0, f_num - int(second_number))
    
    if math_operation == "multiply":
        display.insert(0, f_num * int(second_number))
    
    if math_operation == "divide":
        display.insert(0, f_num / int(second_number))


# buttons 
btn_1 = Button(root, text="1", width=10, height=3, command= lambda: button_click(1))
btn_2 = Button(root, text="2", width=10, height=3, command= lambda: button_click(2))
btn_3 = Button(root, text="3", width=10, height=3, command= lambda: button_click(3))
btn_4 = Button(root, text="4", width=10, height=3, command= lambda: button_click(4))
btn_5 = Button(root, text="5", width=10, height=3, command= lambda: button_click(5))
btn_6 = Button(root, text="6", width=10, height=3, command= lambda: button_click(6))
btn_7 = Button(root, text="7", width=10, height=3, command= lambda: button_click(7))
btn_8 = Button(root, text="8", width=10, height=3, command= lambda: button_click(8))
btn_9 = Button(root, text="9", width=10, height=3, command= lambda: button_click(9))
btn_0 = Button(root, text="0", width=10, height=3, command= lambda: button_click(0))

btn_clr = Button(root, text="Clear", width=10, height=3, command=  button_clear)
btn_equal = Button(root, text="=", width=10, height=3, command=  button_equal)

btn_add = Button(root, text="+", height=3, width=10, command= add )
btn_sub = Button(root, text="-", height=3, width=10, command= sub)
btn_div = Button(root, text="/", height=3, width=10, command= div)
btn_multi = Button(root, text="x", height=3, width=10, command= multi)


# buttons positions 
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)

btn_0.grid(row=4, column=0)
btn_clr.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)

btn_sub.grid(row=1, column=3)
btn_div.grid(row=2, column=3)
btn_multi.grid(row=3, column=3)
btn_add.grid(row=4, column=3)



root.mainloop()