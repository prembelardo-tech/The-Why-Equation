# The Why-Equation

**Computational simulation and empirical validation for the theoretical framework: "The Why-Equation: How Abstract Intentionality Governs Biological Systems through Top-Down Causality"**

This repository contains all code, data, and figures necessary to reproduce the computational simulations and empirical validation presented in the manuscript.

---

## 📄 Manuscript
- **Full PDF**: [`The_Why_Equation .pdf`](The_Why_Equation .pdf) (latest version)

---

## ✨ Key Features
- Recursive dynamical system modeling Will (𝑾) and Meaning (𝑴) as independent higher-order variables
- Time-series simulation of Cognitive Friction → Resonance Moment → Flow State
- Monte Carlo robustness analysis (n = 1,000)
- 80% directional concordance validation against GSE45329 (Fredrickson et al., 2013)
- Cross-validation with 2015 replication cohort
- Full reproducibility of all figures in the paper

---

## 📁 Repository Structure
The-Why-Equation/
├── The_Why_Equation.pdf                     # Full manuscript
├── Supplementary Material.pdf               # Appendix A + Supplementary Table S1 (full reproducibility protocol)
├── why_equation_main_simulation.py          # Main simulation → produces Figure 1 (Eudaimonic vs Hedonic time-series) and comparison plot figure 3
├── why_equation_sensitivity_analysis.py     # Sensitivity analysis → Figure 2
├── why_equation_cross_validation_2015.py    # Cross-validation with Fredrickson et al. 2015 figure 6
├── Why_Equation_MonteCarlo_Figure4.py       # # Monte Carlo n=100 → Figure 4
├── Why_Equation_MonteCarlo_Figure7.py       # # Monte Carlo N=1,000 → Figure 7
├── GSE45329_Validation.py                   # Empirical validation script (80% concordance) figher 5
├── GSE45329.top.table.tsv                   # Pre-processed transcriptomic data
├── figures/                                 # High-resolution figures used in the paper
├── requirements.txt                         # Python dependencies
└── LICENSE
text

---

Citation
If you use this code or the Why-Equation framework in your research, please cite the manuscript:
Prem Belardo (2026). The Why-Equation: How Abstract Intentionality Governs Biological Systems through Top-Down Causality. Manuscript submitted for publication.
GitHub repository: https://github.com/prembelardo-tech/The-Why-Equation

License
This project is licensed under the MIT License - see the LICENSE file for details.

Repository last updated: April 2026
Questions? Open an issue or contact the author.
