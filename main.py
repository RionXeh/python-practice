import numpy as np
import matplotlib.pyplot as plt

# Definicja osi czasu
t = np.linspace(-0.5, 0.5, 1000)
harmonics_list = [1, 3]
offset = -0.25
plt.figure(figsize=(10, 6))

# Rysowanie idealnej fali prostokątnej jako punktu odniesienia
ideal_square = np.sign(np.sin(6*(t-offset)))
plt.plot(t, ideal_square, label='Idealna fala prostokątna', color='black', linestyle='--', linewidth=2)

# Obliczanie i rysowanie aproksymacji szeregiem Fourieria dla N harmonicznych
for N in harmonics_list:
    f_approx = np.zeros_like((6*(t-offset)))
    for n in range(1, N + 1, 2):
        f_approx += (4 / np.pi) * (1 / n) * np.sin(n * (6*(t-offset)))
    plt.plot(t, f_approx, label=f'N = {N} harmonicznych', linewidth=1.5)

# Stylizacja wykresów
plt.title('Aproksymacja fali prostokątnej szeregiem Fourieria', fontsize=14, fontweight='bold')
plt.xlabel('Czas (t)', fontsize=12)
plt.ylabel('Amplituda', fontsize=12)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', frameon=True)
plt.tight_layout()

# Wyświetlenie wykresów
plt.show()
