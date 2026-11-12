import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- 1. Parameters ---
Fs = 200.0          # Sampling frequency in Hz
f0 = 50.0           # Frequency to eliminate in Hz
omega = 2 * np.pi * f0 / Fs  # Digital frequency (pi/2 radians/sample)

r2 = 1.0            # Zero radius (1.0 for complete elimination)
r1 = 0.95           # Pole radius (must be < 1 for stability; close to 1 for narrow notch)

# --- 2. Filter Design (Zeros and Poles) ---
# Zeros on the unit circle at +omega and -omega
zeros = [r2 * np.exp(1j * omega), r2 * np.exp(-1j * omega)]
# Poles inside the unit circle at the same angles
poles = [r1 * np.exp(1j * omega), r1 * np.exp(-1j * omega)]

# Convert zeros and poles to transfer function polynomial coefficients (b, a)
b = np.poly(zeros)
a = np.poly(poles)

# Normalize gain so that DC (0 Hz) gain is close to 1
b = b / np.sum(b) * np.sum(a)

# --- 3. Impulse Response ---
num_samples = 60
delta = np.zeros(num_samples)
delta[0] = 1.0
impulse_response = signal.lfilter(b, a, delta)

# --- 4. Frequency Response (Magnitude) ---
w, h = signal.freqz(b, a, worN=1024)
freqs = w * Fs / (2 * np.pi)  # Convert normalized frequency to Hz

# --- 5. Plotting ---
plt.figure(figsize=(12, 5))

# Magnitude Response Plot
plt.subplot(1, 2, 1)
plt.plot(freqs, 20 * np.log10(np.abs(h)), color='b', linewidth=2)
plt.title('Magnitude Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.axvline(f0, color='r', linestyle='--', label=f'Notch ({f0} Hz)')
plt.ylim(-30, 5)
plt.legend()

# Impulse Response Plot
plt.subplot(1, 2, 2)
plt.stem(impulse_response, basefmt="k-")
plt.title('Impulse Response')
plt.xlabel('Sample Index (n)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()