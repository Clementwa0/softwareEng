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

# Create a bar plot
# Sample data
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

plt.bar(names, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

# pie chart
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 30, 20, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Programming Language Popularity")
plt.show()

# histogram
ages = [22, 23, 22, 21, 25, 24, 22, 23, 24, 25] 
plt.hist(ages, bins=5, color='blue', alpha=0.7)
plt.title("Age Distribution")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.show()


