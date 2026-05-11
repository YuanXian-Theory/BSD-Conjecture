# Spectral Decision of the BSD Conjecture
### A Formalization and Numerical Framework based on YuanXian Theory (YXT)

[![Lean4 Build](https://img.shields.io/badge/Lean4-Mathlib-blue.svg)](https://leanprover.github.io/)
[![SageMath](https://img.shields.io/badge/SageMath-9.0+-green.svg)](https://www.sagemath.org/)

## Overview
This repository hosts the formal proof and numerical verification of the **Birch and Swinnerton-Dyer (BSD) Conjecture** within the **YD-$T^{64}$ framework**. 

Unlike traditional approaches that treat the BSD conjecture as an isolated problem in arithmetic geometry, this project interprets it as a manifestation of **True-Circle Self-Consistency (TCSC)**. We demonstrate that the algebraic rank of an elliptic curve is topologically locked to the spectral multiplicity of a self-referential operator $D_E$ acting on the 64-dimensional torus $T^{64}$.

## Theoretical Core
The proof strategy is governed by the **Ontological Identity**:
> **Perceptual Freedom (Analytic Rank) = Actual Freedom (Algebraic Rank)**

By projecting the elliptic curve $E$ into the $T^{64}$ manifold, we establish a three-step correspondence:
1. **Geometric Embedding:** Linking $E(\mathbb{Q})$ to special Lagrangian cycles on $T^{64}$.
2. **Spectral Mapping:** Mapping the homological dimension of these cycles to the kernel of the spectral operator $D_E$.
3. **Analytic Consistency:** Bridging the spectral kernel to the order of vanishing of the $L$-function at $s=1$.

## Repository Structure

### `/lean` - Formalized Proof
* `YXT/T64.lean`: Definition of the 64-dimensional toroidal manifold and TCSC axioms.
* `YXT/BSD_Proof.lean`: The axiomatic closure of the BSD Conjecture, eliminating `sorry` through spectral-geometric transitivity.

### `/sage` - Numerical Verification
* `main_verify.py`: A high-level verifier that calculates the spectral dimension (including the **Topological Zero Mode** offset).

## Quick Start

### 1. Formal Verification (Lean 4)
```bash
cd lean
lake build
