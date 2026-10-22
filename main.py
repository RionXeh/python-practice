import numpy as np
import matplotlib.pyplot as plt

# 1. Definicja osi czasu dla sygnału nieokresowego
dt = 0.01
t = np.arange(-5, 5, dt)

# Definicja pojedynczego impulsu prostokątnego o szerokości od -1 do 1
x_t = np.where(np.abs(t) <= 1, 1.0, 0.0)

# 2. Obliczenie transformaty Fouriera (przybliżenie całki za pomocą FFT)
X_f = np.fft.fft(x_t) * dt
frequencies = np.fft.fftfreq(len(t), dt)

# Przesunięcie składowej zerowej na środek wykresu
X_f_shifted = np.fft.fftshift(X_f)
frequencies_shifted = np.fft.fftshift(frequencies)

# 3. Wizualizacja wyników
fig, axes = plt.subplots(2, 1, figsize=(10, 7))

# Wykres w dziedzinie czasu
axes[0].plot(t, x_t, color='blue', linewidth=2)
axes[0].set_title('Sygnał w dziedzinie czasu: Pojedynczy impuls prostokątny', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Czas ($t$)', fontsize=10)
axes[0].set_ylabel('$x(t)$', fontsize=10)
axes[0].grid(True, linestyle=':', alpha=0.6)
axes[0].set_ylim(-0.2, 1.2)

# Wykres w dziedzinie częstotliwości (widmo amplitudowe - moduł transformaty)
axes[1].plot(frequencies_shifted, np.abs(X_f_shifted), color='red', linewidth=1.5)
axes[1].set_title('Transformata Fouriera: Widmo amplitudowe $|X(f)|$ (funkcja sinc)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Częstotliwość ($f$)', fontsize=10)
axes[1].set_ylabel('$|X(f)|$', fontsize=10)
axes[1].grid(True, linestyle=':', alpha=0.6)
axes[1].set_xlim(-5, 5)

plt.tight_layout()

# Wyświetlenie wykresów
plt.show()
