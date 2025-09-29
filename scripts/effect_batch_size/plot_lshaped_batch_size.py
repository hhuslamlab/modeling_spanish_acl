
import matplotlib.pyplot as plt
import seaborn as sns
import tikzplotlib

plt.style.use('seaborn')
sns.set_palette("deep")

model_types = ["32", "64", "128", "256", "400", "512", "800", "3600"]
l_shaped_accuracy_10L_90NL = [61.88, 61.61, 64.71, 46.27, 36.75, 34.86, 34.17, 46.74]
l_shaped_accuracy_50L_50NL = [87.42, 86.16, 84.94, 81.14, 72.31, 75.73, 82.67, 80.35]
l_shaped_accuracy_90L_10NL = [88.62, 89.24, 87.18, 87.61, 88.75, 87.7, 88.43, 86.13]

plt.figure(figsize=(12, 7))

plt.plot(model_types, l_shaped_accuracy_10L_90NL, marker='o', linewidth=2, markersize=8, label='10%L-90%NL')
plt.plot(model_types, l_shaped_accuracy_50L_50NL, marker='s', linewidth=2, markersize=8, label='50%L-50%NL')
plt.plot(model_types, l_shaped_accuracy_90L_10NL, marker='^', linewidth=2, markersize=8, label='90%L-10%NL')

plt.xlabel('Batch Size', fontsize=14, labelpad=10)
plt.ylabel('L-shaped Accuracy (%)', fontsize=14, labelpad=10)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)

plt.ylim(30, 100)

plt.grid(True, linestyle='--', alpha=0.7)

plt.legend(title='Conditions', title_fontsize='13', fontsize='12', loc='lower right', frameon=True)

plt.tight_layout()
tikzplotlib.save("../data/analysis/plots/l_shaped_accuracy_by_batch_sizes.tex")
