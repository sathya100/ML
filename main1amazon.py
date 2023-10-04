import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
import pandas as pd
import re


def get_url1(search_term):
    template= 'https://www.amazon.com/s?k={}&crid=36LOFF5NBCR9T&sprefix={}%2Caps%2C387&ref=nb_sb_noss_2'
    search_term=search_term.replace(' ','+')
    

    url=template.format(search_term,search_term)
    url += '&page{}'
    return url


def extract_record(item):
     atag=item.h2.a
     description=atag.text.strip()
     url='https://www.amazon.com' + atag.get('href')

     try:
     
        price_parent=item.find('span','a-price')
        price=price_parent.find('span','a-offscreen').text
        
     except AttributeError:
        return 
 

     try:
         rating=item.i.text
         review_count=item.find('span',{'class':'a-size-base s-underline-text'}).text
     except AttributeError:
         rating= ' '
         review_count= ' '


     result=(description,price,rating,review_count,url)
     return result
def main(search_term):
       driver=webdriver.Chrome()
       records=[]
       url=get_url1(search_term)
       for page in range(1,21):
           driver.get(url.format(page))
           soup=BeautifulSoup(driver.page_source,'html.parser')
           results=soup.find_all('div', {'data-component-type': 's-search-result'})

           for item in results:
               record=extract_record(item)
               if record:
                   records.append(record)
       driver.close()
       with open('font67.csv','w',newline='',encoding='utf-8') as f:
           writer=csv.writer(f)
           writer.writerow(['Description','Price','rating','reviewcount','url'])
           writer.writerows(records)

product=input("Enter the product you need to search :")

main(product)    



       