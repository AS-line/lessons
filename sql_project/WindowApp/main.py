import tkinter as tk

root = tk.Tk()
root.title('Построение отрезков')
root.geometry('1220x640')

canvas = tk.Canvas(root, width=1020, height=640, bg='#002')
canvas.pack(side='right')

# линии сетки по вертикали
for y in range(21):
    k = 50 * y
    canvas.create_line(20 + k, 620, 20 + k, 20, width=1, fill='#191936')

# линии сетки по горизонтали
for x in range(13):
    k = 50 * x
    canvas.create_line(20, 20 + k, 1020, 20 + k, width=1, fill='#191936')

# линии координат X и Y
canvas.create_line(5, 320, 1010, 320, width=2, arrow='last', fill='white')  # X
canvas.create_line(20, 620, 20, 20, width=2, arrow='last', fill='white')  # Y

# текст на линиях(x, y)
canvas.create_text(35, 35, text='Y', fill='white')
canvas.create_text(1000, 305, text='X', fill='white')

# поля ввода
dot_x1 = 'Точка X1:'

label_x1 = tk.Label(root, text=dot_x1)
label_x1.place(x=0, y=10)
label_y1 = tk.Label(root, text='Точка Y1:')
label_y1.place(x=0, y=30)
label_x2 = tk.Label(root, text='Точка X2:')
label_x2.place(x=0, y=50)
label_y2 = tk.Label(root, text='Точка Y2:')
label_y2.place(x=0, y=70)

def calc(x1, y1, x2, y2):
    global line
    line = canvas.create_line((x1*50)+20, (y1*250)+20, (x2*50)+20, (y2*250)+20, width=2, fill='green')

def clean():
    canvas.delete(line)

entry_x1 = tk.Entry(root)
entry_x1.place(x=70, y=10)
entry_y1 = tk.Entry(root)
entry_y1.place(x=70, y=30)
entry_x2 = tk.Entry(root)
entry_x2.place(x=70, y=50)
entry_y2 = tk.Entry(root)
entry_y2.place(x=70, y=70)

btn_calc = tk.Button(root, text='Построить')
btn_calc.bind('<Button-1>', lambda event: calc(float(entry_x1.get()), float(entry_y1.get()), float(entry_x2.get()), float(entry_y2.get())))
btn_calc.place(x=0, y=100)

btn_cls = tk.Button(root, text='Очистить')
btn_cls.bind('<Button-1>', lambda event: clean())
btn_cls.place(x=0, y=130)


root.mainloop()