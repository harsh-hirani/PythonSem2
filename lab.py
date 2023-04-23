# p8 2
# Using the given code snippet generate an array x and display the histogram for the generated x.

import numpy as np 
import matplotlib.pyplot as mlt 
x =np.random.normal(170,10,250)
# print(x)\
mlt.hist(x)
mlt.show()