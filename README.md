# Monte Carlo Simulations

This repository contains simulations showing the convergence of empirical results toward theoretical expectations when the number of observations increases 

## 1) Approximation of π

**Idea:**  
- Generate random points uniformly in the square [-1, 1] × [-1, 1]
- Count how many fall inside the unit circle defined by x^2 + y^2 < 1

**Key facts:** 
- Area of the square = 4
- Area of the unit circle = π
- Ratio: points_in_circle / total_points ≈ π / 4

**Estimation:**
- π ≈ 4 × (points_in_circle / total_points)


## 2) Rolling a fair dice

**Idea:**
- Simulate rolling a 6-sided fair dice multiple times

**Theorethical probability:**
- 1/6 for each face


## 3) Coin toss

**Idea:**
- Simulate flipping a fair coin where 1 = heads and 0 = tails

**Theorethical probability:**
- 1/2 for each face

All these simulations illustrates the Law of Large Number
