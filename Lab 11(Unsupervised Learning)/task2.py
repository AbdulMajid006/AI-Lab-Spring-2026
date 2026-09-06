import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

df['vehicle_type'] = df['vehicle_type'].map({
    'SUV': 0,
    'Sedan': 1,
    'Truck': 2,
    'Hatchback': 3
})

X = df.values

wcss = []
for i in range(1, 6):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 6), wcss)
plt.title('Elbow Method (Without Scaling)')
plt.xlabel('K')
plt.ylabel('WCSS')
plt.show()

kmeans_no_scale = KMeans(n_clusters=3, random_state=42)
y_no_scale = kmeans_no_scale.fit_predict(X)

print("Cluster Labels (Without Scaling):")
print(y_no_scale)

vehicle_type = df[['vehicle_type']].values
numeric_features = df.drop('vehicle_type', axis=1)

scaler = StandardScaler()
scaled_numeric = scaler.fit_transform(numeric_features)

X_scaled = np.concatenate((scaled_numeric, vehicle_type), axis=1)

wcss_scaled = []
for i in range(1, 6):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss_scaled.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 6), wcss_scaled)
plt.title('Elbow Method (With Scaling except vehicle_type)')
plt.xlabel('K')
plt.ylabel('WCSS')
plt.show()

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
y_scaled = kmeans_scaled.fit_predict(X_scaled)

print("\nCluster Labels (With Scaling):")
print(y_scaled)

print("\nAnalysis")
print("Without Scaling: Clustering is dominated by large values like mileage and maintenance cost.")
print("With Scaling: All numerical features contribute equally, resulting in better grouping.")