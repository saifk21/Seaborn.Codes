#Advanced plot customization in Seaborn involves manipulating various elements of the plot for more detailed and specialized visualizations. Let's create a customized violin plot with added elements:

import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Create a customized violin plot
plt.figure(figsize=(10, 6))

# Set the style to "whitegrid"
sns.set(style="whitegrid")

# Create a violin plot with custom elements
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True, inner="quart", palette="Set2")

# Add a title and customize the legend
plt.title('Customized Violin Plot')
plt.legend(title='Sex', loc='upper right')

plt.show()


#In this example:

# sns.set(style="whitegrid") sets the overall style of the plot to "whitegrid."
# Various parameters in sns.violinplot() are used for customization, such as split, inner, and palette.
# The legend is customized using plt.legend().



#Seaborn seamlessly integrates with machine learning workflows for visualizing relationships in datasets. Let's create a pair plot with different colors for each target class in a machine learning dataset:


import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_names'] = iris.target_names[iris.target]

# Create a pair plot with different colors for each target class
sns.pairplot(iris_df, hue='target_names', palette='viridis')
plt.suptitle('Pair Plot with Machine Learning Integration', y=1.02)
plt.show()


# The Iris dataset from scikit-learn is used.
# sns.pairplot() is used to create a pair plot, and the hue parameter is set to the target class.
# The palette parameter specifies the color palette for different classes.




#Seaborn can be extended with custom functions to create specialized plots or modify existing ones. Let's create a custom function for a specialized plot:

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Define a custom function for a polar plot
def polar_plot(data, categories, title='Custom Polar Plot'):
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    plt.polar(angles, data, marker='o')
    plt.fill(angles, data, alpha=0.25)

    plt.title(title)
    plt.show()

# Generate random data for the polar plot
random_data = np.random.randint(1, 10, 5)
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']

# Use the custom function to create a polar plot
polar_plot(random_data, categories, title='Custom Polar Plot Example')


# In this example:

# The polar_plot function is defined to create a polar plot with random data and specified categories.
# The function uses plt.polar() and plt.fill() to create the plot.
# These advanced topics showcase the flexibility of Seaborn for customizing and extending its functionality, making it a powerful tool for a wide range of data visualization tasks, including advanced customization, machine learning integration, and custom function creation.