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


"""def scrape_rating_percentage(url):
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



    return rating_percentage"""

def review(url):
    driver.get(url)
   
# Find the <a> element by ID
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    element = driver.find_element(By.ID,'acrCustomerReviewLink')

# Click the element
    element.click()
    
    
    try:
       see_all_reviews_link = driver.find_element(By.CSS_SELECTOR, 'a[data-hook="see-all-reviews-link-foot"].a-link-emphasis.a-text-bold')

    # Click the "See all reviews" link
       see_all_reviews_link.click()




       page_source = driver.page_source
    

    # Parse the page source using BeautifulSoup
       soup = BeautifulSoup(page_source, 'html.parser')
       select=[]
    
    # Extract and print the reviews
       c_reviews = soup.find_all('div', {'data-hook': 'review'})
       for item in c_reviews:
            review = {
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip()
        }
            select.append(review)
        

    
    #print("next page")
    
    
    
       next_page_link = driver.find_element(By.XPATH, '//a[contains(@href, "/product-reviews/") and contains(@href, "pageNumber=2")]')

    # Click the "Next page" link
    
    # Click the "Next page" link
       next_page_link.click()

       page_source1 = driver.page_source
    

    # Parse the page source using BeautifulSoup
       soup = BeautifulSoup(page_source1, 'html.parser')

    # Extract and print the reviews
  
    # Extract and print the reviews
   
       c_reviews = soup.find_all('div', {'data-hook': 'review'})
       for item in c_reviews:
        review = {
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip()
        }
        select.append(review)
        
    
    
     #kppp

       next_page_link = driver.find_element(By.XPATH, '//a[contains(@href, "/product-reviews/") and contains(@href, "pageNumber=3")]')

    # Click the "Next page" link
    
    # Click the "Next page" link
       next_page_link.click()

       page_source = driver.page_source
    

    # Parse the page source using BeautifulSoup
       soup = BeautifulSoup(page_source, 'html.parser')

    # Extract and print the reviews
    
       c_reviews = soup.find_all('div', {'data-hook': 'review'})
       for item in c_reviews:
        review = {
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip()
        }
        select.append(review)
        
        
    

    
       next_page_link = driver.find_element(By.XPATH, '//a[contains(@href, "/product-reviews/") and contains(@href, "pageNumber=4")]')

    # Click the "Next page" link
    
    # Click the "Next page" link
       next_page_link.click()

       page_source = driver.page_source


       c_reviews = soup.find_all('div', {'data-hook': 'review'})
       for item in c_reviews:
        review = {
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip()
        }
        select.append(review)
       return select
    
    except NoSuchElementException:
        print("No reviews")
        return None

   



def critical_review(url):
        driver.get(url)
        select1=[]
   
# Find the <a> element by ID
        driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

        element = driver.find_element(By.ID,'acrCustomerReviewLink')

# Click the element
        element.click()
        driver.implicitly_wait(10)
        see_all_reviews_link = driver.find_element(By.CSS_SELECTOR, 'a[data-hook="see-all-reviews-link-foot"].a-link-emphasis.a-text-bold')

    # Click the "See all reviews" link
        see_all_reviews_link.click()
        #driver.execute_script("arguments[0].scrollIntoView(true);",see_all_reviews_link)
        all_critical_reviews_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="filterByStar=critical"][href*="reviewerType=all_reviews"]')

# Click the "All critical reviews" link
        all_critical_reviews_link.click()
        review_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-hook="review-body"].review-text-content')

# Fetch and print all the review texts
        for review_element in review_elements:
               review_text = review_element.text
               select1.append(review_text)
        try:       

           next_page_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="/Amazon-Brand-Sunscreen-Spectrum-Protection/product-reviews"][href*="pageNumber=2"]')

# Click the "Next page" link
    
           next_page_link.click()
           review_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-hook="review-body"].review-text-content')

# Fetch and print all the review texts
           for review_element in review_elements:
                 review_text = review_element.text
                 select1.append(review_text)
               
           next_page_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="/Amazon-Brand-Sunscreen-Spectrum-Protection/product-reviews"][href*="pageNumber=3"]')

# Click the "Next page" link
           next_page_link.click()
           review_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-hook="review-body"].review-text-content')

# Fetch and print all the review texts
           for review_element in review_elements:
               review_text = review_element.text
               select1.append(review_text)
               
           return select1

        except (StaleElementReferenceException, NoSuchElementException):
        
                return select1
     
    









def write_reviews_to_csv(products_data):
    with open(r'D:\py\merix1.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        for product in products_data:
            product_url = product['url']
            reviews_list = review(product_url)

            # Write the reviews for the product in the same row
            csv_writer.writerow(reviews_list)

def write_reviews_to_csvc(products_data):
    with open(r'D:\py\scrapzz.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        for product in products_data:
            product_url = product['url']
            reviews_list = critical_review(product_url)

            # Write the reviews for the product in the same row
            csv_writer.writerow(reviews_list)  


driver = webdriver.Chrome()


products_data = []

with open(r"D:\py\sorted_data1.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_desc = row['Description']
        product_url = row['url']
        """percentage1 = scrape_rating_percentage(product_url)
        percentage7 = four(product_url)"""
        
        print(f"Product Description: {product_desc}")
        print(f"Product URL: {product_url}")
        """print(f"Rating Percentage: {percentage1}")
        print(f"4star: {percentage7}")"""
        
        # Append the row data to products_data list
        products_data.append(row)

# Now, products_data will contain all the rows from the CSV file
print(products_data)
# Read all rows fr
 #Read all rows from the CSV file into a list of 
    

#write_reviews_to_csvc(products_data)
write_reviews_to_csv(products_data)



# Close the browser after completing the scraping
driver.quit()
