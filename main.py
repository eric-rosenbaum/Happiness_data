import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

import numpy as np

# Load the survey data
data = pd.read_csv('/Users/ericrosenbaum/Desktop/pysych data/responses.csv')

# Define the column names for factors to be plotted
factors = ['Interests or hobbies', 'Movies', 'Healthy eating', 'Public speaking']
happiness_column = 'Happiness in life'  # Replace with exact name if different

# Create a figure with subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))  # Adjusted figsize here

axes = axes.flatten()  # Flatten the array to make iteration easier

# Loop through the factors and create a plot for each
for i, factor in enumerate(factors):
    # Group the data by the current factor and calculate the mean and count of happiness
    grouped_data = data.groupby(factor)[happiness_column].agg(['mean', 'count']).reset_index()

    # Plotting on the respective subplot
    sns.regplot(ax=axes[i], x=factor, y='mean', data=grouped_data, ci=None, scatter_kws={'s': 100})
    axes[i].set_title(f'Average Happiness by {factor}')
    axes[i].set_xlabel(f'{factor} Preference Level (1-5)')
    axes[i].set_ylabel('Average Happiness')
    axes[i].grid(True)

    # Print the number of people in each bin for the current factor
    print(f"Number of people in each {factor} preference level:")
    print(grouped_data[[factor, 'count']])

# Adjust layout
plt.tight_layout()
plt.show()
