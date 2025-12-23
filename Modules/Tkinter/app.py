from tkinter import * 
def f1():
    print("You clicked the button!")
    
root = Tk()
root.geometry("300x400")


Label(root, text='Hello World!').grid(row=0, column=1)


btn = Button(root,command=f1, text="Click Now!", pady=10).grid(row=1, column=1)


Label(root, text="Enter Name: ").grid(row=3)
inp1 = Entry(root).grid(row=3, column=1)


root.mainloop()
