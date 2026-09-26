import matplotlib.pyplot as plt

with open("3_data.txt", "r") as f:
    data = f.read()

data = data.split('\n')

x = [row.split()[0] for row in data if row.strip()]
y = [row.split()[1] for row in data if row.strip()]

x = [float(value) for value in x]
y = [float(value) for value in y]

plt.plot(x, y)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('graph')

plt.show()