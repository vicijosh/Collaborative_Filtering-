
# Video Recommendation System Using Collaborative Filtering

This project demonstrates the construction of a video recommendation system using Collaborative Filtering with Singular Value Decomposition (SVD) on a dataset of global YouTube statistics.

## Overview
The recommendation system aims to suggest videos based on user interactions, specifically focusing on the 'likes' metric as an indicator of user preference.

## Methodologies
1. **Data Preprocessing**: Filtered out entries with missing video IDs or channel titles and generated a user-video interaction matrix.
2. **Exploratory Data Analysis (EDA)**: Identified the top 10 channels with the most videos and visualized the data.
3. **Model Building**: Utilized Collaborative Filtering with SVD and split the data into training and test sets.
4. **Evaluation**: Evaluated the model's performance using the Root Mean Squared Error (RMSE).

## How to Run
1. Ensure you have the necessary libraries installed (pandas, numpy, matplotlib, seaborn, surprise).
2. Download the 'Global_YouTube_Statistics.csv' dataset.
3. Run the `video_recommendation.py` script.
4. Visualize the results and the model's performance metric (RMSE).

## Note
This project uses the `surprise` library for the implementation of the SVD recommendation algorithm. Ensure you have this library installed before running the script.
