import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set_palette("deep")

model_types = ["32", "64", "128", "256", "400", "512", "800", "1600", "2400"]
nl_shaped_accuracy_10L_90NL = [73.29, 75.31, 70.87, 67.97, 61.8, 53.37, 39.83, 38.36]
nl_shaped_accuracy_50L_50NL = [65.37, 65.45, 60.02, 56.17, 55.19, 54.75, 62.36, 61.46]
nl_shaped_accuracy_90L_10NL = [26.83, 26.54, 22.59, 20.06, 24.17, 22.6, 21.99, 21.03]

# Create the plot
plt.figure(figsize=(12, 7))

plt.plot(model_types, nl_shaped_accuracy_10L_90NL, marker='o', linewidth=2, markersize=8, label='10%L-90%NL')
plt.plot(model_types, nl_shaped_accuracy_50L_50NL, marker='s', linewidth=2, markersize=8, label='50%L-50%NL')
plt.plot(model_types, nl_shaped_accuracy_90L_10NL, marker='^', linewidth=2, markersize=8, label='90%L-10%NL')

# Customize the plot
plt.xlabel('Batch Size', fontsize=14, labelpad=10)
plt.ylabel('NL-shaped Accuracy (%)', fontsize=14, labelpad=10)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)

# Add a grid
plt.grid(True, linestyle='--', alpha=0.7)

# Customize the legend
plt.legend(title='Conditions', title_fontsize='13', fontsize='12', loc='upper right', frameon=True)

# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig('../data/analysis/plots/nl_shaped_accuracy_by_batch_sizes.png', dpi=300, bbox_inches='tight')
