import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ==============================================================================
# The Why-Equation: Monte Carlo Robustness Analysis
# Purpose: To test the structural resilience of the model against biological noise.
# ==============================================================================

# 1. Simulation Parameters
num_simulations = 1000  # Number of iterations to test robustness
time_steps = 50         # Temporal progression
natural_entropy_rate = 0.05 # Baseline tendency for biological systems to degrade

# 2. The Core Recursive Function
def simulate_why_equation(M_level, noise_level=0.1):
    """
    Simulates the recursive dynamics of Biological Entropy (E) governed by Meaning (M).
    Formula conceptualization: E(t+1) = E(t) - W(Veto) + Noise + Natural_Decay
    """
    E_history = []
    E = 1.0  # Initial state of systemic entropy
    
    for t in range(time_steps):
        # Introduce Gaussian noise to simulate biological/environmental variance
        stochastic_noise = np.random.normal(0, noise_level)
        
        # Will (W) acts as a selective inhibitor, scaled by the magnitude of Meaning (M)
        W_veto = M_level * 0.15 
        
        # Recursive update of Systemic Entropy (E)
        E = E - W_veto + stochastic_noise + natural_entropy_rate
        
        # Constrain E to realistic biological limits (cannot be infinitely negative)
        E = max(0.1, E) 
        E_history.append(E)
        
    return E_history

# 3. Execute Monte Carlo Simulations
plt.figure(figsize=(10, 6))

# Condition A: Eudaimonic State (High Meaning)
# Hypothesis: High M dampens entropy and maintains systemic coherence despite noise.
for _ in range(num_simulations):
    res_high_M = simulate_why_equation(M_level=0.8, noise_level=0.08)
    plt.plot(res_high_M, color='#4d79ff', alpha=0.03) # Blue with high transparency

# Condition B: Hedonic/Stress State (Low Meaning)
# Hypothesis: Low M fails to inhibit entropy, leading to systemic decoherence.
for _ in range(num_simulations):
    res_low_M = simulate_why_equation(M_level=0.2, noise_level=0.08)
    plt.plot(res_low_M, color='#ff4d4d', alpha=0.03) # Red with high transparency

# 4. Visualization Formatting
plt.title('Monte Carlo Robustness Analysis of The Why-Equation (N=1000 Simulations)', fontsize=14, fontweight='bold')
plt.ylabel('Systemic Biological Entropy (E)', fontsize=12)
plt.xlabel('Time Steps (t)', fontsize=12)

# Custom Legend
red_patch = mpatches.Patch(color='#ff4d4d', label='Low Meaning (Hedonic/Stress Trajectory)')
blue_patch = mpatches.Patch(color='#4d79ff', label='High Meaning (Eudaimonic/Coherence Trajectory)')
plt.legend(handles=[red_patch, blue_patch], loc='upper left')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Save the output figure
plt.savefig('Figure_MonteCarlo_Robustness.png', dpi=300)
print("Monte Carlo Simulation completed. Figure saved as 'Figure_MonteCarlo_Robustness.png'")
plt.show()
