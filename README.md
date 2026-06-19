# DSP Project
# Stochastic Analysis of Frequency-Domain Adaptive Filters (FDAF)

This repository contains a Python implementation and simulation framework for Frequency-Domain Adaptive Filters (FDAF), based on the paper:

Feiran Yang (2024)  
"Stochastic Analysis of Frequency-Domain Adaptive Filters"  
EURASIP Journal on Advances in Signal Processing

---

## Project Description

This project implements and analyzes different versions of FDAF algorithms and studies their stochastic behavior in adaptive filtering problems.

The main goal is to reproduce the theoretical results of the paper using numerical simulations.

---

## Implemented Algorithms

- Constrained FDAF
- Unconstrained FDAF
- Step-Normalized FDAF
- LMS (for comparison)

---

## What This Project Does

- Adaptive filtering in frequency domain
- System identification
- Convergence analysis
- Performance evaluation using:
  - MSD (Mean Square Deviation)
  - EMSE (Excess Mean Square Error)
- Comparison of FDAF variants
- Exact and under-modeling experiments

---

## System Model

The unknown system is modeled as a 16-tap FIR filter:

h = [0.01, 0.02, -0.04, -0.08,
     0.15, -0.3, 0.45, 0.6,
     0.6, 0.45, -0.3, 0.15,
     -0.08, -0.04, 0.02, 0.01]

---

## Requirements

Install dependencies using:

pip install -r requirements.txt

Required packages:
- numpy
- matplotlib

---

## How to Run

Run the simulation using:

python main.py

---

## Output

The program generates:

- Learning curve (MSD)
- Error convergence plots
- Comparison between FDAF variants
- Performance evaluation under different conditions

---

## Experimental Setup

- Filter length: 16
- Block size: 16
- Input signal: white / correlated (AR)
- Step size: adjustable

---

## Notes

This is an independent implementation based on the published paper.
No original code or figures from the paper are included.

---

## Citation

If you use this work, please cite:

@article{yang2024fdaf,
  title={Stochastic Analysis of Frequency-Domain Adaptive Filters},
  author={Yang, Feiran},
  journal={EURASIP Journal on Advances in Signal Processing},
  year={2024}
}

---

## Author

This project is developed for educational and research purposes in Digital Signal Processing (DSP).
