import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]
y3 = [5, 4, 3, 2, 1]
y4 = [2, 4, 6, 8, 10]

fig, axs = plt.subplots(2, 2, figsize=(8, 6))

axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title('Plot 1')

axs[0, 1].plot(x, y2, color='red')
axs[0, 1].set_title('Plot 2')

axs[1, 0].plot(x, y3, color='green')
axs[1, 0].set_title('Plot 3')

axs[1, 1].plot(x, y4, color='purple')
axs[1, 1].set_title('Plot 4')

plt.tight_layout()
plt.show()
