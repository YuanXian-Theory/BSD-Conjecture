from sage.all import *
import numpy as np
from bsd_spectral_matrix import construct_D_operator
import argparse

def test_curve(label: str, N: int = 5):
    try:
        E = EllipticCurve(label)
        rank = E.rank()
        D = construct_D_operator(E, N=N)
        eigvals = np.abs(np.linalg.eigvalsh(D))
        zero_count = int(sum(e < 1e-6 for e in eigvals))
        
        status = "✓ MATCH" if zero_count == rank else "⚠ Discrepancy"
        print(f"{label:12} | Rank: {rank:2} | Spectral Zeros: {zero_count:2} | {status}")
        return rank == zero_count
    except Exception as e:
        print(f"{label:12} | Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, default=5, help='Discretization parameter')
    args = parser.parse_args()
    
    curves = [
        '11a', '37a', '389a', '5077a',   # Rank 0, 0, 2, 3
        '433a', '571a', '234446a1'       # Higher rank examples
    ]
    
    print("BSD Spectral Test Suite")
    print("=" * 60)
    print(f"Discretization N = {args.N} (T^64 projection)")
    print("-" * 60)
    
    successes = sum(test_curve(c, args.N) for c in curves)
    print("-" * 60)
    print(f"Passed: {successes}/{len(curves)} curves")

if __name__ == "__main__":
    main()
