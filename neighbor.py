import tkinter as tk

root = tk.Tk()
root.title("Dream House")

canvas = tk.Canvas(root, width=500, height=350, bg="white")
canvas.pack()

# House body
canvas.create_rectangle(120, 140, 380, 300, fill="lightyellow")

# Roof
canvas.create_polygon(
    90, 140,
    250, 50,
    410, 140,
    fill="brown"
)

# Door
canvas.create_rectangle(220, 220, 280, 300, fill="brown")

# Door knob
canvas.create_oval(265, 255, 272, 262, fill="black")

# Left window
canvas.create_rectangle(145, 170, 195, 220, fill="lightblue")
canvas.create_line(170, 170, 170, 220, fill="black")
canvas.create_line(145, 195, 195, 195, fill="black")

# Right window
canvas.create_rectangle(305, 170, 355, 220, fill="lightblue")
canvas.create_line(330, 170, 330, 220, fill="black")
canvas.create_line(305, 195, 355, 195, fill="black")

root.mainloop()