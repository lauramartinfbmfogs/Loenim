import matplotlib
matplotlib.use('agg')  # Set the backend to 'Agg'

import matplotlib.pyplot as plt

# Create a simple plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Simple Plot')

# Save the plot to a file
plt.savefig('plot.png')
