import numpy as np
import matplotlib.pyplot as plt

# Definice funkce, např. f(x) = x^3 - x - 1
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

plt.ion()           # Interaktivní mód ON
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_plot, y_plot, label='f(x)')
ax.axhline(0, color='gray', linestyle='--')

line_old = ax.axvline(b, color='gray', linestyle='--')
line_a = ax.axvline(a, color='blue', label='a (levá mez)')
line_b = ax.axvline(b, color='red', label='b (pravá mez)')
point, = ax.plot([], [], 'ko', label='střed (x)')

ax.set_title('Bisekční metoda – průběžný postup')
ax.legend()
plt.tight_layout()
input("Stiskni Enter pro další krok...")  # Interaktivní pauza

for i in range(n):
    x = (a + b) / 2
    xs[i] = x

    # Vyhodnocení znaménka
    if f(a) * f(x) < 0:
        line_old.set_xdata([b])
        line_old.set_color("red")
        b = x
    else:
        line_old.set_xdata([a])
        line_old.set_color("blue")
        a = x

    # Aktualizace grafu
    line_a.set_xdata([a])
    line_b.set_xdata([b])
    point.set_data([x], [f(x)])
   
    ax.set_xlabel(f'krok {i+1}, x = {x:.6f}')
    plt.draw()
    plt.pause(0.01)  # Krátká pauza pro aktualizaci

    if input("Stiskni Enter pro další krok...") != "":  # Interaktivní pauza
        break

plt.ioff()
plt.show()