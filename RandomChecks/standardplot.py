import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 40, 200)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.cos(x))       # Plot the sine of each x point
plt.show()