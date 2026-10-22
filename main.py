import numpy as np
import matplotlib.pyplot as plt

# 1. Konfiguracja osi czasu i okresu
f = 1                     # Częstotliwość w Hz
T = 1.0 / f               # Okres (czas trwania jednego pełnego cyklu)
t = np.linspace(-1.5, 1.5, 1000, endpoint=False)

# 2. Offset czasu i znormalizowany czas do okresu
offset_czasu = -0.25
t_okres_przesuniety = (t - offset_czasu) % T

# 3. Definicja przedziałowa z uwzględnieniem offsetu poziomego
sygnal_poziomy = np.where((t_okres_przesuniety >= 0) & (t_okres_przesuniety < T / 2), 1, 0)

# 4. Wizualizacja (rysujemy sygnal_poziomy)
plt.figure(figsize=(10, 4))
plt.plot(t, sygnal_poziomy, color='tab:blue', linewidth=2)
plt.title('Fala prostokątna z offsetem poziomym (za pomocą NumPy)')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.ylim(-0.2, 1.2)
plt.grid(True)
plt.tight_layout()
plt.show()

