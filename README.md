# DSP-Project
Stochastic Analysis of Frequency-Domain Adaptive Filters (FDAF)

A comprehensive Python implementation and reproduction of the 2024 research paper:

"Stochastic Analysis of Frequency-Domain Adaptive Filters (FDAF)"
by Feiran Yang

---

Overview

This repository provides a complete implementation, analysis, and experimental reproduction of the Frequency-Domain Adaptive Filter (FDAF) family studied in the paper.

The project investigates the convergence behavior, stability conditions, and steady-state performance of several FDAF variants under both exact-modeling and under-modeling scenarios.

The implementation follows the theoretical framework presented in the paper and reproduces the main simulation results, including MSD, EMSE, MMSE, convergence curves, and stability analysis.

---

Implemented Algorithms

Constrained FDAF

- Standard FDAF
- Step-normalized FDAF

Unconstrained FDAF

- Standard FDAF
- Step-normalized FDAF

---

Features

- Time-domain implementation of FDAF algorithms
- Exact-modeling experiments
- Under-modeling experiments
- White-noise input simulations
- Correlated AR(1) input simulations
- Mean convergence analysis
- Mean-square convergence analysis
- MSD evaluation
- EMSE evaluation
- MMSE evaluation
- Stability bound verification
- Reproduction of figures presented in the original paper

---

Mathematical Metrics

The following performance measures are evaluated:

- Mean Square Deviation (MSD)
- Excess Mean Square Error (EMSE)
- Mean Square Error (MSE)
- Minimum Mean Square Error (MMSE)
- Convergence Rate
- Stability Region

---

Project Structure

FDAF-Stochastic-Analysis/
│
├── fdaf/
│   ├── constrained.py
│   ├── unconstrained.py
│   ├── normalized.py
│   └── utils.py
│
├── experiments/
│   ├── exact_modeling.py
│   ├── under_modeling.py
│   ├── stability_analysis.py
│   └── mmse_analysis.py
│
├── figures/
│
├── notebooks/
│   └── FDAF_Tutorial.ipynb
│
├── README.md
├── requirements.txt
└── LICENSE

---

Experimental Scenarios

Exact Modeling

Adaptive filter length equals the true system length.

L = M

Under Modeling

Adaptive filter length is shorter than the unknown system.

L < M

---

Reproduced Results

The repository reproduces the principal experiments reported in the paper:

- Learning curves (MSD)
- Learning curves (EMSE)
- Stability bounds
- Exact-modeling performance
- Under-modeling performance
- MMSE comparison
- Step-size sensitivity analysis

---

Installation

git clone https://github.com/your_username/FDAF-Stochastic-Analysis.git

cd FDAF-Stochastic-Analysis

pip install -r requirements.txt

---

Example Usage

from fdaf.constrained import ConstrainedFDAF

fdaf = ConstrainedFDAF(
    filter_length=16,
    block_length=16,
    step_size=0.1
)

fdaf.fit(x, d)

---

Future Work

- Comparison with LMS
- Comparison with NLMS
- Comparison with RLS
- Real-time audio echo cancellation
- GPU acceleration
- Deep-learning-assisted adaptive filtering

---

Citation

If you use this repository in academic work, please cite the original paper:

@article{yang2024fdaf,
  title={Stochastic Analysis of Frequency-Domain Adaptive Filters},
  author={Yang, Feiran},
  journal={EURASIP Journal on Advances in Signal Processing},
  year={2024}
}

---

Acknowledgments

This repository is an independent educational and research-oriented implementation based on the theoretical developments presented in the original FDAF paper.

The goal is to provide a transparent, reproducible, and extensible framework for studying frequency-domain adaptive filtering algorithms.
