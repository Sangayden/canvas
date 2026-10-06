
import tkinter as tk

# Create window
root = tk.Tk()
root.title("My House")
root.geometry("600x500")

# Create Canvas
canvas = tk.Canvas(root, width=600, height=500, bg="skyblue")
canvas.pack()

# Ground
canvas.create_rectangle(
    0, 400, 600, 500,
    fill="green"
)

# House body
canvas.create_rectangle(
    180, 230, 420, 400,
    fill="lightyellow"
)

# Roof
canvas.create_polygon(
    150, 230,
    300, 100,
    450, 230,
    fill="red"
)

# Door
canvas.create_rectangle(
    270, 310, 330, 400,
    fill="brown"
)

# Door handle
canvas.create_oval(
    315, 350, 322, 357,
    fill="yellow"
)

# Left window
canvas.create_rectangle(
    205, 270, 255, 320,
    fill="lightblue"
)

# Right window
canvas.create_rectangle(
    345, 270, 395, 320,
    fill="lightblue"
)

# Window crosses
canvas.create_line(230, 270, 230, 320, width=2)
canvas.create_line(205, 295, 255, 295, width=2)

canvas.create_line(370, 270, 370, 320, width=2)
canvas.create_line(345, 295, 395, 295, width=2)

# Sun
canvas.create_oval(
    40, 40, 110, 110,
    fill="yellow"
)

# Title
canvas.create_text(
    300, 40,
    text="MY BEAUTIFUL HOUSE",
    font=("Arial", 22, "bold"),
    fill="darkblue"
)

# Click challenge
def add_flower(event):
    canvas.create_oval(
        event.x - 5, event.y - 5,
        event.x + 5, event.y + 5,
        fill="pink"
    )

canvas.bind("<Button-1>", add_flower)

root.mainloop()