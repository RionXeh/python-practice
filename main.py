import numpy as np
import matplotlib.pyplot as plt

# Tworzenie okna z trzema wykresami (po jednym dla każdego warunku)
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

# --- 1. Naruszenie warunku 1: x(t) = 1/t (brak całkowalności w otoczeniu 0) ---
t1 = np.linspace(0.01, 1, 1000)
x1 = 1 / t1

axes[0].plot(t1, x1, color='blue', linewidth=1.5)
axes[0].set_title('1. Naruszenie warunku całkowalności: $x(t) = 1/t$', fontsize=12, fontweight='bold')
axes[0].set_ylabel('$x(t)$', fontsize=10)
axes[0].grid(True, linestyle=':', alpha=0.6)

# --- 2. Naruszenie warunku 2: x(t) = sin(pi / t) (nieskończenie wiele ekstremów near 0) ---
t2 = np.linspace(0.001, 1, 2000)
x2 = np.sin(np.pi / t2)

axes[1].plot(t2, x2, color='green', linewidth=1.0)
axes[1].set_title('2. Nieskończona liczba oscylacji: $x(t) = \\sin(\\pi / t)$', fontsize=12, fontweight='bold')
axes[1].set_ylabel('$x(t)$', fontsize=10)
axes[1].grid(True, linestyle=':', alpha=0.6)

# --- 3. Naruszenie warunku 3: Nieskończenie wiele sekcji o malejącej szerokości i wysokości ---
# Budujemy sygnał impulsowy z nieskończoną liczbą zwężających się sekcji w przedziale (0, 1]
t3 = np.linspace(0.001, 1, 2000)
x3 = np.zeros_like(t3)

# Symulacja kilku pierwszych kroków geometrycznych (połowa szerokości, połowa wysokości)
for n in range(1, 8):
    right = 1 / (2**n)
    left = 1 / (2**(n-1))
    height = 1 / (2**n)
    mask = (t3 > right) & (t3 <= left)
    x3[mask] = height

axes[2].plot(-t3, x3, color='purple', linewidth=1.5, drawstyle='steps-post')
axes[2].set_title('3. Nieskończona liczba nieciągłości (sekcje o połowę mniejsze)', fontsize=12, fontweight='bold')
axes[2].set_xlabel('Czas ($t$)', fontsize=10)
axes[2].set_ylabel('$x(t)$', fontsize=10)
axes[2].grid(True, linestyle=':', alpha=0.6)

# Dopasowanie układu i wyświetlenie
plt.tight_layout()
plt.show()
