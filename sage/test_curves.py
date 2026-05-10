from sage.all import *
from bsd_spectral_matrix import construct_D_operator

curves = ['37a', '11a', '389a', '5077a']  # Rank 0,1,2,3 examples

for label in curves:
    E = EllipticCurve(label)
    rank = E.rank()
    D = construct_D_operator(E, N=4)
    eigvals = np.abs(np.linalg.eigvals(D))
    zero_count = sum(e < 1e-5 for e in eigvals)
    print(f"{label:8} | Rank: {rank} | Spectral Zeros: {zero_count}")
