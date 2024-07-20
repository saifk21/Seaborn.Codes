#Seaborn allows you to customize the colors and styles of your plots easily. Let's consider an example of a scatter plot with custom colors:

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# Create a scatter plot with custom colors
sns.scatterplot(x=x, y=y, color='skyblue')
plt.title('Scatter Plot with Custom Color')
plt.show()


#You can further customize styles using Seaborn's built-in themes. For example, let's use the "darkgrid" theme:

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# Set the style to 'darkgrid'
sns.set(style='darkgrid')

# Create a scatter plot with the 'darkgrid' style
sns.scatterplot(x=x, y=y, color='coral')
plt.title('Scatter Plot with Dark Grid Style')
plt.show()


#Adding clear labels and titles to your plots is essential for conveying information. Let's enhance a histogram with informative labels:

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = np.random.randn(1000)

# Create a labeled histogram
sns.histplot(data, bins=30, kde=True)
plt.title('Distribution of Random Data')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()


#Seaborn offers a variety of color palettes to enhance the visual appeal of your plots. Let's use a custom color palette for a categorical plot:

import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Define a custom color palette
custom_palette = ["#FF7F50", "#6495ED", "#FFD700", "#98FB98"]

# Create a bar plot with the custom color palette
sns.barplot(x="day", y="total_bill", data=tips, palette=custom_palette)
plt.title('Bar Plot with Custom Color Palette')
plt.show()

























