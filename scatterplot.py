import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 7, 4, 10, 12, 15, 6, 8, 18]

# Create scatter plot
plt.scatter(x, y)
plt.title('Scatter Plot with Outliers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()