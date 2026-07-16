from tkinter import *
from random import randint
root = Tk()
root.geometry("800x300")
root.title("Number Guessing Game")
a = None
r = None
def start():
    global r
    r = randint(1, 10)
    print("Game started! Random number generated (hidden).")
def check():
    global a, r
    try:
        a = int(entry.get())
        if a == r:
            result_label.config(text="Match number successfully!", fg="green")
        elif a > r:
            result_label.config(text=" Random number is smaller!", fg="orange")
        else:
            result_label.config(text=" Random number is greater!", fg="red")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")
def stop():
    root.destroy()
l1 = Label(text="Number Guessing Game", font="arial 25 bold", fg="blue", bg="lightgreen")
l1.pack(fill=X)
entry = Entry(root, font="arial 15 bold", width=10, justify='center')
entry.pack(pady=20)
f1 = Frame(root, borderwidth=10, relief=RIDGE, bg="red")
f1.pack()
b1 = Button(f1, text="Start", bg="green", fg="white", width=10, command=start, font="arial 15 bold")
b1.pack(side=LEFT, padx=5)
b2 = Button(f1, text="Check", bg="green", fg="white", width=10, command=check, font="arial 15 bold")
b2.pack(side=LEFT, padx=5)
b3 = Button(f1, text="Stop", bg="green", fg="white", width=10, command=stop, font="arial 15 bold")
b3.pack(side=LEFT, padx=5)
result_label = Label(root, text="", font="arial 15 bold", fg="black")
result_label.pack(pady=15)
root.mainloop()
