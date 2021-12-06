import tkinter as tk
root = tk.Tk()

root.title("Working Calculator")
#Variables
entry = tk.StringVar()
entry.set(0.0)
add = tk.Label()



entry = tk.Entry(root, textvariable = entry)
entry.grid(row=1, column = 1)

add_button = tk.Button(root, text="+")
add_button.grid(row = 2, column =7)

minus_button = tk.Button(root, text="-")
minus_button.grid(row = 3, column =7)

multiplication_button = tk.Button(root, text="÷")
multiplication_button.grid(row = 4, column =7)

division_button = tk.Button(root, text="x")
division_button.grid(row = 5, column =7)

one_button = tk.Button(root, text="1")
one_button.grid(row = 2, column =1)

two_button = tk.Button(root, text="2")
two_button.grid(row = 2, column =2)

three_button = tk.Button(root, text="3")
three_button.grid(row = 2, column =3)

four_button = tk.Button(root, text="4")
four_button.grid(row = 3, column =1)

five_button = tk.Button(root, text="5")
five_button.grid(row = 3, column =2)

six_button = tk.Button(root, text="6")
six_button.grid(row = 3, column =3)

seven_button = tk.Button(root, text="7")
seven_button.grid(row = 4, column =1)

eight_button = tk.Button(root, text="8")
eight_button.grid(row = 4, column =2)

nine_button = tk.Button(root, text="9")
nine_button.grid(row = 4, column =3)

zero_button = tk.Button(root, text="0")
zero_button.grid(row = 5, column =2)

clear_button = tk.Button(root, text="clear")
clear_button.grid(row = 6, column =1)

equal_button = tk.Button(root, text="=")
equal_button.grid(row = 5, column =3)

decimal_button = tk.Button(root, text=".")
decimal_button.grid(row = 5, column =1)

percent_button = tk.Button(root, text="%")
percent_button.grid(row = 6, column =2)









root.mainloop()