import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
X = np.linspace(0, 2*np.pi, 100)
Y = np.cos(X)
fig, ax = plt.subplots()
ax.plot(X, Y)
fig.savefig("1")
fig.show()
plt.show()
