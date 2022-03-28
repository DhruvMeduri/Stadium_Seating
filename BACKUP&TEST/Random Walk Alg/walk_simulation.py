import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import random

x = 0
y = 0

x_data=[0]
y_data=[0]

fig = plt.figure()
axis = plt.axes(xlim =(-20, 20),
                ylim =(-20, 20))
line, = axis.plot([],[])

def init():
    line.set_data([],[])
    return line,

def move_random(s, t):
    direction = random.randint(1, 4)
    if direction == 1:
        s += 1
    elif direction == 2:
        t += 1
    elif direction == 3:
        s += -1
    elif direction == 4:
        t += -1
    # This line has added to this function
    return s, t


def animate_rw(i):
    # Attention to these
    #x = np.linspace(0, 2, 1000)
    #y = np.sin(2 * np.pi * (x - 0.01 * i))

    x, y = move_random(x_data[len(x_data)-1], y_data[len(y_data)-1])

    x_data.append(x)
    y_data.append(y)

    line.set_data(x_data,y_data)
    print(i)
    return line,

anim = animation.FuncAnimation(fig, animate_rw, init_func=init, frames=500, interval=50, blit = True)
anim.save('Walk.mp4', writer = 'ffmpeg', fps = 15)
