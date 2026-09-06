# Task:
# EXPLORATORY DATA ANALYSIS AND PRICE PREDICTION OF HOUSES:
# ▪ Perform EDA (Exploratory Data Analysis)
# ▪ Handle missing values
# ▪ Analyze feature relationships
# ▪ Build a basic regression model to predict house prices

# 1. Data Understanding
# a) Load the dataset using Pandas
# b) Display:
#     ▪ First 5 rows
#     ▪ Dataset shape
#     ▪ Column names
# c) Identify:
#     ▪ Numerical vs Categorical features

# 2. Data Cleaning
# a) Find missing values
# b) Handle missing data:
#     ▪ Numerical → fill with mean/median
#     ▪ Categorical → fill with mode

# c) Drop columns with too many missing values (e.g., >50%)
# 3. Univariate Analysis
# a) Plot distribution of:
#     ▪ SalePrice
#     ▪ GrLivArea
# b) Identify skewness and outliers

# TOOLS:
# • Histogram
# • Boxplot

# 4. Bivariate Analysis
# a) Find correlation with SalePrice
# b) Plot:
#     ▪ Scatter plot: GrLivArea vs SalePrice
#     ▪ Bar plot: OverallQual vs SalePrice
# c) Identify top 5 features affecting price

# 5. Multivariate Analysis
# a) Create a correlation heatmap
# b) Analyze strong positive/negative relationships

# 6. Feature Engineering
# a) Create new feature:
#     ▪ HouseAge = YrSold - YearBuilt
# b) Drop irrelevant features (like Id)

# 7. Model Building
# a) Split data into training/testing
# b) Apply:
#     ▪ Linear Regression
# c) Evaluate model using:
#     ▪ MAE
#     ▪ RMSE
#     ▪ R2 Score


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('house_prices_practice.csv')

print(df.head())

print("Shape:", df.shape)

print("Columns:", df.columns)

num_features = df.select_dtypes(include=['int64', 'float64']).columns
cat_features = df.select_dtypes(include=['object']).columns

print("Numerical Features:", num_features)
print("Categorical Features:", cat_features)

print(df.isnull().sum())

threshold = len(df) * 0.5
df = df.dropna(thresh=threshold, axis=1)

for col in df.select_dtypes(include=['int64', 'float64']):
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include=['object', 'string']):
    df[col] = df[col].fillna(df[col].mode()[0])

print("Remaining missing values:", df.isnull().sum().sum())

plt.figure(figsize=(8,5))
sns.histplot(df['SalePrice'], kde=True)
plt.title("SalePrice Distribution")
plt.show()

sns.boxplot(x=df['SalePrice'])
plt.show()

sns.histplot(df['GrLivArea'], kde=True)
plt.title("GrLivArea Distribution")
plt.show()

sns.boxplot(x=df['GrLivArea'])
plt.show()

corr = df.corr(numeric_only=True)
sale_corr = corr['SalePrice'].sort_values(ascending=False)
print(sale_corr)

sns.scatterplot(x=df['GrLivArea'], y=df['SalePrice'])
plt.show()

sns.barplot(x='OverallQual', y='SalePrice', data=df)
plt.show()

top5 = sale_corr[1:6]
print("Top 5 features affecting price:\n", top5)

plt.figure(figsize=(10,8))
sns.heatmap(corr, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

df['HouseAge'] = df['YrSold'] - df['YearBuilt']

if 'Id' in df.columns:
    df.drop('Id', axis=1, inplace=True)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X = df.select_dtypes(include=['int64', 'float64']).drop('SalePrice', axis=1)
y = df['SalePrice']

X = X.fillna(X.mean())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)
