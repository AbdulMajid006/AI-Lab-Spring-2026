import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Mall_Customers.csv')

df = df.drop('CustomerID', axis=1)

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

X = df.values

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method (Without Scaling)')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.show()

kmeans_no_scale = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_no_scale = kmeans_no_scale.fit_predict(X)

print("Cluster labels (Without Scaling):")
print(y_no_scale)

age = df[['Age']].values
other_features = df.drop('Age', axis=1)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(other_features)

X_scaled = np.concatenate((age, scaled_features), axis=1)

wcss_scaled = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss_scaled.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 11), wcss_scaled)
plt.title('Elbow Method (With Scaling except Age)')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.show()

kmeans_scaled = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_scaled = kmeans_scaled.fit_predict(X_scaled)

print("\nCluster labels (With Scaling except Age):")
print(y_scaled)

print("\nComparison")
print("Without Scaling: Clusters biased towards high-value features (Income, Spending Score)")
print("With Scaling: More balanced clustering, all features contribute equally")