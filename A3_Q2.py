import matplotlib.pyplot as plt

# Defining the programming languages and their popularity
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating a pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%')

# Adding a title
plt.title('Popularity of Programming Languages')

# Showing the chart
plt.show()
