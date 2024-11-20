#import matplotlib.pyplot as plt
#import numpy as np
#
## Generate some sample data (replace this with your own data)
#data = [29, 31, 37, 43, 47, 47, 51, 58, 78, 80, 100, 124, 125, 128, 213, 218, 228, 242, 350, 422, 516, 563, 703, 780, 895, 1500, 2500, 2780, 3000, 5000, 13000, 27000, 403000]
#
## Create a logarithmic box and whisker plot
#plt.boxplot(data, vert=True)  # Set vert=False to create a horizontal box plot
#plt.yscale('log')  # Set the y-axis to logarithmic scale
#
## Add labels and title
#plt.xlabel('Data Values')
#plt.ylabel('Number of people ill')
#plt.title('Virus-caused waterborne outbreaks')
#
## Show the plot
#plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data (replace this with your own data),
data = [6, 24, 41, 43, 70, 73, 84, 92, 100, 108, 108, 134, 156, 174, 182, 194, 200, 229, 238, 305, 344, 368, 427, 448, 500, 631, 709, 758, 900, 924, 1000, 1393, 1500, 1614, 1640, 1699, 1750, 1783, 2400, 2400, 3000, 3000, 3600, 12000, 12145]
#bacteria-dead [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 6, 14, 14, 17, 18, 22, 71, 95, 296]
#protozoa-hospital [3, 5, 5, 28, 41]
#virus-hospital[3, 6, 6, 12, 35]
#bacteria-hospital [2, 3, 3, 4, 7, 9, 10, 10, 13, 14, 15, 16, 20, 32, 32, 35, 42, 46, 76, 84, 91, 163, 259, 449, 6673]
#virus-ill [6, 24, 41, 43, 70, 73, 84, 92, 100, 108, 108, 134, 156, 174, 182, 194, 200, 229, 238, 305, 344, 368, 427, 448, 500, 631, 709, 758, 900, 924, 1000, 1393, 1500, 1614, 1640, 1699, 1750, 1783, 2400, 2400, 3000, 3000, 3600, 12000, 12145]
#bacteria-ill [6, 15, 22, 27, 30, 39, 41, 58, 60, 62, 68, 71, 86, 91, 101, 103, 104, 105, 108, 114, 117, 122, 129, 138, 138, 154, 163, 183, 194, 206, 218, 234, 243, 251, 281, 288, 298, 304, 330, 394, 408, 434, 463, 628, 665, 670, 680, 694, 749, 756, 765, 775, 800, 865, 921, 1076, 1078, 1430, 1455, 1500, 1573, 1875, 2000, 2085, 2122, 2400, 2700, 3000, 8000, 8320, 8901, 10000, 16400, 22815]
#protozoa-ill [29, 31, 37, 43, 47, 47, 51, 58, 78, 80, 100, 124, 125, 128, 213, 218, 228, 242, 350, 422, 516, 563, 703, 780, 895, 1500, 2500, 2780, 3000, 5000, 13000, 27000, 403000]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a box and whisker plot
bp = ax.boxplot(data, vert=True, patch_artist=True)  # Set vert=False to create a horizontal box plot

# Set the y-axis to logarithmic scale
ax.set_yscale('log')

# Add labels and title
#ax.set_xlabel('Data Values')
#ax.set_ylabel('Number of People ill')
ax.set_title('Virus')

# Extract and display statistics
statistics = {
    '1st Quartile': np.percentile(data, 25),
    'Median': np.median(data),
    '3rd Quartile': np.percentile(data, 75),
    'Mean': np.mean(data),
    'Outliers': bp['fliers'][0].get_data()[1]
}

for label, value in statistics.items():
    print(f'{label}: {value}')

# Show the plot
plt.show()



