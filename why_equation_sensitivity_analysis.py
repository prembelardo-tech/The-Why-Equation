import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Use the same class from the previous code. (WhyEquationSimulation)
# If you haven't run that class yet, copy the first set of code and run it first.

# --- Set up an experiment Sensitivity Analysis ---
feedback_rates = [0.10, 0.15, 0.20] # X-axis: Feedback strength [Ref: Source 182-188]
n_trials = 50 # Number of trial laps per point (to obtain Error Bars)

eudaimonic_means = []
eudaimonic_stds = []
hedonic_means = []
hedonic_stds = []

sim = WhyEquationSimulation()

# 1. run Loop collect data
for rate in feedback_rates:
    # collect Eudaimonic data (M=0.7)
    eu_outcomes = []
    for _ in range(n_trials):
        _, _, _, P = sim.run_scenario(initial_m=0.7, feedback_rate=rate, decay_rate=0.005)
        eu_outcomes.append(np.mean(P[80:])) # Take the average at the end
    eudaimonic_means.append(np.mean(eu_outcomes))
    eudaimonic_stds.append(np.std(eu_outcomes))
    
    # collect Hedonic data (M=0.3)
    he_outcomes = []
    for _ in range(n_trials):
        _, _, _, P = sim.run_scenario(initial_m=0.3, feedback_rate=rate, decay_rate=0.02)
        he_outcomes.append(np.mean(P[80:]))
    hedonic_means.append(np.mean(he_outcomes))
    hedonic_stds.append(np.std(he_outcomes))

# 2. Calculate Linear Regression (dashed line) [Ref: Source 181]
slope_eu, intercept_eu, _, _, _ = stats.linregress(feedback_rates, eudaimonic_means)
slope_he, intercept_he, _, _, _ = stats.linregress(feedback_rates, hedonic_means)

# create line Fit Line
x_fit = np.linspace(0.09, 0.21, 100)
y_fit_eu = slope_eu * x_fit + intercept_eu
y_fit_he = slope_he * x_fit + intercept_he

# --- Plotting Figure 2 ---
plt.figure(figsize=(10, 6))

# Plot Eudaimonic (BLUE)
plt.errorbar(feedback_rates, eudaimonic_means, yerr=eudaimonic_stds, fmt='o', 
             color='blue', ecolor='blue', capsize=5, label='Eudaimonic Data')
plt.plot(x_fit, y_fit_eu, '--', color='navy', label=f'Eudaimonic Fit (Slope={slope_eu:.2f})')

# Plot Hedonic (RED)
plt.errorbar(feedback_rates, hedonic_means, yerr=hedonic_stds, fmt='o', 
             color='red', ecolor='red', capsize=5, label='Hedonic Data')
plt.plot(x_fit, y_fit_he, '--', color='darkred', label=f'Hedonic Fit (Slope={slope_he:.2f})')

# Decorate graphs
plt.title('Figure 2: Sensitivity Analysis (Effect of Feedback on Physiological Change)')
plt.xlabel('Feedback Rate (Strength of Biological Response Loop)')
plt.ylabel('Mean Average ΔP (Physiological Output)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0.09, 0.21)

plt.tight_layout()
plt.show()
