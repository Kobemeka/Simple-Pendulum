'''
    θ(t) = θ_o * cos(ωt)
    ω = √(g/L)
'''

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from matplotlib.colors import hsv_to_rgb
import numpy as np

plt.figure(figsize=(16,9))
save = True

g = 9.81
L = 1
w = np.sqrt(g/L)
theta0 = np.pi/3

xvals = []
yvals = []

def animate(time):
    if save:
        t = time
    else:
        t = time / 100

    theta = theta0 * np.cos(w * t)

    x = L * np.sin(theta)
    y = -L * np.cos(theta)

    xmax = 2*L*np.sin(theta0)

    xvals.append(x)
    yvals.append(y)

    if len(xvals) > 30:
        xvals.pop(0)
        yvals.pop(0)

    plt.cla()

    plt.xlim(-L * np.sin(theta0) - L/10 ,L * np.sin(theta0) + L/10)
    plt.ylim(-L-L/10, 0+L/10)

    plt.scatter(0, 0, c="k",s=5)
    plt.plot([0,x], [0,y], color="k")
    
    xmap = abs(np.array(xvals)/xmax)

    color = [hsv_to_rgb((xm,0.8,0.8)) for xm in xmap]

    plt.scatter(xvals,yvals,c=color)

if save:
    plt.axis("off")
    anim = FuncAnimation(plt.gcf(),animate,interval=1,frames=np.arange(0,2*np.pi/w,0.01))
    writervideo = animation.PillowWriter(fps=60)
    anim.save('pendulum0.gif', writer=writervideo, dpi=120)
    plt.close()
else:
    anim = FuncAnimation(plt.gcf(), animate, interval=1)
    plt.show()
