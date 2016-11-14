import matplotlib.pyplot as plt
import numpy as np

y = np.random.uniform(0,1,1000000)

plt.hist(y, 100)
plt.show()