import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# ==========================================
# 4.2 Custom freqs_lab Function definition
# ==========================================
def freqs_lab(B, A, Om):
    """
    Frequency response of transmittance H(s) = B(s) / A(s)
    Om - frequency in rad/s, s = j * Om
    """
    Om = np.asarray(Om, dtype=float)
    s = 1j * Om
    num_vals = np.polyval(B, s)
    den_vals = np.polyval(A, s)
    H = num_vals / den_vals
    return H


f0 = 50.0                        # Target frequency in Hz
Omega_0 = 2 * np.pi * f0         # Angular frequency Omega_0 ≈ 314.16 rad/s

c = Omega_0**2
b = Omega_0**2
a = 15               # Damping parameter

B = [1, 0, c]
A = [1, a, b]

# Zakres częstotliwości od 45 do 55 Hz (przeliczony na rad/s)
Om = np.linspace(45 * 2 * np.pi, 55 * 2 * np.pi, 1000)

# 1. Użycie funkcji freqs_lab
H = freqs_lab(B, A, Om)

# 2. Użycie funkcji freqs z SciPy do porównania
_, H_scipy = signal.freqs(B, A, worN=Om)

# Czas od 0 do 0.5 sekundy dla odpowiedzi impulsowej
t, y_impulse = signal.impulse((B, A), T=np.linspace(0, 0.5, 1000))


# ==========================================
# Wykresy (2 podwykresy: charakterystyka i odpowiedź)
# ==========================================
plt.figure(figsize=(10, 8))

# 1. Charakterystyka amplitudowa (45 - 55 Hz)
plt.subplot(2, 1, 1)
freqs_hz = Om / (2 * np.pi)
plt.plot(freqs_hz, 20 * np.log10(np.abs(H)), 'b-', linewidth=2, label='freqs_lab')
plt.plot(freqs_hz, 20 * np.log10(np.abs(H_scipy)), 'r--', linewidth=1, label='scipy.signal.freqs')
plt.title('Charakterystyka amplitudowa filtru (45 - 55 Hz)')
plt.xlabel('Częstotliwość (Hz)')
plt.ylabel('Amplituda (dB)')
plt.axvline(50, color='green', linestyle=':', label='Tłumienie 50 Hz')
plt.grid(True)
plt.legend()

# 2. Odpowiedź impulsowa (0 - 0.5 s)
plt.subplot(2, 1, 2)
plt.plot(t, y_impulse, color='darkorange', linewidth=1.2)
plt.title('Odpowiedź impulsowa (0 do 0.5 s)')
plt.xlabel('Czas (s)')
plt.ylabel('Amplituda')
plt.grid(True)

plt.tight_layout()
plt.show()