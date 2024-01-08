import json

import matplotlib.pyplot as plt

"""
This file is used to visualise the test
data if you need to

Change the file_path variable below to plot the test data
"""

file_path = "data/meetings_small.json"


# Load intervals from file
# Change the path to the file to PLOT
with open(file_path) as file:
    intervals = json.load(file)

# Plotting the intervals on a line
for interval in intervals:
    plt.plot(interval, [1, 1], marker='o')  # Plot each interval on the same line (y=1)

# Setting the limits for better visualization

# Removing the y-axis as it's not needed for this representation
plt.yticks([])

# Adding title and labels
plt.title("Plot of Meetings")
plt.xlabel("Value")

# Showing the plot
plt.show()
