#!/usr/bin/env python
# coding: utf-8

# Data Collection 
# 
# In this notebook we will collect the customer review data from the airline quality website called Skytrax and analyse it. Very helpful source to how to web scraping is the ducument in Medium, the link is here https://medium.com/analytics-vidhya/webscraping-a-site-with-pagination-using-beautifulsoup-fa0a09804445.

# In[18]:


#import libraries
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


# In[19]:


#Defining the base URL and query parameters
base_url='https://www.airlinequality.com/airline-reviews/british-airways'
#query_parameter="/page/"+str(i)


# In[20]:


#creat an empty list to store all scraped reviews
all_pages_reviews=[]


# In[21]:


#define a scraper function
def scraper():
    for i in range(1,10):
        #creat an empty list to store the reviews of each page
        pagewise_reviews=[]
        #construct the URL
        query_parameter="/page/"+str(i)
        url=base_url+query_parameter
        #send http request to the URL using request and store response
        response=requests.get(url)
        #creat the soup object and parse the html
        soup=BeautifulSoup(response.content,'html.parser')
        #find all the div elements of class name text_content and store them in a variable
        rev_div=soup.findAll("div",attrs={"class","text_content"})
    #loop through all the rev_div and append the review text to the pagewise_reviews list
    for j in range(len(rev_div)):
        # finding all the strong tags to fetch only the review text
        pagewise_reviews.append(rev_div[j].find('strong').text)
        #append all page wise review to a single list 'all_pages_reviews'
        for k in range(len(pagewise_reviews)):
            all_pages_reviews.append(pagewise_reviews[k])
            return all_pages_reviews
# Call the function scraper() and store the output to a variable 'reviews' 
reviews = scraper()
        
        


# In[22]:


i = range(1, len(reviews)+1)
reviews_df = pd.DataFrame({'review':reviews}, index=i)
df=reviews_df.to_csv('reviews.txt', sep='t')


# In[23]:


df.head()


# In[ ]:


#get the html data
page=requests.get(base_url)
htmlData=page.content


# In[ ]:


#pars the html data
soup=BeautifulSoup(htmlData,'lxml')


# In[ ]:


#organise the data with prettify
print(soup.prettify)


# In[ ]:


#get the title
title=soup.title
print(title)


# In[ ]:


#print out the text
text=soup.get_text()
#print(text)


# In[ ]:


#pull the titles and hrefs of all 10 reviews in first page
reviews_rating_title=soup.find_all('div', class_="review-stats")
print(reviews_rating_title)


# In[ ]:


df=pd.DataFrame()                    


# In[ ]:


reviews=df['reviews_rating_title']


# In[ ]:





# In[ ]:


paginated_url = f"{url}/page/{page_num}/?sortby=post_date%3ADesc&pagesize={page_size}"
print(paginated_url )


# In[ ]:


con=article.table.td.text
print(con)


# In[ ]:




