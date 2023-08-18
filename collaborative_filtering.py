
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Generate a mock user-video matrix for demonstration purposes
np.random.seed(42)
num_users = 100
num_videos = 1000
user_video_matrix = np.random.randint(1, 6, (num_users, num_videos))

# User-Based Collaborative Filtering
def recommend_videos_user_based(user_id, N=5):
    user_similarity = cosine_similarity(user_video_matrix)
    sim_values = user_similarity[user_id]
    predicted_ratings = np.dot(sim_values, user_video_matrix) / np.array([np.abs(sim_values).sum(axis=0)])
    video_indices = predicted_ratings.argsort()[::-1]
    rated_videos = np.where(user_video_matrix[user_id] > 0)[0]
    recommended_indices = [video for video in video_indices if video not in rated_videos]
    return recommended_indices[:N]

# Item-Based Collaborative Filtering
def recommend_videos_item_based(user_id, N=5):
    video_similarity = cosine_similarity(user_video_matrix.T)
    user_ratings = user_video_matrix[user_id]
    predicted_ratings = user_ratings.dot(video_similarity) / np.array([np.abs(video_similarity).sum(axis=1)])
    video_indices = predicted_ratings.argsort()[::-1]
    rated_videos = np.where(user_ratings > 0)[0]
    recommended_indices = [video for video in video_indices if video not in rated_videos]
    return recommended_indices[:N]

# Example usage:
# user_based_recommendations = recommend_videos_user_based(5)
# item_based_recommendations = recommend_videos_item_based(5)
