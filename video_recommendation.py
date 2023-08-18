
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import cross_validate

# Data Loading
data_path = "PATH_TO_YOUR_DATASET/Global_YouTube_Statistics.csv"  # <-- Adjust this path
data = pd.read_csv(data_path)

# Data Preprocessing
data = data.dropna(subset=['video_id', 'channel_title'])
user_video_ratings = data.groupby(['channel_title', 'video_id'])['likes'].mean().unstack().fillna(0)
user_video_matrix = user_video_ratings.applymap(lambda x: 1 if x > 0 else 0)

# EDA
top_channels = data['channel_title'].value_counts()[:10]

# Model Building using Collaborative Filtering with SVD
reader = Reader()
ratings = data[['channel_title', 'video_id', 'likes']]
data_surprise = Dataset.load_from_df(ratings, reader)
trainset, testset = train_test_split(data_surprise, test_size=0.25)

model = SVD()
model.fit(trainset)
predictions = model.test(testset)

# Evaluation
rmse = accuracy.rmse(predictions)

