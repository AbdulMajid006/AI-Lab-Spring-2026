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