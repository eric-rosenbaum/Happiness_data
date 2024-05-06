# Happiness Correlation Dashboard

## Overview
This project explores how various lifestyle factors correlate with happiness. It uses a Streamlit dashboard to visualize these correlations dynamically, allowing users to select different categories and see how each factor correlates with happiness.

## Dashboard Photo
<img width="1388" alt="Screen Shot 2024-05-06 at 6 46 39 PM" src="https://github.com/eric-rosenbaum/Happiness_data/assets/161375414/a9437ee8-9e09-4564-a273-a96713402b32">


## Features
- **Interactive Visualizations**: Explore correlations through interactive graphs.
- **Category Selection**: Filter data by categories like Music, Lifestyle, Movies, School Subjects, and more.
- **Statistical Insights**: View calculated Pearson correlation coefficients, t-values, and p-values.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/happiness-dashboard.git
   
2. Navigate to the project directory:
   ```bash
   cd happiness-dashboard
3. Install the required packages:
    ```bash
    pip install -r requirements.txt

4. Run application:
    ```bash
    streamlit run app.py

## Data
This project utilizes the "Young People Survey" dataset from Kaggle, which gathers responses on various
lifestyle preferences and happiness indicators among young people. Note that the data path in the script
should be adjusted to the location where you have stored the `responses.csv` on your local machine.
You can find more information about the dataset and download it from [Kaggle's Young People Survey page](https://www.kaggle.com/datasets/miroslavsabo/young-people-survey).



