import numpy as np
import matplotlib.pyplot as plt

means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)

n_groups = len(means_men)
index = np.arange(n_groups)
bar_width = 0.35

plt.bar(index, means_men, bar_width, color='blue', label='Men')
plt.bar(index + bar_width, means_women, bar_width, color='pink', label='Women')

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(index + bar_width / 2, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()
plt.tight_layout()
plt.show()
