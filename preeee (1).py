import pandas as pd
import re

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math

# Read the CSV file
df = pd.read_csv(r'D:\py\font67.csv')

pattern = r'(\d+\.\d+)'  # Regular expression pattern to match floating-point numbers
df['rating'] = df['rating'].str.extract(pattern).astype(float)
columns_to_check = ['Description', 'Price', 'rating', 'reviewcount', 'url']

# Remove rows with null values in the specified columns
df = df.dropna(subset=columns_to_check)


# Load your data into a Pandas DataFrame
 # Replace 'your_dataset.csv' with your actual file path or data source

num1 = int(input("Enter how many keywords you need to enter: "))
input_descriptions = []

for x in range(num1):
    input_description = input("Enter the input for Description: ")
    input_descriptions.append(input_description)

# Filter data based on input descriptions using regular expression
filtered_data = df[df['Description'].str.contains('|'.join(input_descriptions), case=False, regex=True)]

print(filtered_data)
# Save the filtered data to a new CSV file
filtered_data.to_csv('filtered_data8.csv', index=False)  # Replace 'filtered_data.csv' with your desired file name

print("Filtered data saved to 'filtered_data8.csv'")
df = pd.read_csv(r'D:\py\filtered_data8.csv')
df['reviewcount'] = df['reviewcount'].str.replace(r'[\(\),]', '', regex=True).astype(float)

# Now the 'reviewcount' column is of float type
#print(df.dtypes)  # To confirm the data types
df['Price'] = df['Price'].str.replace('$', '').astype(float)
min_value = df['reviewcount'].min()
max_value = df['reviewcount'].max()

# Step 2: Define the number of ranges
num_ranges = 5

# Step 3: Calculate the range width
   
range_width = (max_value - min_value) / num_ranges
range_width = round(range_width)  # Adjust if needed to obtain whole numbers

# Step 4: Create thnee ranges
ranges = [min_value + i * range_width for i in range(num_ranges)]
ranges.append(max_value) 
 # Include the maximum value as the last range boundary

# Step 5: Count the number of products in each range
counts1 = pd.cut(df['reviewcount'], ranges).value_counts().sort_index()

# Step 6: Analyze the results
#print(counts1)
total_products_reviewcount = counts1.sum()

# Step 8: Calculate the percentages for reviewcount
percentages_reviewcount = counts1 / total_products_reviewcount * 100


# Step 9: Display the counts and percentages for reviewcount

# Clean the 'Price' column
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)
  # Convert to numeric, coerce invalid values to NaN


# Assumiimport pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the data from the CSV file

# Prepare the 'Price' data for clustering
X_price = df[['Price']].values

# Choose the number of clusters (you can experiment with this)
n_clusters_price = 5
kmeans_price = KMeans(n_clusters=n_clusters_price, random_state=42)
df['price_cluster'] = kmeans_price.fit_predict(X_price)

# Identify the cluster with the maximum number of data points for Price
max_price_cluster = df['price_cluster'].value_counts().idxmax()
cluster_price_data = df[df['price_cluster'] == max_price_cluster]

# Calculate the range of Price for the cluster with maximum rows
max_price_range = cluster_price_data['Price'].min()-3, cluster_price_data['Price'].max()

print(f"Range with maximum rows for Price: {max_price_range}")

# Plot the histogram of price clusters
plt.hist(df['Price'], bins=20, alpha=0.5, label='All Data')
for cluster in range(n_clusters_price):
    cluster_price_data = df[df['price_cluster'] == cluster]
    plt.hist(cluster_price_data['Price'], bins=20, alpha=0.5, label=f'Cluster {cluster}')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Prices by Cluster')
plt.legend()
plt.show()
df= df[(df['Price'] >= cluster_price_data['Price'].min()-3) & (df['Price'] <= cluster_price_data['Price'].max())]

# Select the desired columns
selected_columns = ['Description', 'url', 'reviewcount', 'rating','Price']
df= df[selected_columns]

