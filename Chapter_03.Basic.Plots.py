#A scatter plot is useful for visualizing the relationship between two continuous variables. Seaborn's scatterplot() function makes it easy to create informative scatter plots. Let's consider an example with randomly generated data

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# Create a scatter plot using Seaborn
sns.scatterplot(x=x, y=y)
plt.title('Scatter Plot Example')
plt.show()


#Line plots are useful for visualizing trends or patterns in data. Seaborn's lineplot() function simplifies the creation of line plots. Here's an example using a sine wave

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate data - sine wave
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a line plot using Seaborn
sns.lineplot(x=x, y=y)
plt.title('Line Plot Example')
plt.show()

#Histograms are essential for understanding the distribution of a single variable. Seaborn's histplot() function makes it easy to create histograms. Consider the following example:

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = np.random.randn(1000)

# Create a histogram using Seaborn
sns.histplot(data, bins=30, kde=True)
plt.title('Histogram Example')
plt.show()


#Seaborn comes with built-in datasets that are convenient for practicing and learning. Let's load and visualize the famous "tips" dataset:

import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
print(tips.head())

# Create a scatter plot using the "tips" dataset
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title('Scatter Plot with Tips Dataset')
plt.show()
















































