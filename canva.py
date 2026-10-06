'''import tkinter as tk
root = tk.Tk()
root.title("My First Canvas")
canvas = tk.Canvas(root, width=500,
                   height=350, bg="white")
canvas.pack()
root.mainloop()'''

import tkinter as tk
root = tk.Tk()
root.geometry("600x450")
canvas = tk.Canvas(root, width=550, height=360, bg="white")
canvas.pack()
canvas.create_rectangle(40, 40, 220, 150, fill="coral")
canvas.create_oval(280, 50, 440, 190, fill="lightblue")
canvas.create_line(50, 250, 500, 250, width=4)
canvas.create_text(275, 310, text="Hello Canvas", font=
("Arial", 20))
root.mainloop()