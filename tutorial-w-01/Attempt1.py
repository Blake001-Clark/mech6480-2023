import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

file_path = "curve.data"

# Load data from the .data file using NumPy with space as the delimiter
data = np.loadtxt(file_path)

# Separate x and y values
x = data[:, 0]
y = data[:, 1]

# Calculate the forward difference derivative
dx_forward = x[1] - x[0]
dy_forward = np.diff(y) / dx_forward

# Calculate the central difference derivative
dx_central = (x[1:] - x[:-1]) / 2
dy_central = np.diff(y) / dx_central

# Create a figure and axis (subplots) using plt.subplots()
fig, ax = plt.subplots()

# Plot the data on the axis 'ax'
ax.plot(x, y, marker='o', linestyle='-', label='Original Data')
ax.set_xlabel('X Values')
ax.set_ylabel('Y Values')
ax.set_title('X vs Y')

# Add a timestamp to the plot
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ax.annotate(timestamp, xy=(0.7,0.95), xycoords='figure fraction', annotation_clip=False)

# Add a revision stamp to the plot
from git import Repo
repo = Repo('.', search_parent_directories=True)
revsha = repo.head.object.hexsha[:8]
ax.annotate(f"[rev {revsha}]", xy=(0.05,0.95), xycoords='figure fraction', annotation_clip=False)

# Plot the forward difference derivative
ax.plot(x[:-1], dy_forward, marker='x', linestyle='-', label='Forward Difference')

# Plot the central difference derivative
ax.plot(x[:-1], dy_central, marker='^', linestyle='-', label='Central Difference')

ax.legend()
ax.grid(True)
plt.show()