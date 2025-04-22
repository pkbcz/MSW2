import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
import matplotlib as mpl

def f1(x):                                              # definice funkce např. f(x) = x^2 - 3
    return x ** 3 + 1
def f2(x): 
    return np.where(x > 0, x**2 + 2, x)
def f3(x):
    x = np.array(x, dtype=float)                        # ujistíme se, že x je numpy.ndarray typu float
    return np.divide(1, x, out=np.zeros_like(x, dtype=float), where=x != 0)
x0 = 0                                                  # bod x0
hmax = 2

#x = np.linspace(x0-hmax, x0 + hmax, 1000)               # generování hodnot x pro vykreslení grafu


delta = 1                                               # krok delta
epsilon = 1

default_line_color = mpl.rcParams['lines.color']        # výchozí barva pro křivky
def setup(val):
    sliderD.valmin = 0.00001                            # slider od nuly

    sliderD.ax.set_xlim(sliderD.valmin,sliderD.valmax)  # překreslení slideru
    update(delta)                                       # překreslení grafu

def line_eq(x, x1, y1, x2, y2, color):
    return
    if x1 == x2:
        return
    k = (y2 - y1) / (x2 - x1)                           # směrnice
    q = y1 - k * x1                                     # úsek na ose y
    ax.plot(x, k*x + q, color + '--')                   # sečna
    ax.plot(x0, f(x0), 'ro')                            # červený bod v bodě x0

def update2(val):                                       # změna křivky
    global f, y, ymin, ymax, x, x0
    x = np.linspace(x0-hmax, x0 + hmax, 1000)               # generování hodnot x pro vykreslení grafu

    x0 = slider0.val

    if val == "spoj":
        f = f1
    elif val == "nesp1":
        f = f2
    elif val == "nesp2":
        f = f3

#    x = np.linspace(x0-hmax, x0 + hmax, 1000)          # generování hodnot x > x0 pro vykreslení grafu
    y = f(x)
    ymin = np.min(y) - 1
    ymax = np.max(y) + 1
    ymin = max(ymin, -10)
    ymax = min(ymax, 10)
    update(1)

def vykresli_eps(ax, epsilon):
    col = "red"
    ax.axhline(f(x0)-epsilon, color=col, linestyle="--", alpha=0.4)                    # vykreslení osy y
    ax.axhline(f(x0)+epsilon, color=col, linestyle="--", alpha=0.4)                    # vykreslení osy y
    ax.axhspan(f(x0)-epsilon, f(x0)+epsilon, color=col, alpha=0.1, label="Vybarvená oblast")
    xpos = ax.get_xlim()[0] + 0.15 #*(hmax)

    ax.annotate("$\epsilon$-okolí",
            xy=(xpos, f(x0)-epsilon), xytext=(xpos, f(x0)+epsilon),  # Začátek a konec šipky
            color=col, 
            #xycoords=fig.transFigure,
            arrowprops=dict(arrowstyle="<->", color=col, lw=2),
            ha='center', va='bottom')



def vykresli_delta(ax, delta):
    col = "green"
    #return
    ax.plot(x0 - delta, f(x0 - delta), 'mo')                                            # bod v bodě x0
    ax.plot(x0 + delta, f(x0 + delta), 'mo')                                            # bod v bodě x0 + delta
    ax.text(x0 - delta, f(x0 - delta), r'$x_0 - \delta$', fontsize=12, verticalalignment='bottom')      # popiska x0 - delta
    ax.text(x0, f(x0), r'$x_0$', fontsize=12, verticalalignment='bottom')                               # popiska x0
    ax.text(x0 + delta, f(x0+delta), r'$x_0 + \delta$', fontsize=12, verticalalignment='bottom')        # popiska x0 + delta

    ax.axvline(x = x0, color=col)                                                       # vykreslení osy y
    ax.axvline(x = x0-delta, color=col, linestyle="--", alpha=0.2)                      # vykreslení osy y
    ax.axvline(x = x0+delta, color=col, linestyle="--", alpha=0.2)                      # vykreslení osy y
    ax.axvspan(x0-delta, x0+delta, color=col, alpha=0.05, label="Vybarvená oblast")
    # Přidání šipky k označení oblasti
    ypos = ymin + 10/(ymax-ymin)
