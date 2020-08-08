# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)
print x
# Plot the data
plt.plot(x, x, label='linear')

# Add a legend mean leaner will show in the graph
plt.legend()

# Show the plot
plt.show()
