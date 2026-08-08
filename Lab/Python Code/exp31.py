import numpy as np
import matplotlib.pyplot as plt

means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)
std_men = (4, 3, 4, 1, 5)
std_women = (3, 5, 2, 3, 3)

n_groups = len(means_men)
index = np.arange(n_groups)
width = 0.35

plt.bar(index, means_men, width, yerr=std_men, color='steelblue', label='Men')
plt.bar(index, means_women, width, bottom=means_men, yerr=std_women, color='lightsalmon', label='Women')

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(index, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()
plt.tight_layout()
plt.show()
