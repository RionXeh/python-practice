import numpy as np
import matplotlib.pyplot as plt

# 1. Konfiguracja sygnału
# Częstotliwość próbowania (ile punktów na sekundę)
fs = 1000.0 
# Czas trwania sygnału (w sekundach)
t = np.linspace(0, 1.0, int(fs), endpoint=False)

# Sygnał składający się z dwóch częstotliwości: 50 Hz oraz 120 Hz
f_1, f_2 = 50, 120
sygnal = np.sin(2 * np.pi * f_1 * t) + 0.5 * np.sin(2 * np.pi * f_2 * t)

# 2. Obliczenie Szybkiej Transformaty Fouriera (FFT)
n = len(sygnal)
fft_wynik = np.fft.fft(sygnal)
# Wyznaczenie osi częstotliwości (bierzemy tylko dodatnią połowę widma)
czestotliwosci = np.fft.fftfreq(n, d=1/fs)[:n // 2]
# Amplituda (skalowana długością sygnału)
amplituda = 2.0 / n * np.abs(fft_wynik[:n // 2])

# 3. Wizualizacja wyników
plt.figure(figsize=(12, 6))

# Wykres sygnału w dziedzinie czasu
plt.subplot(2, 1, 1)
plt.plot(t[:100], sygnal[:100], color='tab:blue') # Pokazujemy pierwsze 100 punktów
plt.title('Sygnal w dziedzinie czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid(True)

# Wykres widma częstotliwościowego (Fourier)
plt.subplot(2, 1, 2)
plt.plot(czestotliwosci, amplituda, color='tab:orange')
plt.title('Widmo czestotliwosciowe (FFT)')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.grid(True)
plt.xlim(0, 200) # Ograniczamy widok do 200 Hz, aby dobrze widzieć piki

plt.tight_layout()
plt.show()
