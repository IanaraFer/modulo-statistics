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
tasks.ipynb/
	lady_tasting_tea.ipynb # Related experiment notebook (if present)
	problems.ipynb         # Main problems & extended experiment simulation
```

Currently there are no dedicated data folders because simulations are generated on the fly.

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
There is no `requirements.txt` yet. The notebooks currently use:
- `numpy`
- `scipy` (for `scipy.special.comb`)

Install them:
```powershell
pip install numpy scipy
```

If you would like, create a `requirements.txt`:
```powershell
echo numpy> requirements.txt
echo scipy>> requirements.txt
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
1. Open `tasks.ipynb/problems.ipynb`.
2. Run cells in order (restart kernel first for a clean state).
3. Each code cell handles a single logical step (imports, parameters, simulation, comparison, interpretation).

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
- Add `requirements.txt` (and optionally `pyproject.toml`).
- Provide benchmarking cell to show scaling of simulation time vs trials.
- Extend experiment to partial correctness thresholds (e.g., allow 11/12 correct) and compute cumulative probabilities.
- Include power analysis for alternative designs.

## Attribution
Original Lady Tasting Tea concept credited to Sir Ronald Fisher. Implementation and extension prepared by Ianara Fernandes.

---
Feel free to open issues or propose enhancements.


