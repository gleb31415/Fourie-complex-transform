import numpy as np
import tkinter as tk

width, height = 800, 800
rel_factor = 10000

val = 2 * np.pi * 1j
scale = 100
dt = 1/1000
n = 50

def update_n():
    global n
    try:
        n = int(entry_n.get())
    except ValueError:
        n = 50

def start_dr(event, points, state):
    if not state['fin']:
        points.append((event.x, event.y))
        state['dr'] = True
    else:
        reset_animation(state)

def reset_animation(state):
    state['dr'] = False
    state['fin'] = False
    canvas.delete("all")
    points.clear()

def draw(event, points, state):
    if state['dr']:
        last_x, last_y = points[-1]
        canvas.create_line(last_x, last_y, event.x, event.y, fill='blue', width=2)
        points.append((event.x, event.y))

def f(t, points):
    ind = int(t * (len(points) - 1))
    return complex((points[ind][0] - width/2)/scale, (points[ind][1] - height/2)/scale)

def count_c(points, ind):
    sum = 0
    t = 0
    length = len(points)
    dt = 1/length
    while t < 1:
        sum += f(t, points) * np.exp(-ind * val * t) * dt
        t += dt
    return sum

def start_anim(points):
    segments = []
    segments.append(Segment(count_c(points, 0), 0))
    for i in range(1, n + 1):
        segments.append(Segment(count_c(points, i), i))
        segments.append(Segment(count_c(points, -i), -i))
    animate(0, width / 2, height / 2, 0, segments)

def stop_dr(event, points, state):
    if state['dr']:
        points.append((event.x, event.y))
        state['dr'] = False
        state['fin'] = True
        start_anim(points)

root = tk.Tk()
root.geometry(f"{width}x{height}")

entry_n = tk.Entry(root, width=10)
entry_n.pack(pady=10)
entry_n.insert(0, str(n))

button_apply = tk.Button(root, text="subm", command=update_n)
button_apply.pack(pady=5)

canvas = tk.Canvas(root, width=width, height=height, background='black')
canvas.pack()

points = []
state = {'dr': False, 'fin': False}

canvas.bind("<Button-1>", lambda event: start_dr(event, points, state))
canvas.bind("<B1-Motion>", lambda event: draw(event, points, state))
canvas.bind("<ButtonRelease-1>", lambda event: stop_dr(event, points, state))

zx = width / 2
zy = height / 2

class Segment:
    def __init__(self, c, n):
        self.c = c
        self.n = n

    def get_end(self, t, x0, y0):
        new = self.c * np.exp(val * self.n * t) * scale
        return (new.real + x0), (new.imag + y0)

def animate(t, lx, ly, cnt, segments):
    if not state['fin']:
        return
    x0, y0 = zx, zy
    canvas.delete("dynamic")
    for segment in segments:
        x1, y1 = segment.get_end(t, x0, y0)
        canvas.create_line(x0, y0, x1, y1, width=1, fill='yellow', tags="dynamic")
        r = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
        canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, width=1, outline='green', tags="dynamic")
        x0, y0 = x1, y1
    if cnt != 0:
        canvas.create_line(x0, y0, lx, ly, width=1, fill='white', tags='static')
    lx, ly = x0, y0
    canvas.create_oval(x0 - 5, y0 - 5, lx + 5, ly + 5, fill='red', tags='dynamic')

    if t < 1: t += dt
    else: t = 0
    cnt = 1

    root.after(int(dt*rel_factor), animate, t, lx, ly, cnt, segments)

root.mainloop()
