# Modulo Statistics

Assessment materials for a statistics module, including reproducible simulation notebooks (e.g. Lady Tasting Tea extension) and problem explorations.

Repository: https://github.com/IanaraFer/modulo-statistics/

## Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Notebooks](#running-the-notebooks)
- [Reproducing the Lady Tasting Tea Simulations](#reproducing-the-lady-tasting-tea-simulations)
- [Data & Assets](#data--assets)
- [Large Files Policy](#large-files-policy)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

## Project Overview
This repository is an educational exploration of classical hypothesis testing using a historically significant experiment. It focuses on how experimental design choices (number of trials / class balance) affect the probability of success by chance and therefore the stringency of a test.

The core statistical example extends Fisher's "Lady Tasting Tea" experiment from 8 cups (4 tea-first, 4 milk-first) to 12 cups (8 tea-first, 4 milk-first) to illustrate:
1. How combinatorial counts ("choose" functions) drive exact p-values.
2. When Monte Carlo simulation is appropriate for validating analytic results.
3. How increasing imbalance or total sample size tightens chance probabilities.
4. Practical interpretation of very small p-values in an experimental context.

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

Then open `tasks.ipynb/problems.ipynb` and run cells top to bottom.

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
tasks.ipynb/
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

1. Open any notebook in `tasks.ipynb/` (e.g., `problem2.ipynb`, `problem3.ipynb`, `problem4.ipynb`, or `problems.ipynb`)
2. Run cells in order (restart kernel first for a clean state)
3. Each code cell handles a single logical step (imports, parameters, simulation, visualization, interpretation)

**Available Notebooks:**
- **problem2.ipynb**: Normal Distribution and Sample Standard Deviation (ddof=0 vs ddof=1)
- **problem3.ipynb**: t-Tests and Type II Error Analysis with power curves
- **problem4.ipynb**: ANOVA vs Multiple t-Tests and the multiple comparisons problem
- **problems.ipynb**: Lady Tasting Tea experiment simulation

If any cell errors due to missing packages, verify the environment activation and reinstall dependencies.

## Reproducing the Lady Tasting Tea Simulations
Key parameters (defined early in `problems.ipynb`):
- `n_cups_extended = 12`, `n_tea_first_extended = 8`, `n_milk_first_extended = 4`
- `n_cups_original = 8`, `n_tea_first_original = 4`, `n_milk_first_original = 4`
- `n_simulations = 1_000_000` (Monte Carlo trials)

The helper function `simulate_exact_match` encapsulates the random guessing logic.

To adjust computational cost, reduce `n_simulations` (e.g. 100_000) for faster iteration, then scale up for final results.

## Data & Assets
No external datasets or images are required; all results are generated programmatically. If future problems require datasets:
- Store small CSV/JSON files under a new `data/` directory.
- For large public datasets, provide scripted download (see template below).

### Example Download Snippet (Template)
```python
import urllib.request, pathlib
DATA_DIR = pathlib.Path("data")
DATA_DIR.mkdir(exist_ok=True)
url = "https://example.com/large_dataset.csv"  # Replace
dest = DATA_DIR / "large_dataset.csv"
if not dest.exists():
		print("Downloading large dataset...")
		urllib.request.urlretrieve(url, dest)
		print("Download complete.")
else:
		print("Dataset already present.")
```

## Large Files Policy
If any file exceeds repository size best practices (>50MB):
- Do NOT commit directly.
- Provide an automated download script instead (as above).
- Optionally use Git LFS if truly necessary (document commands).

## Troubleshooting
- "ModuleNotFoundError": Ensure virtual environment activated and run `pip install numpy scipy`.
- Performance slow: Lower `n_simulations` for exploratory runs.
- Random results vary: Set `seed` in helper function or reuse provided seeds (42, 123).

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


