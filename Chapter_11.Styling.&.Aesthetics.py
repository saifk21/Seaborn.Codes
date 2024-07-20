#In this chapter, we'll explore how to fine-tune the aesthetics of Seaborn plots to make them visually appealing and more informative.

#Seaborn provides various parameters to customize the aesthetics of your plots. Let's go through an example where we adjust the color palette, increase the figure size, and set plot titles:

import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Set a custom color palette
custom_palette = ["#FF7F50", "#6495ED", "#FFD700", "#98FB98"]
sns.set_palette(custom_palette)

# Increase the figure size
plt.figure(figsize=(10, 6))

# Create a bar plot with the custom color palette
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Bar Plot with Custom Color Palette')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill Amount')
plt.show()


# In this example:

# sns.set_palette(custom_palette) sets a custom color palette for the plot.
# plt.figure(figsize=(10, 6)) increases the figure size.
# plt.title(), plt.xlabel(), and plt.ylabel() are used to add labels and a title to the plot.




#Seaborn provides styling functions that allow you to control the overall appearance of your plots. Let's use set_style() and set_context() to change the style and context of a scatter plot:


import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set the context to "talk" for larger text and labels
sns.set_context("talk")

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title('Scatter Plot with Dark Grid Style and Larger Text')
plt.show()


# In this example:

# sns.set_style("darkgrid") sets the overall style of the plot to "darkgrid."
# sns.set_context("talk") sets the context to "talk" for larger text and labels.