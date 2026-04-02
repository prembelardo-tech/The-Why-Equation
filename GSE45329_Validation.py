import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the Dataset
# Ensure the .tsv file is in the same directory as this script
file_path = r'/content/GSE45329.top.table (2).tsv'
try:
    df = pd.read_csv(file_path, sep='\t')
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure it is in the correct directory.")
    exit()

# 2. Define CTRA Gene Set Targets (Based on Fredrickson et al., 2013)
# Pro-inflammatory genes (Expected to increase under Low Meaning/High Stress)
pro_genes = ['IL6', 'PTGS2', 'IL1B', 'IL1A', 'NFKB2', 'NFKB1', 'TNF', 'REL', 'JUN', 'RELB']
# Antiviral/Antibody genes (Expected to be stable or decrease)
anti_genes = ['OAS1', 'OAS2', 'OAS3', 'MX1', 'MX2', 'IFIT1', 'IFIT2', 'IFIT3', 'IFI35', 'STAT1']

# 3. Analyze Directional Concordance
def analyze_concordance(gene_list, expected_up=True):
    temp_df = df[df['ID'].isin(gene_list)].copy()
    if expected_up:
        # Success if logFC is positive
        temp_df['match'] = temp_df['logFC'] > 0
    else:
        # Success if logFC is zero or negative
        temp_df['match'] = temp_df['logFC'] <= 0
    return temp_df

pro_results = analyze_concordance(pro_genes, expected_up=True)
anti_results = analyze_concordance(anti_genes, expected_up=False)

# 4. Statistical Summary Output
print(f"--- Why-Equation: Empirical Validation Summary ---")
print(f"Pro-inflammatory Concordance: {pro_results['match'].mean()*100:.2f}%")
print(f"Antiviral/Antibody Concordance: {anti_results['match'].mean()*100:.2f}%")
print(f"Overall Systematic Accuracy: {(pd.concat([pro_results, anti_results])['match'].mean()*100):.2f}%")

# 5. Generate Validation Visualization (Figure 5)
plt.figure(figsize=(12, 6))
plot_data = pd.concat([
    pro_results.assign(Group='Pro-inflammatory (Entropy)'),
    anti_results.assign(Group='Antiviral (Stability)')
])

# Professional Color Scheme: Red for Entropy/Inflammation, Blue for Coherence/Antiviral
colors = ['#ff4d4d' if g == 'Pro-inflammatory (Entropy)' else '#4d79ff' for g in plot_data['Group']]

plt.bar(plot_data['ID'], plot_data['logFC'], color=colors, alpha=0.8, edgecolor='black')
plt.axhline(0, color='black', linewidth=1)

plt.title('Directional Validation of the Why-Equation (Dataset: GSE45329)', fontsize=14)
plt.ylabel('Log2 Fold Change (logFC)', fontsize=12)
plt.xlabel('Gene Symbol', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Add Legend
import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='#ff4d4d', label='Pro-inflammatory (Expected UP)')
blue_patch = mpatches.Patch(color='#4d79ff', label='Antiviral (Expected DOWN/Stable)')
plt.legend(handles=[red_patch, blue_patch])

plt.tight_layout()

# Save the figure for the manuscript
plt.savefig('Why_Equation_Validation_Figure.png', dpi=300)
print("Validation figure saved as 'Why_Equation_Validation_Figure.png'")
plt.show()