import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown']

plt.bar(languages, popularity, color=colors)
plt.xlabel('Programming Language')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages (Multi-color)')
plt.show()
