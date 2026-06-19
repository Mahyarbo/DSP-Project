# DSP-Project
FDAF: Stochastic Analysis of Frequency-Domain Adaptive Filters

A Python implementation and experimental reproduction of the FDAF algorithms analyzed in the paper:

Feiran Yang, "Stochastic Analysis of Frequency-Domain Adaptive Filters", EURASIP Journal on Advances in Signal Processing, 2024.

---

Overview

This repository provides a clean and educational implementation of Frequency-Domain Adaptive Filters (FDAFs), together with simulations that reproduce the theoretical results presented in the original paper.

The project focuses on:

- Constrained FDAF
- Unconstrained FDAF
- Step-Normalized FDAF
- Exact Modeling Analysis
- Under-Modeling Analysis
- MSD Evaluation
- EMSE Evaluation
- MMSE Evaluation
- Stability Analysis

---

Implemented Algorithms

Algorithm| Implemented
Constrained FDAF| ✓
Constrained FDAF with Step-Normalization| ✓
Unconstrained FDAF| ✓
Unconstrained FDAF with Step-Normalization| ✓

---

Reproduced Experiments

The repository reproduces and verifies several theoretical results reported in the paper, including:

- Learning Curves (MSD)
- Learning Curves (EMSE)
- Stability Bounds
- Exact Modeling Performance
- Under-Modeling Performance
- MMSE Comparison
- Step-Size Sensitivity Analysis

---

Project Structure

FDAF-Stochastic-Analysis/
│
├── fdaf/
├── experiments/
├── notebooks/
├── figures/
├── README.md
├── requirements.txt
└── LICENSE

---

Installation

git clone https://github.com/your-username/FDAF-Stochastic-Analysis.git

cd FDAF-Stochastic-Analysis

pip install -r requirements.txt

---

Research Purpose

This repository was developed for educational and research purposes to improve understanding of frequency-domain adaptive filtering and stochastic convergence analysis.

---

Disclaimer

This repository is an independent implementation written from scratch based on the methodology described in the referenced publication.

No original source code, figures, tables, or copyrighted material from the paper are included in this repository.

---

Citation

If this repository contributes to your research, please cite the original paper:

@article{yang2024fdaf,
  title={Stochastic Analysis of Frequency-Domain Adaptive Filters},
  author={Yang, Feiran},
  journal={EURASIP Journal on Advances in Signal Processing},
  year={2024}
}

---

Author

Developed as a research and educational project in Digital Signal Processing (DSP).
