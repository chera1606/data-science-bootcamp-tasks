# Statistical Engine & Monte Carlo Simulation

## Project Overview
This project implements a **pure Python statistical engine** to analyze 1D numerical data.  
It calculates **central tendency** (mean, median, mode), **dispersion** (variance, standard deviation), and **detects outliers**.  

Additionally, it includes a **Monte Carlo simulation** to model server crash probabilities, demonstrating the **Law of Large Numbers (LLN)** in practice.

---

## Mathematical Logic

### Variance
Variance measures how spread out the data is.  

- **Population variance:**  
\[
\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}
\]  

- **Sample variance (Bessel's correction):**  
\[
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}
\]  

The implementation allows switching between **sample** and **population** using the parameter `is_sample=True`.

### Standard Deviation
- Calculated as the **square root of the variance**.  
- Reflects the average deviation from the mean.

### Median
- **Odd number of elements:** select the middle value.  
- **Even number of elements:** average the two middle values.

### Mode
- Returns all modes if multiple values have the same highest frequency.  
- If all values are unique, returns: `"All values are unique, no mode."`

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/username/statistical_engine.git
cd statistical_engine
