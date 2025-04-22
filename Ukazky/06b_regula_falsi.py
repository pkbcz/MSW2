import numpy as np
import matplotlib.pyplot as plt

# Definice funkce
def f(x):
    return x**3 - x - 1

# Počáteční interval a počet kroků
a0, b0 = 1, 2
n = 12

a = a0
b = b0
xs = np.empty(n)

# Vykreslení základního grafu funkce
x_plot = np.linspace(a0 - 0.5, b0 + 0.5, 400)
y_plot = f(x_plot)

plt.ion()
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_plot, y_plot, label='f(x)')
ax.axhline(0, color='gray', linestyle='--')

# První zobrazení mezí
line_old = ax.axvline(b, color='gray', linestyle='--', linewidth= 1)
line_a = ax.axvline(a, color='blue', label='a (levá mez)')
line_b = ax.axvline(b, color='red', label='b (pravá mez)')
point, = ax.plot([], [], 'ko', label='nový bod (x)')

# Tětiva mezi (a, f(a)) a (b, f(b))
secant_line, = ax.plot([a, b], [f(a), f(b)], 'y--', linewidth= 0.5)

ax.set_title('Regula falsi – průběžný postup')
ax.legend()
plt.tight_layout()
input("Stiskni Enter pro start...")

# Regula falsi iterace
for i in range(n):
    fa = f(a)
    fb = f(b)

    # Výpočet nového bodu
    x = b - fb * (b - a) / (fb - fa)
    fx = f(x)
    xs[i] = x

    # Určení nové meze a zaznamenání staré
    if fa * fx < 0:
        line_old.set_xdata([b])
        line_old.set_color("red")
        b = x
    else:
        line_old.set_xdata([a])
        line_old.set_color("blue")
        a = x

    # Aktualizace vizualizace
    line_a.set_xdata([a])
    line_b.set_xdata([b])
    point.set_data([x], [fx])
    
    # Tětiva
    secant_line.set_data([a, b], [f(a), f(b)])

    ax.set_xlabel(f'Krok {i+1}: x = {x:.6f}')
    plt.draw()
    plt.pause(0.01)

    if input("Stiskni Enter pro další krok (nebo něco napiš pro konec)...") != "":
        break

plt.ioff()
plt.show()
