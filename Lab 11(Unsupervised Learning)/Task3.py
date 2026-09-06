# Task#3:
# The academic affairs department at FAST NUCES Karachi is looking to identify distinct groups of
# students based on their academic engagement and performance. The department has access to
# anonymized student data containing the attributes student_id, GPA, study_hours (average weekly
# study hours), and attendance_rate (percentage of classes attended).
# The goal is to group students into meaningful clusters that can help tailor academic support
# programs, such as extra tutoring, mentoring sessions, or motivation workshops.
# You are required to perform unsupervised learning using K-Means clustering on the student
# dataset. Do following :

# ● Feature Selection and Scaling: Use the following features for clustering: GPA, study_hours,
# and attendance_rate.
# ● Apply appropriate feature scaling before clustering.
# ● Determine Optimal Number of Clusters (K): Use the ELbow method to determine the optimal
# number of clusters (K) in the range of 2 to 6.
# ● Perform Clustering: Apply K-Means using the optimal K and assign a cluster label to each
# student.
# ● Visualization: Create a scatter plot to visualize the clusters using study_hours and GPA as the
# axes.
# ● Color each point based on its cluster.
# ● Add an informative title and labels for clarity.
# ● Deliverables: Display the final dataset showing student IDs along with their assigned cluster.
# ● Present the scatter plot that illustrates the clustering result.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

n = 30
df = pd.DataFrame({
    'student_id': range(1, n+1),
    'GPA': np.round(np.random.uniform(2.0, 4.0, n), 2),
    'study_hours': np.random.randint(5, 35, n),
    'attendance_rate': np.random.randint(60, 100, n)
})

X = df[['GPA', 'study_hours', 'attendance_rate']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
for i in range(2, 7):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2, 7), wcss)
plt.xlabel('K')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()

optimal_k = 3

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

print(df[['student_id', 'cluster']])

plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'])
plt.xlabel('Study Hours')
plt.ylabel('GPA')
plt.title('Student Clusters')
plt.show()
