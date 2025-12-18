# Modulo Statistics

A collection of statistical simulations and analyses exploring fundamental concepts in hypothesis testing, experimental design, and statistical inference through reproducible Jupyter notebooks.

Repository: https://github.com/IanaraFer/modulo-statistics/

## Purpose

This repository serves as an educational resource for understanding key statistical concepts through computational simulation and visualization. It contains four main problem sets that demonstrate:

1. **Fisher's Lady Tasting Tea Experiment** - Classic experimental design and exact probability calculations
2. **Normal Distribution and Standard Deviation** - Understanding bias in variance estimators (ddof parameter)
3. **Type II Error and Statistical Power** - How effect size impacts the ability to detect true differences
4. **ANOVA vs Multiple Comparisons** - Why multiple t-tests inflate error rates and when to use ANOVA

Each problem is implemented as a self-contained Jupyter notebook with:
- Clear explanations of the statistical concepts
- Python code using NumPy, SciPy, and Matplotlib
- Visualizations to illustrate key findings
- Interpretations connecting theory to practice

The code is designed to be reproducible, educational, and easily modifiable for exploring different parameters or scenarios.

## Table of Contents

- [Purpose](#purpose)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Notebooks](#running-the-notebooks)
- [How to Use This Repository](#how-to-use-this-repository)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## Quick Start
```powershell
# Clone
git clone https://github.com/IanaraFer/modulo-statistics.git
cd modulo-statistics

# Create & activate environment
python -m venv .venv
./.venv/Scripts/Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Launch notebooks
jupyter notebook  # or open in VS Code
```

Then open `problems.ipynb/problems.ipynb` and run cells top to bottom.

## Run Simulation From Command Line (Optional)
Use the provided `run_simulation.py` script for a fast, non-notebook reproduction:
```powershell
python run_simulation.py --trials 300000 --extended 12 8 --original 8 4 --seed 42
```
Arguments:
- `--trials`: Monte Carlo iterations (increase for accuracy)
- `--extended CUPS TEA` and `--original CUPS TEA`: configure designs
- `--seed`: reproducible randomness

Example alternative design (10 cups: 5 tea-first, 5 milk-first):
```powershell
python run_simulation.py --extended 10 5 --original 8 4 --trials 500000
```

## Repository Structure
```
README.md                # This file
requirements.txt         # Python dependencies
run_simulation.py        # Command-line simulation script
problems.ipynb/
   problem2.ipynb       # Normal Distribution and Sample Standard Deviation
   problem3.ipynb       # t-Tests and Type II Error Analysis
   problem4.ipynb       # ANOVA vs Multiple t-Tests
   problems.ipynb       # Lady Tasting Tea experiment simulation
```

All simulations are generated on the fly using reproducible random seeds.

## Setup Instructions
### 1. Python Version
Use Python 3.10+ (3.11 recommended). Earlier versions should work but are untested here.

### 2. Create a Virtual Environment (Recommended)
PowerShell (Windows):
```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
```

### 3. Install Dependencies

The project requires:
- `numpy`
- `scipy`
- `matplotlib`

Install them:
```powershell
pip install -r requirements.txt
```

### 4. Launch Jupyter / VS Code
If using VS Code, open the workspace and select the Python interpreter from the virtual environment. Then open the notebook files directly.

Alternative (classic Jupyter):
```powershell
pip install jupyter
jupyter notebook
```

## Running the Notebooks

1. Open any notebook in `problems.ipynb/` (e.g., `problem2.ipynb`, `problem3.ipynb`, `problem4.ipynb`, or `problems.ipynb`)
2. Run cells in order (restart kernel first for a clean state)
3. Each code cell handles a single logical step (imports, parameters, simulation, visualization, interpretation)

**Available Notebooks:**
- **problem2.ipynb**: Normal Distribution and Sample Standard Deviation (ddof=0 vs ddof=1)
- **problem3.ipynb**: t-Tests and Type II Error Analysis with power curves
- **problem4.ipynb**: ANOVA vs Multiple t-Tests and the multiple comparisons problem
- **problems.ipynb**: Lady Tasting Tea experiment simulation

If any cell errors due to missing packages, verify the environment activation and reinstall dependencies.

## How to Use This Repository

### For Learning Statistical Concepts

Each notebook is self-contained and can be studied independently:

- **Start with problem2.ipynb** if you want to understand sampling distributions and bias in estimators
- **Move to problem3.ipynb** to learn about statistical power and Type II errors
- **Study problem4.ipynb** to understand ANOVA and the multiple comparisons problem
- **Explore problems.ipynb** for Fisher's classic experimental design example

### For Running Simulations

All simulations use reproducible random seeds (typically 2025 or 42), so you should get identical results when running the same code. To explore different scenarios:

1. **Modify parameters** at the top of each notebook (clearly marked in parameter cells)
2. **Change sample sizes** to see how results scale with larger datasets
3. **Adjust significance levels** (α) to understand their impact on conclusions
4. **Increase simulation trials** for more precise Monte Carlo estimates

### For Extending the Analysis

The code is designed to be modular and easy to modify:

- All helper functions are documented with docstrings
- Visualization code is separated from computation
- Random number generators use seeds for reproducibility
- Parameters are centralized at the beginning of notebooks

Feel free to fork the repository and adapt the code for your own statistical experiments!

## Reproducing the Lady Tasting Tea Simulations
Key parameters (defined early in `problems.ipynb`):
- `n_cups_extended = 12`, `n_tea_first_extended = 8`, `n_milk_first_extended = 4`
- `n_cups_original = 8`, `n_tea_first_original = 4`, `n_milk_first_original = 4`
- `n_simulations = 1_000_000` (Monte Carlo trials)

The helper function `simulate_exact_match` encapsulates the random guessing logic.

To adjust computational cost, reduce `n_simulations` (e.g. 100_000) for faster iteration, then scale up for final results.

## Troubleshooting

**"ModuleNotFoundError" or Import Errors:**
- Ensure your virtual environment is activated
- Run `pip install -r requirements.txt` to install all dependencies
- Verify you're using Python 3.10 or higher

**Notebook Kernel Issues:**
- In VS Code: Select the Python interpreter from your `.venv` folder using the kernel picker
- In Jupyter: Ensure you've installed jupyter in the virtual environment

**Slow Performance:**
- Reduce `n_simulations` or `N_SAMPLES` parameters for faster exploratory runs
- Increase them back for final, publication-quality results

**Random Results Vary:**
- All notebooks use fixed seeds (2025, 42, or 123) for reproducibility
- If you modify code, ensure you're not accidentally removing seed parameters
- For truly random results, set `seed=None` or remove the seed parameter

**Visualization Not Showing:**
- Ensure matplotlib is installed: `pip install matplotlib`
- In VS Code, plots should appear inline automatically
- In Jupyter, you may need `%matplotlib inline` magic command

## Future Improvements

- Extend experiments to partial correctness thresholds (e.g., allow 11/12 correct) and compute cumulative probabilities
- Include power analysis for alternative experimental designs
- Add benchmarking cells to show scaling of simulation time vs trials
- Explore Bayesian approaches to hypothesis testing
- Add additional statistical problems exploring different distributions and tests

## Attribution

Original Lady Tasting Tea concept credited to Sir Ronald Fisher. Implementation and extension prepared by Ianara Fernandes.

## References

### Statistical Theory and Methods

1. **Fisher, R. A. (1935).** *The Design of Experiments*. Edinburgh: Oliver and Boyd.
   - Original description of the Lady Tasting Tea experiment and randomization in experimental design

2. **Casella, G., & Berger, R. L. (2002).** *Statistical Inference* (2nd ed.). Pacific Grove, CA: Duxbury Press.
   - Comprehensive coverage of sampling distributions, hypothesis testing, and ANOVA

3. **Montgomery, D. C. (2017).** *Design and Analysis of Experiments* (9th ed.). Wiley.
   - Modern treatment of experimental design, ANOVA, and multiple comparisons

4. **Cohen, J. (1988).** *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Routledge.
   - Foundational work on statistical power, effect sizes, and Type II error

### Hypothesis Testing and Multiple Comparisons

5. **Neyman, J., & Pearson, E. S. (1933).** On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society A*, 231, 289-337.
   - Development of the Neyman-Pearson framework for hypothesis testing

6. **Benjamini, Y., & Hochberg, Y. (1995).** Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B*, 57(1), 289-300.
   - Modern approach to multiple comparison corrections

7. **Tukey, J. W. (1949).** Comparing individual means in the analysis of variance. *Biometrics*, 5(2), 99-114.
   - Introduction of Tukey's Honest Significant Difference (HSD) test for post-hoc comparisons

### Computational Statistics

8. **Robert, C. P., & Casella, G. (2004).** *Monte Carlo Statistical Methods* (2nd ed.). Springer.
   - Comprehensive treatment of Monte Carlo simulation methods

9. **Efron, B., & Tibshirani, R. J. (1993).** *An Introduction to the Bootstrap*. Chapman and Hall/CRC.
   - Resampling methods for statistical inference

### Software Documentation

10. **Harris, C. R., et al. (2020).** Array programming with NumPy. *Nature*, 585, 357-362.
    - NumPy library used for numerical computations

11. **Virtanen, P., et al. (2020).** SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods*, 17, 261-272.
    - SciPy library used for statistical functions (t-tests, ANOVA, distributions)

12. **Hunter, J. D. (2007).** Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90-95.
    - Matplotlib library used for data visualization

### Online Resources

13. **NIST/SEMATECH e-Handbook of Statistical Methods.** Available at: https://www.itl.nist.gov/div898/handbook/
    - Comprehensive online reference for statistical methods and experimental design

14. **Penn State STAT 500: Applied Statistics.** Available at: https://online.stat.psu.edu/stat500/
    - Educational materials on ANOVA, experimental design, and hypothesis testing

---
Feel free to open issues or propose enhancements.


