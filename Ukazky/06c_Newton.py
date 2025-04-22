import numpy as np
import matplotlib.pyplot as plt

# Funkce a její derivace
def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

# Počáteční bod a počet kroků
x0 = 2.5
n = 10
xs = [x0]

# Vykreslení základního grafu
x_plot = np.linspace(0.5, 2.5, 400)
y_plot = f(x_plot)

plt.ion()
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_plot, y_plot, label='f(x)')
ax.axhline(0, color='gray', linestyle='--')

# Grafické prvky: aktuální bod, tečna, průsečík a svislá čára
point, = ax.plot([], [], 'ko', label='x (aktuální)')
tangent_line, = ax.plot([], [], 'g--', label='tečna')
x_new_dot, = ax.plot([], [], 'ro', label='x nový (průsečík tečny)')
vertical_line = ax.axvline(x0, color='orange', linestyle=':', label='svislá k f(x)')

ax.set_title('Newtonova metoda – průběžný postup')
ax.legend()
plt.tight_layout()
input("Stiskni Enter pro start...")

x = x0
for i in range(n):
    fx = f(x)
    dfx = df(x)

    if dfx == 0:
        print("Derivace je nulová, nelze pokračovat.")
        break

    # Výpočet nového bodu
    x_new = x - fx / dfx
    fx_new = f(x_new)
    xs.append(x_new)

    # Tečna: y = f(x) + f'(x)(t - x)
    t = np.linspace(x - 1, x + 1, 50)
    tangent = fx + dfx * (t - x)

    # Aktualizace grafických prvků
    point.set_data([x], [fx])
    tangent_line.set_data(t, tangent)
    x_new_dot.set_data([x_new], [0])                     # průsečík s osou x
    vertical_line.set_xdata([x_new])                     # svislá čára k f(x_new)

    ax.set_xlabel(f'Krok {i+1}: x = {x:.6f}, x_new = {x_new:.6f}')
    plt.draw()
    plt.pause(0.01)

    if input("Stiskni Enter pro další krok (nebo něco napiš pro konec)...") != "":
        break

    x = x_new

plt.ioff()
plt.show()
