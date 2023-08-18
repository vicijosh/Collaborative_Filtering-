
# Collaborative Filtering for Video Recommendation

This project demonstrates the use of collaborative filtering techniques to recommend videos to users.

## Overview
Collaborative filtering is a method of making predictions about the interest of a user by collecting preferences or taste information from many users. The underlying assumption is that if a user A has the same opinion as a user B on an issue, A is more likely to have B's opinion on a different issue.

## Methodologies
1. **User-Based Collaborative Filtering**: This method finds users that are similar to the target user based on their ratings. Items that these similar users have liked are recommended to the target user.
2. **Item-Based Collaborative Filtering**: Instead of finding similar users, this method finds similar items based on user ratings. For a target user, items that are similar to the ones they've highly rated are recommended.

## Results
Due to the nature of the mock data where every user "rated" every video, the recommendation approach couldn't suggest new videos. However, the methodology and code can be applied to real-world datasets with sparse user-item interactions for effective recommendations.

## How to Run
1. Ensure you have the necessary libraries installed.
2. Run the `collaborative_filtering.py` script.
3. Check the recommendations for the specified user.

## Note
This project is a demonstration using mock data. In a real-world scenario, most users will have only interacted with or rated a small subset of items, which makes collaborative filtering effective in recommending unrated items.
