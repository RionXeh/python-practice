import numpy as np

def freqz_lab(B, A, w):
    # Ensure inputs are numpy arrays
    B = np.asarray(B, dtype=complex)
    A = np.asarray(A, dtype=complex)
    w = np.asarray(w, dtype=float)
    
    # Create a matrix of frequency terms: e^(-j * k * w)
    # k goes from 0 to len(B)-1 for numerator, and 0 to len(A)-1 for denominator
    k_b = np.arange(len(B))
    k_a = np.arange(len(A))
    
    # Outer product to compute e^(-j * w * k) for all frequencies and coefficients
    # Shape: (len(w), len(B))
    term_b = np.exp(-1j * np.outer(w, k_b))
    term_a = np.exp(-1j * np.outer(w, k_a))
    
    # Evaluate polynomials B(e^jw) and A(e^jw)
    num = np.dot(term_b, B)
    den = np.dot(term_a, A)
    
    # Compute frequency response
    H = num / den
    return H