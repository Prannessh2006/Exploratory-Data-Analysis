
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


df = pd.read_excel('Online Retail.xlsx')

print("First 5 rows of the dataset:")
print(df.head())


print("\nMissing values in each column:")
print(df.isnull().sum())


df = df.dropna(subset=['CustomerID'])

df = df[df['Quantity'] > 0]

df = df[df['UnitPrice'] > 0]

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

df = df.dropna(subset=['InvoiceDate'])

print("\nNumber of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()


print("\nBasic statistics of numerical columns:")
print(df.describe())


plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.histplot(df['Quantity'], bins=50, kde=True)
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.xlim(0, df['Quantity'].quantile(0.99))  # Limit to 99th percentile to handle outliers

plt.subplot(2, 2, 2)
sns.histplot(df['UnitPrice'], bins=50, kde=True)
plt.title('Distribution of UnitPrice')
plt.xlabel('UnitPrice')
plt.xlim(0, df['UnitPrice'].quantile(0.99))  # Limit to 99th percentile

df['TotalSales'] = df['Quantity'] * df['UnitPrice']

top_countries = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head(10)
plt.subplot(2, 2, 3)
top_countries.plot(kind='bar')
plt.title('Top 10 Countries by Total Sales')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
sns.scatterplot(x='UnitPrice', y='Quantity', data=df)
plt.title('Quantity vs UnitPrice')
plt.xlabel('UnitPrice')
plt.ylabel('Quantity')
plt.xlim(0, df['UnitPrice'].quantile(0.99))
plt.ylim(0, df['Quantity'].quantile(0.99))

plt.tight_layout()
plt.show()


df['Month'] = df['InvoiceDate'].dt.month
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()

monthly_sales = df.groupby('Month')['TotalSales'].sum()
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.show()

day_sales = df.groupby('DayOfWeek')['TotalSales'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.figure(figsize=(10, 5))
day_sales.plot(kind='bar')
plt.title('Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 products by quantity sold:")
print(top_products)

top_countries_qty = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 countries by quantity sold:")
print(top_countries_qty)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Quantity'])
plt.title('Box Plot of Quantity')
plt.ylim(0, df['Quantity'].quantile(0.99))

plt.subplot(1, 2, 2)
sns.boxplot(y=df['UnitPrice'])
plt.title('Box Plot of UnitPrice')
plt.ylim(0, df['UnitPrice'].quantile(0.99))

plt.tight_layout()
plt.show()

Q1 = df[['Quantity', 'UnitPrice']].quantile(0.25)
Q3 = df[['Quantity', 'UnitPrice']].quantile(0.75)
IQR = Q3 - Q1
outliers = ((df[['Quantity', 'UnitPrice']] < (Q1 - 1.5 * IQR)) | 
            (df[['Quantity', 'UnitPrice']] > (Q3 + 1.5 * IQR))).any(axis=1)
print("\nNumber of rows with outliers:", outliers.sum())

print("\nSummary of Findings:")
print("- The dataset was cleaned by removing missing values, negative quantities/prices, and duplicates.")
print("- Sales are highest in certain months, indicating seasonal trends.")
print("- Specific days of the week show higher sales, suggesting targeted promotions.")
print("- Top-selling products and countries were identified, useful for inventory and marketing strategies.")
print("- Outliers were detected, which may represent bulk orders or errors needing further investigation.")
