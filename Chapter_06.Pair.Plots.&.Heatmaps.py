#Pair plots are an excellent way to visualize pairwise relationships between multiple variables in a dataset. Seaborn's pairplot() function simplifies the creation of such plots. Let's use the "iris" dataset for this example:

import seaborn as sns
import matplotlib.pyplot as plt

# Load the "iris" dataset
iris = sns.load_dataset("iris")

# Create a pair plot
sns.pairplot(iris, hue="species")
plt.suptitle('Pairwise Relationships in the Iris Dataset', y=1.02)
plt.show()


#In this example:

#The pairplot() function creates scatter plots for all pairwise combinations of numerical features.
#The hue="species" parameter colors the data points based on the species of the iris flower.



#Heatmaps are effective for representing data in a matrix form, providing a visual summary of the magnitude of a phenomenon. Seaborn's heatmap() function simplifies the creation of heatmaps. Let's use a correlation matrix as an example:

import seaborn as sns
import matplotlib.pyplot as plt

# Load the "iris" dataset
iris = sns.load_dataset("iris")

# Select only the numerical columns
numerical_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
numerical_data = iris[numerical_columns]

# Compute the correlation matrix
correlation_matrix = numerical_data.corr()

# Create a heatmap of the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title('Correlation Heatmap of Iris Dataset')
plt.show()


#In this example:

#The heatmap() function is used to visualize the correlation matrix.
#The annot=True parameter adds numerical annotations to the heatmap cells.
#The cmap="coolwarm" parameter sets the color map for the heatmap.


#Heatmaps can also be used to represent data in a matrix form, providing insights into patterns or distributions. Let's create a simple matrix-form heatmap:

import seaborn as sns
import matplotlib.pyplot as plt

# Create a matrix-form heatmap
matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sns.heatmap(matrix_data, annot=True, cmap="Blues", cbar=False)
plt.title('Matrix-form Heatmap Example')
plt.show()

