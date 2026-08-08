import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.xlabel('X - random distribution')
plt.ylabel('Y - random distribution')
plt.title('Scatter Plot with Balls of Different Sizes')
plt.show()
