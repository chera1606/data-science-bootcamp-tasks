# src/monte_carlo.py

import random

def simulate_crashes(days: int, crash_prob: float = 0.045) -> float:
    """
    Simulate server crashes over a number of days.
    Returns the simulated probability of a crash.
    """
    crashes = 0
    for _ in range(days):
        if random.random() < crash_prob:
            crashes += 1
    return crashes / days


if __name__ == "__main__":
    # Example runs
    for days in [30, 100, 10000]:
        sim_prob = simulate_crashes(days)
        print(f"Simulated probability over {days} days: {sim_prob:.4f}")