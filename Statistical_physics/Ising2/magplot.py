import matplotlib.pyplot as plt

a = []
with open('mag.log', 'r') as file:
    for line in file:
        a.append(float(line))


x = range(30000, 50030000, 100)
plt.scatter(x, a, marker='.', c='#1b9e77')
plt.title('Flips at T* = 1.6')
plt.xlabel('Monte Carlo Steps')
plt.ylabel('Average magnetisation')
plt.show()