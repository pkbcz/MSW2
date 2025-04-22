import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons
from matplotlib.patches import Rectangle, Polygon

def g(x):                                       # definice funkce
    return (x)**2                               # např. x^2
def f(x):                                       # definice funkce
    return np.sin(x)                            # např. sinus

a = 0                                           # interval pro integraci
b = np.pi

n_points = 100                                  # počet bodů pro vykreslení funkce
x_vals = np.linspace(a, b, n_points)
y_vals = f(x_vals)


options = ['Rectangular', 'Trapezoidal']        # seznam popisků pro checkboxy
initial_state = [False, False]                  # počáteční stav checkboxů

# různé způsoby
def integral_obdel0(x, dx, n_rects):            # výpočet určitého integrálu
    heights = f(x)                              # výška obdélníků jako funkční hodnota levého bodu
    integral = np.sum(heights * dx)
    rectangles = [Rectangle((x[i], 0), dx, heights[i], edgecolor='black', facecolor='blue', alpha=0.3) for i in range(n_rects)]
    return integral, rectangles, []

def integral_obdel(x, dx, n_rects):             # výpočet určitého integrálu
    xp = (x[:-1]+ x[1:]) / 2
    heights = f(xp)                             # výška obdélníků jako funkční hodnota středu intervalu
    integral = np.sum(heights * dx)
    rectangles = [Rectangle((x[i], 0), dx, heights[i], edgecolor='black', facecolor='blue', alpha=0.2) for i in range(n_rects)]
    lines = [Rectangle((xp[i], 0), 0, heights[i], edgecolor='b', facecolor='none', alpha=0.07) for i in range(n_rects)]
    return integral, rectangles, lines

def integral_licho(x, dx, n_rects):             # výpočet určitého integrálu
    y = f(x)
    heights = (y[:-1] + y[1:]) / 2              # výška obdélníků jako aritmetický průměr krajních hodnot
    integral = np.sum(heights * dx)
    rectangles = [Polygon([(x[i],0), (x[i],y[i]), (x[i+1],y[i+1]), (x[i+1],0)], 
                       closed=True, edgecolor='black', facecolor='red', alpha=0.2) for i in range(n_rects)]
    return integral, rectangles

def update(val):                                # vytvoření a aktualizace grafu
    n_rects = int(slider.val)
    ax.clear()
    ax.plot(x_vals, y_vals, label='f(x)')
    y_max = ax.get_ylim()[1]
    dx = (b - a) / n_rects
    x = np.linspace(a, b, n_rects + 1)
    if check.get_status()[0]:
        integral, rectangles, lines = integral_obdel(x, dx, n_rects)
        for rect in rectangles:                 # obdélníky
            ax.add_patch(rect)
        for line in lines:                      # středy obdélníků
            ax.add_patch(line)
        ax.text(0.5 * (a + b), 0.3*y_max, f'Rectangular = {integral:.4f}', fontsize=12, ha='center')

    if check.get_status()[1]:
        integral, rectangles = integral_licho(x, dx, n_rects)
        for rect in rectangles:                 # lichoběžníky
            ax.add_patch(rect)
        ax.text(0.5 * (a + b), 0.2*y_max, f'Trapezoidal = {integral:.4f}', fontsize=12, ha='center')

    #ax.grid(True)
    plt.draw()

fig, ax = plt.subplots()                        # vytvoření grafu
check_ax = plt.axes([0.1, 0.88, 0.5, 0.12], frameon=False)   # vytvoření checkboxů do nového objektu axes
check = CheckButtons(check_ax, options, initial_state)

plt.subplots_adjust(left=0.15, bottom=0.17)     # poloha hlavního grafu

# vytvoření posuvníku do nového objektu axes
slider = Slider(plt.axes([0.2, 0.05, 0.65, 0.03]), 'Počet obdélníků', 1, 100, valinit=10, valstep=1)
slider.on_changed(update)
check.on_clicked(update)

update(None)                                    # prvotní inicializace grafu
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
