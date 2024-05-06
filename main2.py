import pandas as pd

# Load the survey data
data = pd.read_csv('/Users/ericrosenbaum/Desktop/pysych data/responses.csv')

# Automatically exclude columns where the first value is not between 1 and 5
valid_columns = [col for col in data.columns if data[col].dtype in ['int64', 'float64'] and data[col].iloc[0] in [1, 2, 3, 4, 5]]

# Filter the dataset to include only the valid columns
# Ensure 'Happiness in life' is correctly spelled and matches exactly with your dataset
filtered_data = data[valid_columns]

# Compute the correlation with 'Happiness in life'
# Ensure this column is exactly named as in your dataset; adjust if necessary
correlations = filtered_data.corr()['Happiness in life']

# Display the correlations
pd.set_option('display.max_rows', None)     # Ensure all rows are shown


# Compute the correlation with 'Happiness in life' and sort it from smallest to largest
sorted_correlations = correlations.sort_values()

# Display the sorted correlations
print("Sorted correlations from smallest to largest:")
print(sorted_correlations)
