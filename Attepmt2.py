#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:16:15 2023

@author: blakeclark
"""

import numpy as np
import matplotlib.pyplot as plt

file_path = "curve.data"

# Load data from the .data file using NumPy with space as the delimiter
data = np.loadtxt(file_path)

# Separate x and y values
x = data[:, 0]
y = data[:, 1]

# Plot the data using Matplotlib
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('X vs Y')
plt.grid(True)
plt.show()