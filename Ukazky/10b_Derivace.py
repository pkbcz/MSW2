import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f(x):                                       # definice funkce f(x) = x^2 - 3
    return x ** 3 + 1

x0 = 1                                          # bod x0
x1 = 3                                          # koncové x

x = np.linspace(x0, x1, 100)                    # generování hodnot x pro vykreslení grafu
y_f = f(x)                                      # hodnoty funkce f(x) pro dané x

y0 = np.min(y_f)                                # krajní body grafu
if y0 > 0:
    y0 = 0
y1 = np.max(y_f)
h = 1                                           # krok h

def update(val):
    h = slider.val
    k = (f(x0+h) - f(x0)) / h                   # výpočet směrnice sečny
    q = f(x0) - k*x0                            # výpočet konstanty

    ax.cla()                                    # clear
    ax.plot(x, y_f, label='f(x) = x^2 - 3')     # vykreslení grafu funkce f(x) 
    ax.plot([x0, x1], [f(x0), k*x1+q], 'r--')   # sečna
    ax.plot(x0, f(x0), 'ro')                    # červený bod v bodě x0
    ax.plot(x0 + h, f(x0 + h), 'ro')            # červený bod v bodě x0 + h
    ax.plot([x0, x0+h], [f(x0), f(x0)], "m:")   # delta x a delta y
    ax.plot([x0+h, x0+h], [f(x0), f(x0+h)], "m:")

    ax.text(x0, f(x0), r'$x_0$', fontsize=12, verticalalignment='bottom')              # popiska x0
    ax.text(x0 + h, f(x0+h), r'$x_0 + h$', fontsize=12, verticalalignment='bottom')    # popiska x0 + h

    #ax.axis([x0, x1, y0, y1])                   # nastavení rozsahů (xmin, xmax, ymin, ymax)
    ax.axhline(y = 0, color='k')                # vykreslení osy x
    ax.set_xlabel('x')                          # popisky os
    ax.set_ylabel('y')

    ax.grid(True)
    plt.draw()

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.25)
slider = Slider(plt.axes([0.2, 0.1, 0.65, 0.03]), 'h', 0.001, 1.9, valinit=h)
slider.on_changed(update)
update(h)
plt.show()