# Write filtered data to a new CSV file
df.to_csv('filtered_data9.csv', index=False) 
print(df.head()) # This will create a new file named 'filtered_data.csv'
print("Filtered data saved to 'filtered_data9.csv'")
csv_file = "D:\\py\\filtered_data9.csv"
df = pd.read_csv(csv_file)
df_deduplicated = df.drop_duplicates(subset=['Description'])

# Save the deduplicated data to a new CSV file

# Drop duplicate rows

print(df_deduplicated.shape[0])
# Save the deduplicated data to a new CSV file
output_csv_file = "D:\\py\\filtered_data9_deduplicated.csv"
df_deduplicated.to_csv(output_csv_file, index=False)

print("Duplicate rows dropped and saved to", output_csv_file)
df=pd.read_csv("D:\\py\\filtered_data9_deduplicated.csv")
print(df.head())




import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def scrape_rating_percentage(url):
    driver.get(url)
   
# Find the <a> element by ID
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    element = driver.find_element(By.ID,'acrCustomerReviewLink')

# Click the element
    element.click()
    driver.implicitly_wait(10)

    try:
          rating_link = driver.find_element(By.XPATH, '//a[contains(@href, "filterByStar=five_star")][contains(text(), "%")]')

    # Retrieve the "70%" data
          rating_percentage = rating_link.text.strip()
    
          return rating_percentage
    except NoSuchElementException:
           print("Rating percentage link notfound ")
           return None


def four (url):
    driver.get(url)
   
# Find the <a> element by ID
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    element = driver.find_element(By.ID,'acrCustomerReviewLink')

# Click the element
    element.click()

    #elements = driver.find_elements(By.CSS_SELECTOR,"span.a-size-base > a.a-link-normal[title='4 stars represent 18% of rating'][href*='/product-reviews/']")

# Get the text value of the first element (if found)
    #if elements:
         #percentage3 = elements[1].text.strip()

    #else:
         #percentage3 = "N/A"    

    rating_link = driver.find_element(By.XPATH, '//a[contains(@href, "filterByStar=four_star")][contains(text(), "%")]')

    # Retrieve the "18%" data
    rating_percentage = rating_link.text.strip()
# Get the text value of the element



    return rating_percentage


driver = webdriver.Chrome()
new_rows = []
with open(r"D:\\py\\filtered_data9_deduplicated.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_desc = row['Description']
        product_url = row['url']
        reviewc = row['reviewcount']
        percentage1 = scrape_rating_percentage(product_url)
        percentage7 = four(product_url)
        o_rating =row['rating']
        new_row = {
            'Description': product_desc,
            'url': product_url,
            '5star': percentage1,
            '4star': percentage7,
            'reviewcount': reviewc,
            'o_rating' :o_rating
                  }
        new_rows.append(new_row)
# Define the field names for the output CSV
field_names = ['Description', 'url', '5star', '4star','reviewcount','o_rating']

with open(r'D:\py\fileee3.csv', 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=field_names)
    
    # Write the header
    writer.writeheader()
    
    # Write the new rows
    writer.writerows(new_rows)

print("New CSV file created with calculated percentages.")
df = pd.read_csv(r'D:\py\fileee3.csv')

print(df.head())


columns_to_sum = ['5star', '4star', 'reviewcount', 'o_rating']

# Convert selected columns to numerical values (if needed)
df['5star'] = df['5star'].str.rstrip('%').astype(float)
df['4star'] = df['4star'].str.rstrip('%').astype(float)
for col in columns_to_sum:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert non-numeric values to NaN

# Calculate a combined score for each row based on the values in selected columns
df['combined_score'] = df[columns_to_sum].sum(axis=1, skipna=True)

# Sort the DataFrame by the combined score in descending order
sorted_data = df.sort_values(by='combined_score', ascending=False)

# Select the desired columns
selected_columns = ['Description', 'url', '5star', '4star', 'reviewcount', 'o_rating', 'combined_score']
sorted_data = sorted_data[selected_columns]

# Write sorted data to a new CSV file
sorted_data.to_csv('sorted_data1.csv', index=False)
print("Sorted data saved to 'sorted_data.csv'")




# Print the filtered DataFrame

