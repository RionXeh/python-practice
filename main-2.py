import matplotlib.pyplot as plt
import numpy as np

# Parametry wspólne
A = 1.0  # Amplituda
phi = 0.0  # Faza początkowa
N = 40  # Liczba próbek (n = 0, 1, ..., N-1)
n = np.arange(N)
dex = 1

# ==========================================
# 1. Równanie (5.1): x[n] = A * cos(omega_0 * n + phi)
# Porównanie omega_0 oraz omega_0 + 2*pi (aliasing / okresowość)
# ==========================================
omega_0 = np.pi / 4  # Przykładowa częstotliwość cyfrowa
omega_shifted = omega_0 + 2 * np.pi

x1 = A * np.cos(omega_0 * n + phi)
x1_shifted = A * np.cos(omega_shifted * n + phi) * np.exp(-dex * n)

plt.figure(figsize=(12, 9))

plt.subplot(3, 1, 1)
plt.stem(n, x1, label=f"omega_0 = pi/4", basefmt="k-")
plt.stem(
    n,
    x1_shifted,
    linefmt="r--",
    markerfmt="ro",
    label=f"omega_0 + 2*pi (to samo!)",
)
plt.title(
    "Porównanie sygnałów: omega_0 oraz omega_0 + 2*pi (Równanie 5.1)\nZauważ, że sygnały się pokrywają!"
)
plt.xlabel("Indeks próbki n")
plt.ylabel("Amplituda")
plt.legend()
plt.grid(True)



# ==========================================
# 3. Generowanie sygnału z równania różnicowego:
# x[n] = 2*cos(omega_0) * x[n-1] - x[n-2]
# ==========================================
# Inicjalizacja tablicy wynikowej

x_diff = np.zeros(N)
omega_diff = np.pi / 6  # Częstotliwość dla równania różnicowego

# Warunki początkowe (np. dla n=0 i n=1, wynikające z postaci cosinusowej)
# x[-1] = cos(-omega) = cos(omega)
# x[-2] = cos(-2*omega) = cos(2*omega)
# Możemy też wygenerować bezpośrednio iteracyjnie:
x_diff[0] = np.cos(0)  # x[0] = 1
x_diff[1] = np.cos(omega_diff)  # x[1] = cos(omega)

for i in range(2, N):
  x_diff[i] = (
      2 * np.cos(omega_diff) *np.exp(-dex) * x_diff[i - 1] - np.exp(-2*dex) * x_diff[i - 2]
  )

plt.subplot(3, 1, 3)
plt.stem(n, x_diff, linefmt="g-", markerfmt="go", basefmt="k-")
plt.title(f"Sygnał z równania różnicowego: x[n] = 2*cos(omega)*x[n-1] - x[n-2]")
plt.xlabel("Indeks próbki n")
plt.ylabel("Amplituda")
plt.grid(True)

plt.tight_layout()
plt.show()