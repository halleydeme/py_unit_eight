import tkinter as tk
root = tk.Tk()

root.title("Tip Calculator")
#some variales that I wlll need
cost = tk.StringVar()
cost.set(0.0)
word = tk.Label(root,text = "tip calculator")
word. grid(row=1,column=1)

meal_cost_label = tk.Label(root, text = "meal cost")
meal_cost_label. grid( row =2 , column = 1)

real_cost_entry = tk.Entry(root, textvariable = cost)
real_cost_entry.grid(row=2, column = 2)


root.mainloop()