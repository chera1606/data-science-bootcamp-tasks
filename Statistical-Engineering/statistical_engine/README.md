# Statistical Engine & Monte Carlo Simulation

## Project Overview

This project builds a pure Python statistical engine (`StatEngine`) that calculates mean, median, mode, variance, standard deviation, and detects outliers. It also runs Monte Carlo simulations to demonstrate the Law of Large Numbers (LLN) using a server crash scenario.

## Mathematical Logic

- **Mean:** Sum of data divided by number of points.
- **Median:** Middle value for odd-length lists; average of two middle values for even-length lists.
- **Mode:** Most frequent value(s); handles multimodal or all-unique cases.
- **Variance:**
  - Population: average squared deviation from the mean.
  - Sample: same as population but divided by (n-1) (Bessel’s correction).
- **Standard Deviation:** Square root of variance.
- **Outliers:** Points > threshold × standard deviation from the mean.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd statistical_engine
   ```
