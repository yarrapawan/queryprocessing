import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

weight1, height1 = 60 + 5 * np.random.randn(20), 160 + 8 * np.random.randn(20)
weight2, height2 = 75 + 6 * np.random.randn(20), 170 + 7 * np.random.randn(20)
weight3, height3 = 90 + 7 * np.random.randn(20), 180 + 6 * np.random.randn(20)

plt.scatter(weight1, height1, color='red', label='Group 1')
plt.scatter(weight2, height2, color='green', label='Group 2')
plt.scatter(weight3, height3, color='blue', label='Group 3')

plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Scatter Plot of Weights and Heights for Three Groups')
plt.legend()
plt.show()
