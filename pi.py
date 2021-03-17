import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import statistics

N_ROWS = 25000

heights = np.empty(N_ROWS)
weights = np.empty(N_ROWS)

with open('heights-weights.csv', 'r') as f:
    rows = csv.reader(f)
    for i, row in enumerate(rows):
        if i == 0:  # Discard the first row (header)
            continue
        heights[i - 1] = row[1]
        weights[i - 1] = row[2]

        if i >= N_ROWS: # Safety check - check the number of rows in your CSV first and assign N_ROWS
            break

N_BINS = 1000
y, x = np.histogram(heights, bins=N_BINS)
x = x[1:]
window_size = N_BINS // 5 \
    + ((N_BINS//5) % 2 == 0)  # Adjust to make the window size odd

y = savgol_filter(y, window_size, 2) # Apply smoothing

y = y / max(y)  # "Squish" it down so its peak is 1

area = np.trapz(y, x=x)

sigma = statistics.stdev(heights)
pi = (area / sigma) ** 2 / 2

print(pi)

plt.plot(x, y)
plt.show()