# sa3 x7
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()
plt.plot(ypoints, linestyle = 'dotted')
plt.show()
plt.plot(ypoints, linestyle = 'dashed')
plt.show()

# it will three graph with defined style by making x axix its index and y axes given array