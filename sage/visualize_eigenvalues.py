from sage.all import *
import numpy as np
import matplotlib.pyplot as plt
import argparse
from bsd_spectral_matrix import construct_D_operator

def plot_eigenvalues(label: str, N: int = 6, save: bool = True):
    E = EllipticCurve(label)
    rank = E.rank()
    
    D = construct_D_operator(E, N=N)
    eigvals = np.sort(np.real(np.linalg.eigvalsh(D)))
    
    plt.figure(figsize=(10, 6))
    plt.plot(eigvals, 'o-', label='Eigenvalues of $D_E$', markersize=4)
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.7, label='Zero Level')
    
    # Highlight zeros
    zero_mask = np.abs(eigvals) < 1e-6
    plt.plot(np.where(zero_mask)[0], eigvals[zero_mask], 'ro', markersize=8, label=f'Zero Eigenvalues ({sum(zero_mask)})')
    
    plt.title(f'Spectral Operator $D_E$ — Elliptic Curve {label}\n'
              f'Algebraic Rank: {rank} | Conductor: {E.conductor()}')
    plt.xlabel('Eigenvalue Index (sorted)')
    plt.ylabel('Eigenvalue')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    if save:
        filename = f'eigenvalues_{label.replace("/", "_")}.png'
        plt.savefig(f'figures/{filename}', dpi=300, bbox_inches='tight')
        print(f"Plot saved: figures/{filename}")
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--curve', default='37a')
    parser.add_argument('--N', type=int, default=6)
    parser.add_argument('--save', action='store_true', default=True)
    args = parser.parse_args()
    
    plot_eigenvalues(args.curve, args.N, args.save)

if __name__ == "__main__":
    main()
