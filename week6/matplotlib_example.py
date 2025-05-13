import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# bar chart
names = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 10]
plt.bar(names, values)
plt.title("Simple Bar Chart")
plt.xlabel("Names")
plt.ylabel("Values")
plt.show()

# histogram
activities = ['sleeping', 'eating', 'working', 'playing']
hours = [8, 2, 8, 6]

plt.bar(activities, hours)
plt.title("Simple Histogram")
plt.xlabel("Activities")
plt.ylabel("Hours")
plt.show()
# pie chart
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 30, 20, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Simple Pie Chart")
plt.show()

# scatter plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
plt.scatter(x, y)
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
