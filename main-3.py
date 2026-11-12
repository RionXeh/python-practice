import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# ==========================================
# PART 1, 2 & 3: Window Method (Rectangular & Hamming)
# ==========================================
Fs1 = 4000  # Sampling frequency in Hz
fc1 = 1000  # Cutoff frequency in Hz
norm_fc1 = fc1 / (Fs1 / 2)  # Normalized cutoff frequency (fraction of Nyquist)

# 1. Plot magnitude responses of rectangular window for different lengths M
Ms = [11, 51, 101]

plt.figure(figsize=(10, 5))
for M in Ms:
    # Design filter using rectangular window ('boxcar')
    h_rect = signal.firwin(M, norm_fc1, window='boxcar', pass_zero='lowpass')
    w, h_resp = signal.freqz(h_rect, worN=1024, fs=Fs1)
    plt.plot(w, 20 * np.log10(np.abs(h_resp) + 1e-10), label=f'Rectangular M={M}')

plt.title('Magnitude Responses: Rectangular Window for Different Lengths (M)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.legend()
plt.xlim(0, Fs1 / 2)
plt.ylim(-80, 5)
plt.tight_layout()
plt.show()

# 2. Plot magnitude responses comparing Rectangular and Hamming windows for M = 51
M_fixed = 51
h_rect_51 = signal.firwin(M_fixed, norm_fc1, window='boxcar', pass_zero='lowpass')
h_hamm_51 = signal.firwin(M_fixed, norm_fc1, window='hamming', pass_zero='lowpass')

plt.figure(figsize=(10, 5))
w, h_rect_resp = signal.freqz(h_rect_51, worN=1024, fs=Fs1)
w, h_hamm_resp = signal.freqz(h_hamm_51, worN=1024, fs=Fs1)

plt.plot(w, 20 * np.log10(np.abs(h_rect_resp) + 1e-10), label=f'Rectangular M={M_fixed}')
plt.plot(w, 20 * np.log10(np.abs(h_hamm_resp) + 1e-10), label=f'Hamming M={M_fixed}')
plt.title('Rectangular vs. Hamming Window (M = 51)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.legend()
plt.xlim(0, Fs1 / 2)
plt.ylim(-80, 5)
plt.tight_layout()
plt.show()


# ==========================================
# PART 4, 5 & 6: Kaiser Window vs. Parks-McClellan
# ==========================================
Fs2 = 5000  # Sampling frequency in Hz
f_pass = 1000  # Passband corner frequency in Hz
f_stop = 1500  # Stopband corner frequency in Hz
Rp = 1.0  # Passband ripple in dB
Rs = 30.0  # Stopband attenuation in dB

# Normalized transition width and band edges
width = (f_stop - f_pass) / (Fs2 / 2)
fp_norm = f_pass / (Fs2 / 2)
fst_norm = f_stop / (Fs2 / 2)

# Calculate ripple bounds from dB specifications
delta1 = (10**(Rp / 20) - 1) / (10**(Rp / 20) + 1)
delta2 = 10**(-Rs / 20)

# --- A. Kaiser Window Design ---
# kaiserord estimates the required filter length and beta parameter
numtaps_kaiser, beta = signal.kaiserord(Rs, width)
if numtaps_kaiser % 2 == 0:
    numtaps_kaiser += 1  # Ensure odd length for Type I linear phase

# Ideal cutoff is typically midway through the transition band
fc_kaiser = fp_norm + width / 2
h_kaiser = signal.firwin(numtaps_kaiser, fc_kaiser, window=('kaiser', beta), pass_zero='lowpass')

print(f"Kaiser Filter Length (M): {numtaps_kaiser}")


# --- C. Plot and Verify Requirements ---
plt.figure(figsize=(10, 6))
w, h_k_resp = signal.freqz(h_kaiser, worN=2048, fs=Fs2)

plt.plot(w, 20 * np.log10(np.abs(h_k_resp) + 1e-10), label=f'Kaiser (Length = {numtaps_kaiser})')

# Boundary and requirement indicator lines
plt.axvline(f_pass, color='gray', linestyle='--', alpha=0.7, label='Passband Edge (1 kHz)')
plt.axvline(f_stop, color='gray', linestyle=':', alpha=0.7, label='Stopband Edge (1.5 kHz)')
plt.axhline(-Rp, color='r', linestyle='-.', alpha=0.5, label=f'Max Passband Ripple (-{Rp} dB)')
plt.axhline(-Rs, color='g', linestyle='-.', alpha=0.5, label=f'Min Stopband Attenuation (-{Rs} dB)')

plt.title('Comparison of Kaiser Window and Parks-McClellan Filters')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.legend(loc='lower left')
plt.xlim(0, Fs2 / 2)
plt.ylim(-50, 5)
plt.tight_layout()
plt.show()