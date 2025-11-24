"""Command-line simulation for Lady Tasting Tea experiments.

Usage (PowerShell):
    python run_simulation.py --trials 200000 --extended 12 8 --original 8 4 --seed 42

If arguments are omitted, defaults are used.
"""
from __future__ import annotations
import argparse
import math
from typing import Tuple
import numpy as np
from scipy.special import comb


def simulate_exact_match(n_cups: int, n_tea: int, trials: int, seed: int) -> Tuple[int, float]:
    rng = np.random.default_rng(seed)
    target = set(range(n_tea))
    hits = 0
    for _ in range(trials):
        guess = set(rng.choice(n_cups, n_tea, replace=False))
        if guess == target:
            hits += 1
    return hits, hits / trials


def theoretical_probability(n_cups: int, n_tea: int) -> float:
    return 1 / comb(n_cups, n_tea)


def format_prob(p: float) -> str:
    return f"{p:.6f} ({p*100:.4f}%)"


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate Lady Tasting Tea experiments.")
    parser.add_argument("--trials", type=int, default=200_000, help="Number of Monte Carlo trials (default 200000)")
    parser.add_argument("--extended", nargs=2, type=int, metavar=("N_CUPS", "N_TEA"), default=[12, 8], help="Extended experiment specs: total cups and tea-first cups")
    parser.add_argument("--original", nargs=2, type=int, metavar=("N_CUPS", "N_TEA"), default=[8, 4], help="Original experiment specs: total cups and tea-first cups")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    ext_cups, ext_tea = args.extended
    orig_cups, orig_tea = args.original

    print("=" * 60)
    print("LADY TASTING TEA SIMULATION")
    print("=" * 60)
    print(f"Trials: {args.trials:,}")
    print(f"Seed: {args.seed}")

    # Extended
    hits_ext, sim_ext = simulate_exact_match(ext_cups, ext_tea, args.trials, args.seed)
    theo_ext = theoretical_probability(ext_cups, ext_tea)

    # Original
    hits_orig, sim_orig = simulate_exact_match(orig_cups, orig_tea, args.trials, args.seed + 1)
    theo_orig = theoretical_probability(orig_cups, orig_tea)

    ratio = theo_ext / theo_orig

    print("\nExtended Experiment:")
    print(f"  Config: {ext_cups} cups ({ext_tea} tea-first, {ext_cups - ext_tea} milk-first)")
    print(f"  Perfect matches: {hits_ext:,}")
    print(f"  Simulated probability:  {format_prob(sim_ext)}")
    print(f"  Theoretical probability: {format_prob(theo_ext)}")

    print("\nOriginal Experiment:")
    print(f"  Config: {orig_cups} cups ({orig_tea} tea-first, {orig_cups - orig_tea} milk-first)")
    print(f"  Perfect matches: {hits_orig:,}")
    print(f"  Simulated probability:  {format_prob(sim_orig)}")
    print(f"  Theoretical probability: {format_prob(theo_orig)}")

    print("\nStringency:")
    print(f"  Chance extended / original: {ratio:.2f}x")
    print(f"  Success by chance is {1/ratio:.2f}x smaller in extended.")

    print("\nNotes:")
    print("  - Increase --trials for a closer match to theoretical values.")
    print("  - Adjust cup counts to explore alternative designs.")
    print("  - Using unbiased logic (ddof not relevant here; exact-match criterion).")


if __name__ == "__main__":
    main()
