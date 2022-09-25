import random
import queue
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as anim
from matplotlib import style

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)

#x and y axes
xs = [0,1,2,3,4,5,6,7,8,9,10]
xst = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
ys = queue.Queue(maxsize = 12)


#x and y axes for plotting
#for 10 secs at a time
ry = []
rx = xs
# the entire thing
rxt = xst
ryt = []

style.use("seaborn-whitegrid")

#to fill the y-axis
def filly():
    for i in range(11):
       randy = random.randint(0,20)
       ys.put(randy)

#add one y-value
def oney():
    randy = random.randint(0,20)
    ys.put(randy)

# make first 11 y-values
def strt():
    filly()
    for i in range(11):
        t = ys.get()
    
        #plot stuff
        ryt.append(t)
        ry.append(t)

strt()

def temp_animate(i):
    oney()
    
    t = ys.get()
    
    #plot stuff
    ry.append(t)
    
    ax2.figure.canvas.draw_idle()
    
    ax1.clear()
    ax1.plot(rx, ry[0:11])
    ax1.set_title("Random Integer Plot over 10 Seconds")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Temperature (deg Celsius)")
    
    rx.pop(0)
    ry.pop(0)
    rx.append(xs[-1] + 1)
    
    ax2.clear()
    ax2.plot(rxt, ryt)
    ax2.set_title("All Random Integer Plot Over Time")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Temperature (deg Celsius)")
    
    ryt.append(t)
    rxt.append(rxt[-1] + 1)
    

ani = anim.FuncAnimation(fig, temp_animate, interval=500)
plt.show()

    
