import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

def linear_difference_eq(b, a, x):
    """
    Implements an Nth-order linear constant-coefficient difference equation,
    comparable to MATLAB's filter(b, a, x) / SciPy's lfilter(b, a, x).
    """
    M = len(b) - 1
    N = len(a) - 1
    L = len(x)
    y = np.zeros(L)
    
    # Normalize by a[0]
    a0 = a[0]
    b_norm = [bi / a0 for bi in b]
    a_norm = [ai / a0 for ai in a]
    
    for n in range(L):
        # Feedforward sum: sum(b[m] * x[n-m])
        sum_b = 0
        for m in range(M + 1):
            if n - m >= 0:
                sum_b += b_norm[m] * x[n - m]
                
        # Feedback sum: sum(a[k] * y[n-k]) for k >= 1
        sum_a = 0
        for k in range(1, N + 1):
            if n - k >= 0:
                sum_a += a_norm[k] * y[n - k]
                
        y[n] = sum_b - sum_a
        
    return y

# --- Test i porównanie z SciPy ---
b = [1.0, 0.5]     # Współczynniki feedforward
a = [1.0, 0.25]    # Współczynniki feedback
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

# Obliczenia
y_custom = linear_difference_eq(b, a, x)
y_scipy = lfilter(b, a, x)

print("Custom Difference Eq:", y_custom)
print("SciPy lfilter:       ", y_scipy)
print("Results Match:       ", np.allclose(y_custom, y_scipy))

# --- Generowanie wykresów ---
plt.figure(figsize=(10, 7))

# Wykres sygnału wejściowego x[n]
plt.subplot(2, 1, 1)
plt.stem(x, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Sygnał wejściowy x[n]')
plt.xlabel('Indeks n')
plt.ylabel('Amplituda')
plt.grid(True)

# Wykres sygnału wyjściowego y[n]
plt.subplot(2, 1, 2)
plt.stem(y_custom, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Sygnał wyjściowy y[n] (Filtr cyfrowy)')
plt.xlabel('Indeks n')
plt.ylabel('Amplituda')
plt.grid(True)

plt.tight_layout()
plt.show()