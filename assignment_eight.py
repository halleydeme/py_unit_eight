# Last edited: 12/14/2021
# Halley Deme
# This program runs a working calculator somplete with ten numbers, a decimal point, a percent button, and the four arithmetic buttons addition, multiplication, division, and subtraction.

import tkinter as tk
root = tk.Tk()

root.title("Working Calculator")
#Variables
entry = tk.StringVar()

add = tk.Label()

def one_function():
    e= entry.get()
    e += "1"
    entry.set(e)
def two_function():
    e = entry.get()
    e += "2"
    entry.set(e)
def three_function():
    e = entry.get()
    e += "3"
    entry.set(e)
def four_function():
    e = entry.get()
    e += "4"
    entry.set(e)
def five_function():
    e = entry.get()
    e += "5"
    entry.set(e)
def six_function():
    e = entry.get()
    e += "6"
    entry.set(e)
def seven_function():
    e = entry.get()
    e += "7"
    entry.set(e)
def eight_function():
    e = entry.get()
    e += "8"
    entry.set(e)
def nine_function():
    e = entry.get()
    e += "9"
    entry.set(e)
def zero_function():
    e = entry.get()
    e += "0"
    entry.set(e)
def eval_function():
    """

    :return: This is the evaluation function that solves the problem entered into the entry field by the user and returns the answer.
    """
    e = entry.get()
    answer = eval(e)
    entry.set(answer)
def division_function():
    e = entry.get()
    e += "/"
    entry.set(e)
def multiplication_function():
    e = entry.get()
    e += "*"
    entry.set(e)
def addition_function():
    e = entry.get()
    e += "+"
    entry.set(e)
def minus_function():
    e = entry.get()
    e += "-"
    entry.set(e)
def clear_function():
    e= entry.get()
    e = ""
    entry.set("")

def percent_function():
    e = entry.get()
    answer = eval(e)/100
    entry.set(answer)

def decimal_function():
    e = entry.get()
    e += "."
    entry.set(e)


# this is the entry field where the numbers are entered in.
entre = tk.Entry(root, textvariable = entry)
entre.grid(row=1, column = 1)

add_button = tk.Button(root, text="+", command = addition_function)
add_button.grid(row = 2, column =7)

minus_button = tk.Button(root, text="-", command= minus_function)
minus_button.grid(row = 3, column =7)

multiplication_button = tk.Button(root, text="x", command= multiplication_function)
multiplication_button.grid(row = 4, column =7)

division_button = tk.Button(root, text="÷", command= division_function)
division_button.grid(row = 5, column =7)

one_button = tk.Button(root, text="1", command = one_function)
one_button.grid(row = 2, column =1)

two_button = tk.Button(root, text="2", command = two_function)
two_button.grid(row = 2, column =2)

three_button = tk.Button(root, text="3", command= three_function)
three_button.grid(row = 2, column =3, )

four_button = tk.Button(root, text="4", command = four_function)
four_button.grid(row = 3, column =1)

five_button = tk.Button(root, text="5", command= five_function)
five_button.grid(row = 3, column =2)

six_button = tk.Button(root, text="6", command = six_function)
six_button.grid(row = 3, column =3)

seven_button = tk.Button(root, text="7", command=seven_function)
seven_button.grid(row = 4, column =1)

eight_button = tk.Button(root, text="8", command= eight_function)
eight_button.grid(row = 4, column =2)

nine_button = tk.Button(root, text="9", command= nine_function)
nine_button.grid(row = 4, column =3)

zero_button = tk.Button(root, text="0", command= zero_function)
zero_button.grid(row = 5, column =2)

clear_button = tk.Button(root, text="clear", command= clear_function)
clear_button.grid(row = 6, column =1)

equal_button = tk.Button(root, text="=", command= eval_function)
equal_button.grid(row = 5, column =3)

decimal_button = tk.Button(root, text=".", command = decimal_function)
decimal_button.grid(row = 5, column =1)

percent_button = tk.Button(root, text="%", command = percent_function)
percent_button.grid(row = 6, column =2)









root.mainloop()