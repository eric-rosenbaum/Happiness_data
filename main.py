import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np


# Load data
data = pd.read_csv('/Users/ericrosenbaum/Desktop/pysych data/responses.csv')
valid_columns = [col for col in data.columns if data[col].dtype in ['int64', 'float64'] and data[col].iloc[0] in [1, 2, 3, 4, 5]]
data = data[valid_columns]

# Compute correlations
correlations = data.corr()


def compute_all_stats(data, target, columns):
    results = []
    for column in columns:
        if column != target:  # Exclude the target variable from comparison against itself
            clean_data = data[[column, target]].dropna()
            if len(clean_data) > 2:  # Pearson requires at least 3 pairs to calculate
                correlation, p_value = pearsonr(clean_data[column], clean_data[target])
                t_value = (correlation * (len(clean_data) - 2) ** 0.5) / ((1 - correlation ** 2) ** 0.5)
                results.append((column, correlation, t_value, p_value))

    stats_df = pd.DataFrame(results, columns=['Variable', 'Correlation', 'T-value', 'P-value'])
    return stats_df

# Streamlit page config
st.set_page_config(page_title="Happiness Correlation Dashboard", layout="wide")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.title('Happiness Correlation Dashboard')
    st.write("Explore how different factors correlate with happiness.")

    # Allow users to select a variable to view correlations
    options = data.columns.tolist()
    selected_option = st.selectbox('Select a factor to see its correlation with happiness:', options)

    grouped_data = data.groupby(selected_option)['Happiness in life'].mean().reset_index()

    # Visualize the correlation
    fig, ax = plt.subplots()
    ax.scatter(grouped_data[selected_option], grouped_data['Happiness in life'], color='blue')
    sns.regplot(x=selected_option, y='Happiness in life', data=data, ax=ax, scatter=False)

    # Add a grid to the background of the plot
    ax.grid(True, linestyle='-', linewidth='0.5', color='gray',
            alpha=0.5)  # Adjust these parameters for desired grid style

    # Improving aesthetics
    ax.set_facecolor('whitesmoke')  # Sets the background color to a light gray, making the grid lines stand out

    st.pyplot(fig)

with col2:
    st.title("Ranked Correlations with Happiness")

    # Group data into categories (example categories, adjust as necessary)
    categories = {
        'Music': ['Dance', 'Folk', 'Country', 'Classical music', 'Musical', 'Pop', 'Rock', 'Metal or Hardrock', 'Punk',
                  'Hiphop, Rap', 'Swing, Jazz', 'Rock n roll', 'Alternative', 'Latino', 'Techno, Trance', 'Opera'],
        'Lifestyle': ['Healthy eating', 'Music', 'Movies'],
        'Movies': ['Horror', 'Thriller', 'Comedy', 'Romantic', 'Sci-fi', 'War', 'Fantasy/Fairy tales', 'Animated',
                   'Documentary', 'Western', 'Action'],
        'School Subject': ['History', 'Psychology', 'Politics', 'Mathematics', 'Physics', 'Economy Management', 'Biology',
                           'Chemistry', 'Reading', 'Geography', 'Foreign languages', 'Medicine', 'Law'],
        'Interests': ['Cars', 'Art exhibitions', 'Religion', 'Countryside, outdoors', 'Dancing', 'Musical instruments',
                      'Writing', 'Passive sport', 'Active sport', 'Gardening', 'Celebrities', 'Shopping',
                      'Science and technology', 'Theatre', 'Fun with friends', 'Adrenaline sports', 'Pets']
    }

    # Option to select category
    category_options = list(categories.keys()) + ['All']
    selected_category = st.selectbox('Select a category to view correlations:', category_options)

    # Filter correlations based on selected category and calculate stats
    if selected_category != 'All':
        relevant_columns = categories[selected_category]
    else:
        relevant_columns = data.columns.tolist()

    # Compute and display statistics
    stats_df = compute_all_stats(data, 'Happiness in life', relevant_columns)
    stats_df.index.name = 'Question Number'
    sorted_stats_df = stats_df.sort_values(by='Correlation', key=abs, ascending=False)
    st.table(sorted_stats_df)

# Run the app with:
# streamlit run app.py
