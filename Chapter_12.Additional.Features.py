#In this chapter, we'll explore additional features in Seaborn, including handling missing data, context settings, and adding annotations to plots.

#Dealing with missing data is crucial in data analysis. Seaborn provides methods to visualize and handle missing data effectively. Let's use a heatmap to visualize missing data in a dataset:

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dataset with missing values
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8], 'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# Create a heatmap to visualize missing data
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
plt.title('Missing Data Visualization')
plt.show()


# In this example:

# df.isnull() generates a DataFrame of the same shape as df, where each cell is True if the corresponding cell in df is NaN, and False otherwise.
# sns.heatmap() is used to visualize this binary matrix, where missing values are highlighted.




#Context settings in Seaborn allow you to control the size, scale, and style of the plots. Let's use different context settings for a bar plot:

import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Create a bar plot with different context settings
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
sns.set_context("notebook")
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Context: notebook')

plt.subplot(2, 2, 2)
sns.set_context("paper")
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Context: paper')

plt.subplot(2, 2, 3)
sns.set_context("talk")
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Context: talk')

plt.subplot(2, 2, 4)
sns.set_context("poster")
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Context: poster')

plt.tight_layout()
plt.show()


# In this example:

# sns.set_context() is used to set the plotting context to different values.
# The bar plot is created under different context settings, influencing the size and scale of the plot.




#Annotations help in providing additional information on specific points in a plot. Let's add annotations to a scatter plot:



import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Add annotations for specific points
plt.text(20, 2, 'Annotation 1', fontsize=10, color='red')
plt.text(40, 5, 'Annotation 2', fontsize=12, color='blue')

plt.title('Scatter Plot with Annotations')
plt.show()



# In this example:

# plt.text() is used to add text annotations at specific coordinates on the scatter plot.
# Adding annotations allows you to highlight and provide additional context to specific points of interest in your visualizations.