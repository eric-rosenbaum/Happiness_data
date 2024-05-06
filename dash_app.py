import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('/Users/ericrosenbaum/Desktop/pysych data/responses.csv')
valid_columns = [col for col in data.columns if data[col].dtype in ['int64', 'float64'] and data[col].iloc[0] in [1, 2, 3, 4, 5]]
data = data[valid_columns]


# Streamlit page config
st.set_page_config(page_title="Happiness Correlation Dashboard", layout="wide")

# Title for your dashboard
st.title('Happiness Correlation Dashboard')

# A simple description
st.write("Explore how different factors correlate with happiness.")

# Allow users to select a variable to view correlations
options = data.columns.tolist()  # Assuming your dataset is already loaded and ready
selected_option = st.selectbox('Select a factor to see its correlation with happiness:', options)

# Calculate correlations
correlations = data.corr()

# Display the selected variable correlation
st.write(f"Correlation with Happiness for {selected_option}: ", correlations.loc['Happiness in life', selected_option])

# Visualize the correlation
fig, ax = plt.subplots()
sns.regplot(x=selected_option, y='Happiness in life', data=data, ax=ax)
st.pyplot(fig)