#    ypos = ax.get_ylim()[0] + 0.15 /(ax.get_ylim()[1] - ax.get_ylim()[0])
    ypos2 = ymin + 15/(ymax-ymin)
    ax.annotate("",
            xy=(x0-delta, ypos), xytext=(x0+delta, ypos),  # Začátek a konec šipky
            #xycoords=fig.transFigure,
            arrowprops=dict(arrowstyle="<->", color=col, lw=2),
            ha='center', va='bottom')
    ax.annotate("$\delta$-okolí", xy=(x0+0.02, ypos2), xytext=(x0+0.02, ypos2), color = col)
    #ax.annotate("Globální anotace", xy=(0.5, 0.25), xycoords=fig.transFigure, fontsize=14, color="blue", ha="center", fontweight="bold")


def vykresli_delta2(ax, delta):
    return
    ax.axhline(y = f(x0), color='b')                     # vykreslení osy x
    ax.axhline(y = f(x0-delta), color='b', linestyle="--", alpha=0.2)                    # vykreslení osy y
    ax.axhline(y = f(x0+delta), color='b', linestyle="--", alpha=0.2)                    # vykreslení osy y
    ax.axhspan(f(x0-delta), f(x0+delta), color='blue', alpha=0.05, label="Vybarvená oblast")

def vykresli_mozne(ax, delta):
    # Vybereme pouze body v intervalu
    mask = (x >= x0-delta) & (x <= x0+delta)
    if not mask.any():
        return
    x_subset = x[mask]
    y_subset = y[mask]

    # Najdeme maximum
    min_value = np.min(y_subset)
    max_value = np.max(y_subset)
    #max_index = np.argmax(y_subset)
    #max_x = x_subset[max_index]

    y_v_intervalu = y[(x >= x0-delta) & (x <= x0+delta)]
    ax.axhspan(np.min(y_v_intervalu), np.max(y_v_intervalu), color='blue', alpha=0.1, label="Vybarvená oblast")



def update(val):
    delta = sliderD.val
    epsilon = sliderE.val

    ax.cla()                                                # clear
    ax.plot(x, y)                                           # vykreslení grafu funkce f(x) pro x > x0

    #ax.plot(xzap, f(xzap), default_line_color)             # vykreslení levé části grafu funkce f(x) 
    #line_eq(x,x0-delta,f(x0-delta),x0+delta,f(x0+delta), 'm')   # sečna
    vykresli_delta(ax, delta)

    #ax.axis([x0, x0+hmax, y0, y1])                         # nastavení rozsahů (xmin, xmax, ymin, ymax)
    ax.set_xlabel('x')                                      # popisky os
    ax.set_ylabel('y')

    #ax.axvline(x = 0, color='k')                            # vykreslení osy y
    #ax.axhline(y = 0, color='k')                            # vykreslení osy x

    #vykresli_delta2(ax, delta)
    vykresli_eps(ax, epsilon)
    vykresli_mozne(ax, delta)

    ax.grid(True)

    #ax.set_xlim(-10, 10)
    if (epsilon > 0.0000001) and (delta > 0.0000001):
        #print(epsilon, delta)
        ax.set_ylim(ymin, ymax)

    plt.draw()

fig, ax = plt.subplots(figsize = (12,8))                    # vytvoření grafu
rb_ax = plt.axes([0.1, 0.88, 0.5, 0.12], frameon=False)     # vytvoření checkboxů do nového objektu axes
radio = RadioButtons(rb_ax, ('spoj', 'nesp1', 'nesp2'))
radio.on_clicked(update2)                                   # Propojení s funkcí
slider0 = Slider(plt.axes([0.4, 0.95, 0.4, 0.03]), '$x_0$', x0-hmax - 0.00001, x0+hmax+0.00001, valstep = 0.5, valinit=x0)
slider0.on_changed(update2)

#plt.subplots_adjust(left=0.15, bottom=0.20)                # poloha hlavního grafu

sliderE = Slider(plt.axes([0.2, 0.1, 0.65, 0.03]), '$\epsilon$', 0.00001, 2*hmax+0.00001, valinit=epsilon)
sliderD = Slider(plt.axes([0.2, 0.06, 0.65, 0.03]), '$\delta$', 0.00001, 2*hmax+0.00001, valinit=delta)

#sliderX = Slider(plt.axes([0.2, 0.05, 0.65, 0.03]), '$x$', 0.00001, hmax+0.00001, valinit=x)
sliderE.on_changed(update)
sliderD.on_changed(update)

update2("spoj")

plt.subplots_adjust(bottom=0.22)        # Vytvoření prostoru pro text pod grafem

plt.figtext(0.2, 0.01, 
    "Pro každé $\epsilon$-okolí $f(x_0)$ existuje $\delta$-okolí $x_0$, "
    "že pro všechna x z $\delta$-okolí $x_0$ je $f(x)$ z $\epsilon$-okolí $f(x_0)$.", 
    wrap=True, fontsize=12, ha='left')

update(delta)
plt.show()
