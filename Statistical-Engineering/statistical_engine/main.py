# main.py

import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

# Load mock salary data
with open("data/sample_salaries.json") as f:
    salaries = json.load(f)

# Initialize StatEngine
engine = StatEngine(salaries)

print("=== Salary Statistics ===")
print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance (sample):", engine.get_variance())
print("Standard Deviation (sample):", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

# Monte Carlo simulation
print("\n=== Monte Carlo Server Simulation ===")
for days in [30, 100, 10000]:
    sim_prob = simulate_crashes(days)
    print(f"Simulated probability over {days} days: {sim_prob:.4f}")