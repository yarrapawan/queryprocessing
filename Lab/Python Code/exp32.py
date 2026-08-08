import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, color='blue')
plt.xlabel('X - random distribution')
plt.ylabel('Y - random distribution')
plt.title('Scatter Graph of Random Distribution')
plt.show()
