import matplotlib.pyplot as plt
import numpy as np

# 1. Definicja parametrów sygnału
T0 = 1.0  # Okres podstawowy (T)
T1 = T0 / 10  # Szerokość impulsu (w Twoim kodzie to było T/10)
omega = 2 * np.pi / T0

# 2. Zakres harmonicznych k (np. od -20 do 20)
N = 20
k_values = np.arange(-N, N + 1)


# 3. Funkcja obliczająca współczynniki analitycznie
def oblicz_Xk_analitycznie(k_vals, T0, T1):
  omega_val = 2 * np.pi / T0
  X_k = np.zeros(len(k_vals), dtype=complex)

  for i, k in enumerate(k_vals):
    if k == 0:
      # Przypadek dla k = 0 (wartość średnia sygnału)
      # W zależności od definicji współczynnika może to być T1/T0 lub 2*T1/T0
      X_k[i] = 2*T1 / T0
    else:
      # Przypadek dla k != 0 (wzór podany przez Ciebie)
      # Uwaga: jeśli sygnał jest przesunięty w czasie, często dochodzi tu czynnik fazowy e^(-j * k * omega * offset)
      X_k[i] = np.sin(k * omega_val * T1) / (k * np.pi)

  return X_k
offset_czasu = -0.25
X_k_przesuniete = X_k * np.exp(-1j * k * omega * offset_czasu)


# Obliczenie współczynników
X_k = oblicz_Xk_analitycznie(k_values, T0, T1)

# 4. Wizualizacja wyników
plt.figure(figsize=(10, 4))
plt.stem(k_values, np.real(X_k), basefmt=" ", linefmt="tab:green", markerfmt="o")
plt.title("Moduł współczynników Fouriera |X_k| (wzór analityczny)")
plt.xlabel("Indeks harmonicznej k")
plt.ylabel("|X_k|")
plt.grid(True)
plt.tight_layout()
plt.show()

