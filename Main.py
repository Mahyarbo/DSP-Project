import numpy as np
import matplotlib.pyplot as plt

# =========================
# SYSTEM MODEL (unknown plant)
# =========================
wopt = np.array([
    0.01, 0.02, -0.04, -0.08,
    0.15, -0.3, 0.45, 0.6,
    0.6, 0.45, -0.3, 0.15,
    -0.08, -0.04, 0.02, 0.01
])

# =========================
# SIGNAL GENERATION
# =========================
def generate_input(N, a=0.0):
    x = np.zeros(N)
    noise = np.random.randn(N)
    for i in range(1, N):
        x[i] = a * x[i-1] + noise[i]
    return x

# =========================
# FDAF CLASS (UNIFIED)
# =========================
class FDAF:
    def __init__(self, L=16, R=16, mu=0.05, constrained=True, normalized=False):
        self.L = L
        self.R = R
        self.mu = mu
        self.constrained = constrained
        self.normalized = normalized

        self.w = np.zeros(L)
        self.nfft = 2 * R

    def update(self, x_block, d_block):

        X = np.fft.fft(x_block, self.nfft)
        W = np.fft.fft(self.w, self.nfft)

        # output
        Y = X * W
        y = np.real(np.fft.ifft(Y))[:self.R]

        # error
        e = d_block - y

        # gradient
        E = np.fft.fft(e, self.nfft)
        grad = np.real(np.fft.ifft(np.conj(X) * E))[:self.L]

        # normalization
        if self.normalized:
            norm = np.sum(np.abs(X)**2) + 1e-8
            grad = grad / norm

        # update
        self.w += self.mu * grad

        # constraint (simplified projection)
        if self.constrained:
            self.w[self.L//2:] *= 0.0

        return e

# =========================
# SIMULATION FUNCTION
# =========================
def run_simulation():
    N = 2000
    L = 16
    R = 16

    x = generate_input(N, a=0.9)

    fdaf = FDAF(L=L, R=R, mu=0.05, constrained=True, normalized=True)

    msd = []

    for i in range(0, N - R, R):

        x_block = x[i:i+R]

        d_block = np.convolve(x_block, wopt)[:R]

        e = fdaf.update(x_block, d_block)

        msd.append(np.linalg.norm(wopt - fdaf.w)**2)

    return msd

# =========================
# RUN + PLOT
# =========================
msd = run_simulation()

plt.plot(msd)
plt.title("FDAF Learning Curve (MSD)")
plt.xlabel("Iteration")
plt.ylabel("MSD")
plt.grid()
plt.show()
