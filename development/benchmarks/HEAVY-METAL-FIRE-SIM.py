"""Reproducible Monte Carlo diagnostic for Savage StarCraft draft infantry combat.

Not an approved equipment profile or an actual session playtest.
Requires numpy. Outputs per-action pre-Soak Heavy Metal probabilities.
"""
import numpy as np

N = 300000
rng = np.random.default_rng(20261010)

def ace(n, sides):
    arr = rng.integers(1, sides + 1, n, dtype=np.int32)
    mask = arr == sides
    while np.any(mask):
        values = rng.integers(1, sides + 1, int(mask.sum()))
        arr[mask] += values
        original = mask.copy()
        mask[original] = values == sides
    return arr

def sim(label, shooting=6, rof=3, wild=True, penalty=0, bonus=0):
    attacks = np.stack([ace(N, shooting) for _ in range(rof)], axis=1)
    if wild:
        wild_die = ace(N, 6)
        low_idx = np.argmin(attacks, axis=1)
        replace = wild_die > attacks[np.arange(N), low_idx]
        attacks[np.arange(N)[replace], low_idx[replace]] = wild_die[replace]
    results = attacks - penalty + bonus
    hits = results >= 4
    raises = results >= 8
    wound_i = (hits * rng.integers(1, 4, (N, rof))).sum(axis=1) + raises.sum(axis=1)
    wound_ii = raises.sum(axis=1)
    return (f"{label}: hit={100*(wound_i>0).mean():.1f}%, "
            f"avg_hits={hits.sum(axis=1).mean():.2f}, "
            f"avg_WI={wound_i.mean():.2f}, P(WI>=4)={100*(wound_i>=4).mean():.1f}%, "
            f"P(WII>=1)={100*(wound_ii>=1).mean():.1f}%")

if __name__ == "__main__":
    cases = [
        ("Extra d6 RoF3 recoil open", 6, 3, False, 2, 0),
        ("Extra d6 RoF3 recoil cover", 6, 3, False, 4, 0),
        ("Wild d6 RoF3 recoil open", 6, 3, True, 2, 0),
        ("Wild d6 RoF3 recoil cover", 6, 3, True, 4, 0),
        ("Wild d6 RoF3 stabilized open", 6, 3, True, 0, 0),
        ("Wild d6 RoF3 stabilized cover", 6, 3, True, 2, 0),
        ("Wild d8 RoF3 recoil cover", 8, 3, True, 4, 0),
        ("Wild d6 RoF1 plain open", 6, 1, True, 0, 0),
        ("Wild d6 RoF1 plain cover", 6, 1, True, 2, 0),
        ("Wild d6 RoF1 3RB open", 6, 1, True, 0, 1),
        ("Wild d6 RoF1 3RB cover", 6, 1, True, 2, 1),
    ]
    for case in cases:
        print(sim(*case))
