import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt(r"D:\Query Processing\DSA05_Lab\data_files\test.txt", delimiter=' ', unpack=True)

plt.plot(x, y, marker='o', color='green')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line graph from test.txt')
plt.show()
