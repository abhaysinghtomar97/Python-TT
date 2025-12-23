from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box for display
display = Entry(root, width=30, font=("Arial", 14))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions for calculator operations
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, END)

def button_add():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "add"
    f_num = int(first_number)
    display.delete(0, END)

def button_subtract():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "subtract"
    f_num = int(first_number)
    display.delete(0, END)

def button_multiply():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "multiply"
    f_num = int(first_number)
    display.delete(0, END)

def button_divide():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "divide"
    f_num = int(first_number)
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

# Create number buttons
button_1 = Button(root, text="1", width=10, height=3, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=10, height=3, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=10, height=3, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=10, height=3, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=10, height=3, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=10, height=3, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=10, height=3, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=10, height=3, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=10, height=3, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=10, height=3, command=lambda: button_click(0))

# Create operation buttons
button_add_btn = Button(root, text="+", width=10, height=3, command=button_add)
button_subtract_btn = Button(root, text="-", width=10, height=3, command=button_subtract)
button_multiply_btn = Button(root, text="*", width=10, height=3, command=button_multiply)
button_divide_btn = Button(root, text="/", width=10, height=3, command=button_divide)
button_equal_btn = Button(root, text="=", width=10, height=3, command=button_equal)
button_clear_btn = Button(root, text="C", width=10, height=3, command=button_clear)

# Place buttons on screen using grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear_btn.grid(row=4, column=1)
button_equal_btn.grid(row=4, column=2)

button_add_btn.grid(row=1, column=3)
button_subtract_btn.grid(row=2, column=3)
button_multiply_btn.grid(row=3, column=3)
button_divide_btn.grid(row=4, column=3)

root.mainloop()