#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
import time
import datetime
import smtplib


# In[2]:


URLcellphones = 'https://cellphones.com.vn/mobile/apple/iphone-15.html'
URLcellphones2 = 'https://cellphones.com.vn/iphone-15-512gb.html'
URLcellphones3 = 'https://cellphones.com.vn/iphone-15-plus-512gb.html'
URLcellphones4 = 'https://cellphones.com.vn/iphone-15-pro-512gb.html'
URLcellphones5 = 'https://cellphones.com.vn/iphone-15-pro-1tb.html'

URLtopzone = 'https://www.topzone.vn/iphone-15'

URLhoangha = 'https://hoanghamobile.com/dien-thoai-di-dong/iphone/iphone-15-series'

URLfpt1 = 'https://fstudiobyfpt.com.vn/iphone/iphone-15-pro-max?dung-luong=256gb'
URLfpt2 = 'https://fstudiobyfpt.com.vn/iphone/iphone-15-pro?dung-luong=256gb'
URLfpt3 = 'https://fstudiobyfpt.com.vn/iphone/iphone-15-plus?dung-luong=128gb'
URLfpt4 = 'https://fstudiobyfpt.com.vn/iphone/iphone-15?dung-luong=128gb'

URLshopdunk = 'https://shopdunk.com/iphone-15-series'

URLviettelstore1 = 'https://viettelstore.vn/dien-thoai/iphone-15-pro-max-256gb-pid317067.html'
URLviettelstore2 = 'https://viettelstore.vn/dien-thoai/iphone-15-pro-pid317061.html'
URLviettelstore3 = 'https://viettelstore.vn/dien-thoai/iphone-15-plus-pid317057.html'
URLviettelstore4 = 'https://viettelstore.vn/dien-thoai/iphone-15-128gb-pid317053.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page1 = requests.get(URLcellphones, headers=headers)
soup1 = BeautifulSoup(page1.content, "html.parser")
soup1_1 = BeautifulSoup(soup1.prettify(), "html.parser")

page1_2 = requests.get(URLcellphones2, headers=headers)
soup1_2_1 = BeautifulSoup(page1_2.content, "html.parser")
soup1_2_2 = BeautifulSoup(soup1_2_1.prettify(), "html.parser")

page1_3 = requests.get(URLcellphones3, headers=headers)
soup1_3_1 = BeautifulSoup(page1_3.content, "html.parser")
soup1_3_2 = BeautifulSoup(soup1_3_1.prettify(), "html.parser")

page1_4 = requests.get(URLcellphones4, headers=headers)
soup1_4_1 = BeautifulSoup(page1_4.content, "html.parser")
soup1_4_2 = BeautifulSoup(soup1_4_1.prettify(), "html.parser")

page1_5 = requests.get(URLcellphones5, headers=headers)
soup1_5_1 = BeautifulSoup(page1_5.content, "html.parser")
soup1_5_2 = BeautifulSoup(soup1_5_1.prettify(), "html.parser")

page2 = requests.get(URLtopzone, headers=headers)
soup2 = BeautifulSoup(page2.content, "html.parser")
soup2_1 = BeautifulSoup(soup2.prettify(), "html.parser")

page3 = requests.get(URLhoangha, headers=headers)
soup3 = BeautifulSoup(page3.content, "html.parser")
soup3_1 = BeautifulSoup(soup3.prettify(), "html.parser")

page4_1 = requests.get(URLfpt1, headers=headers)
soup4_1_1 = BeautifulSoup(page4_1.content, "html.parser")
soup4_1_2 = BeautifulSoup(soup4_1_1.prettify(), "html.parser")
page4_2 = requests.get(URLfpt2, headers=headers)
soup4_2_1 = BeautifulSoup(page4_2.content, "html.parser")
soup4_2_2 = BeautifulSoup(soup4_2_1.prettify(), "html.parser")
page4_3 = requests.get(URLfpt3, headers=headers)
soup4_3_1 = BeautifulSoup(page4_3.content, "html.parser")
soup4_3_2 = BeautifulSoup(soup4_3_1.prettify(), "html.parser")
page4_4 = requests.get(URLfpt4, headers=headers)
soup4_4_1 = BeautifulSoup(page4_4.content, "html.parser")
soup4_4_2 = BeautifulSoup(soup4_4_1.prettify(), "html.parser")

page5 = requests.get(URLshopdunk, headers=headers)
soup5 = BeautifulSoup(page5.content, "html.parser")
soup5_1 = BeautifulSoup(soup5.prettify(), "html.parser")

page6_1 = requests.get(URLviettelstore1, headers=headers)
soup6_1_1 = BeautifulSoup(page6_1.content, "html.parser")
soup6_1_2 = BeautifulSoup(soup6_1_1.prettify(), "html.parser")
page6_2 = requests.get(URLviettelstore2, headers=headers)
soup6_2_1 = BeautifulSoup(page6_2.content, "html.parser")
soup6_2_2 = BeautifulSoup(soup6_2_1.prettify(), "html.parser")
page6_3 = requests.get(URLviettelstore3, headers=headers)
soup6_3_1 = BeautifulSoup(page6_3.content, "html.parser")
soup6_3_2 = BeautifulSoup(soup6_3_1.prettify(), "html.parser")
page6_4 = requests.get(URLviettelstore4, headers=headers)
soup6_4_1 = BeautifulSoup(page6_4.content, "html.parser")
soup6_4_2 = BeautifulSoup(soup6_4_1.prettify(), "html.parser")


# In[3]:


re_name = {    
    ('iphone', '15', 'pro', 'max', '256gb'): 'iPhone 15 Pro Max 256GB',
    ('iphone', '15', 'pro', 'max', '512gb'): 'iPhone 15 Pro Max 512GB',
    ('iphone', '15', 'pro', 'max', '1tb'): 'iPhone 15 Pro Max 1TB',
    
    ('iphone', '15', 'pro', '128gb'): 'iPhone 15 Pro 128GB',
    ('iphone', '15', 'pro', '256gb'): 'iPhone 15 Pro 256GB',
    ('iphone', '15', 'pro', '512gb'): 'iPhone 15 Pro 512GB',
    ('iphone', '15', 'pro', '1tb'): 'iPhone 15 Pro 1TB',
    
    ('iphone', '15', 'plus', '128gb'): 'iPhone 15 Plus 128GB',
    ('iphone', '15', 'plus', '256gb'): 'iPhone 15 Plus 256GB',
    ('iphone', '15', 'plus', '512gb'): 'iPhone 15 Plus 512GB',
    
    ('iphone', '15', '128gb'): 'iPhone 15 128GB',
    ('iphone', '15', '256gb'): 'iPhone 15 256GB',
    ('iphone', '15', '512gb'): 'iPhone 15 512GB'
}


def find_id(name, re_name):
    name_lower = name.lower()
    for combo, newname in re_name.items():
        if all(word in name_lower for word in combo):
            return newname


# In[4]:


soup1_1_2 = soup1_1.find_all(class_ = 'product__price--show')

price1 = [option.get_text(strip=True) for option in soup1_1_2]

soup1_2_4 = soup1_2_2.find(class_ = 'product__price--show')
soup1_2_5 = soup1_2_4.get_text().strip()

soup1_3_4 = soup1_3_2.find(class_ = 'product__price--show')
soup1_3_5 = soup1_3_4.get_text().strip()

soup1_4_4 = soup1_4_2.find(class_ = 'product__price--show')
soup1_4_5 = soup1_4_4.get_text().strip()

soup1_5_4 = soup1_5_2.find(class_ = 'product__price--show')
soup1_5_5 = soup1_5_4.get_text().strip()

price1.append(soup1_2_5)
price1.append(soup1_3_5)
price1.append(soup1_4_5)
price1.append(soup1_5_5)

cellphonesprice = price1


# In[5]:


soup1_1_3 = soup1_1.find_all('h3')
option1 = [option.get_text(strip=True) for option in soup1_1_3]
option2 = option1 [:9]

soup1_2_3 = soup1_2_2.find(class_ = 'box-product-name')
option1_add512 = soup1_2_3.get_text().strip()

soup1_3_3 = soup1_3_2.find(class_ = 'box-product-name')
option1_addplus512 = soup1_3_3.get_text().strip()

soup1_4_3 = soup1_4_2.find(class_ = 'box-product-name')
option1_addpro512 = soup1_4_3.get_text().strip()

soup1_5_3 = soup1_5_2.find(class_ = 'box-product-name')
option1_addpro1tb = soup1_5_3.get_text().strip()

option2.append(option1_add512)
option2.append(option1_addplus512)
option2.append(option1_addpro512)
option2.append(option1_addpro1tb)

cellphonesoption = option2


# In[6]:


soup2_2 = soup2_1.find_all(class_ = 'price')
soup2_3 = [price.get_text(strip=True) for price in soup2_2]
topzoneprice = soup2_3


# In[7]:


soup2_4 = soup2_1.find_all('h3')
soup2_5 = [option.get_text(strip=True) for option in soup2_4]
topzoneoption = soup2_5


# In[8]:


soup3_2 = soup3_1.find_all('a' ,class_ = 'title')
soup3_3 = [option.get_text(strip=True) for option in soup3_2]
hoanghaoption = soup3_3


# In[9]:


soup3_4 = soup3_1.find_all('span', class_ = 'price')
soup3_5 = [price.get_text(strip=True) for price in soup3_4]
hoanghaprice = soup3_5


# In[10]:


pricegb1 = ['priceGB-46449', 'priceGB-46450', 'priceGB-46451']
pricegb2 = ['priceGB-46445', 'priceGB-46446', 'priceGB-46447', 'priceGB-46448']
pricegb3 = ['priceGB-46442', 'priceGB-46443', 'priceGB-46444']
pricegb4 = ['priceGB-46211', 'priceGB-46439', 'priceGB-46440']
fptprice =[]
for subpricegb1 in pricegb1:
    soup4_1_3 = soup4_1_2.find(class_ = subpricegb1)
    soup4_1_4 = soup4_1_3.get_text(strip = True)
    fptprice.append(soup4_1_4)
for subpricegb2 in pricegb2:
    soup4_2_3 = soup4_2_2.find(class_ = subpricegb2)
    soup4_2_4 = soup4_2_3.get_text(strip = True)
    fptprice.append(soup4_2_4)
for subpricegb3 in pricegb3:
    soup4_3_3 = soup4_3_2.find(class_ = subpricegb3)
    soup4_3_4 = soup4_3_3.get_text(strip = True)
    fptprice.append(soup4_3_4) 
for subpricegb4 in pricegb4:
    soup4_4_3 = soup4_4_2.find(class_ = subpricegb4)
    soup4_4_4 = soup4_4_3.get_text(strip = True)
    fptprice.append(soup4_4_4)    
fptprice


# In[11]:


fptoption = []
soup4_1_5 = soup4_1_1.find_all(class_ = 'radio')
soup4_1_6 = [option.get_text(strip=True) for option in soup4_1_5]
soup4_1_7 = soup4_1_6[:3]
fptoption.extend(soup4_1_7)

soup4_2_5 = soup4_2_1.find_all(class_ = 'radio')
soup4_2_6 = [option.get_text(strip=True) for option in soup4_2_5]
soup4_2_7 = soup4_2_6[:4]
fptoption.extend(soup4_2_7)

soup4_3_5 = soup4_3_1.find_all(class_ = 'radio')
soup4_3_6 = [option.get_text(strip=True) for option in soup4_3_5]
soup4_3_7 = soup4_3_6[:3]
fptoption.extend(soup4_3_7)

soup4_4_5 = soup4_4_1.find_all(class_ = 'radio')
soup4_4_6 = [option.get_text(strip=True) for option in soup4_4_5]
soup4_4_7 = soup4_4_6[:3]
fptoption.extend(soup4_4_7)

fptoption


# In[12]:


soup5_2 = soup5_1.find_all(class_ = 'product-title')
soup5_3 = [option.get_text(strip=True) for option in soup5_2]
shopdunkoption = soup5_3
shopdunkoption


# In[52]:


soup5_4 = soup5_1.find_all(class_ = 'price actual-price')
soup5_5 = [price.get_text(strip=True) for price in soup5_4]
shopdunkprice = soup3_5
shopdunkprice


# In[14]:


vietteloption =[]
soup6_1_3 = soup6_1_2.find_all(class_ = 'version-product')
soup6_1_4 = [option.get_text(strip=True) for option in soup6_1_3]
vietteloption.extend(soup6_1_4)

soup6_2_3 = soup6_2_2.find_all(class_ = 'version-product')
soup6_2_4 = [option.get_text(strip=True) for option in soup6_2_3]
vietteloption.extend(soup6_2_4)

soup6_3_3 = soup6_3_2.find_all(class_ = 'version-product')
soup6_3_4 = [option.get_text(strip=True) for option in soup6_3_3]
vietteloption.extend(soup6_3_4)

soup6_4_3 = soup6_4_2.find_all(class_ = 'version-product')
soup6_4_4 = [option.get_text(strip=True) for option in soup6_4_3]
vietteloption.extend(soup6_4_4)

vietteloption


# In[15]:


viettelprice =[]
soup6_1_5 = soup6_1_2.find_all(class_ = 'txt-price')
soup6_1_6 = [price.get_text(strip=True) for price in soup6_1_5]
viettelprice.extend(soup6_1_6)

soup6_2_5 = soup6_2_2.find_all(class_ = 'txt-price')
soup6_2_6 = [price.get_text(strip=True) for price in soup6_2_5]
viettelprice.extend(soup6_2_6)

soup6_3_5 = soup6_3_2.find_all(class_ = 'txt-price')
soup6_3_6 = [price.get_text(strip=True) for price in soup6_3_5]
viettelprice.extend(soup6_3_6)

soup6_4_5 = soup6_4_2.find_all(class_ = 'txt-price')
soup6_4_6 = [price.get_text(strip=True) for price in soup6_4_5]
viettelprice.extend(soup6_4_6)

viettelprice


# In[16]:


cellphonesprice


# In[17]:


cellphonesoption


# In[29]:


cellphones_standardized = [find_id(name, re_name) for name in cellphonesoption]
dfcellphones = pd.DataFrame({'Old Name': cellphonesoption, 'Standardized Name': cellphones_standardized, 'Price' : cellphonesprice})
dfcellphones


# In[47]:


fpt_standardized = [ 'iPhone 15 Pro Max 256GB','iPhone 15 Pro Max 512GB','iPhone 15 Pro Max 1TB','iPhone 15 Pro 128GB','iPhone 15 Pro 256GB','iPhone 15 Pro 512GB','iPhone 15 Pro 1TB','iPhone 15 Plus 128GB','iPhone 15 Plus 256GB' ,'iPhone 15 Plus 512GB','iPhone 15 128GB', 'iPhone 15 256GB', 'iPhone 15 512GB']
dffpt = pd.DataFrame({'Old Name': fptoption, 'Standardized Name': fpt_standardized, 'Price' : fptprice})
dffpt


# In[31]:


topzone_standardized = [find_id(name, re_name) for name in topzoneoption]
dftopzone = pd.DataFrame({'Old Name': topzoneoption, 'Standardized Name': topzone_standardized, 'Price' : topzoneprice})
dftopzone


# In[32]:


shopdunk_standardized = [find_id(name, re_name) for name in shopdunkoption]
dfshopdunk = pd.DataFrame({'Old Name': shopdunkoption, 'Standardized Name': shopdunk_standardized, 'Price' : shopdunkprice})
dfshopdunk


# In[33]:


hoangha_standardized = [find_id(name, re_name) for name in hoanghaoption]
dfhoangha = pd.DataFrame({'Old Name': hoanghaoption, 'Standardized Name': hoangha_standardized, 'Price' : hoanghaprice})
dfhoangha


# In[34]:


viettel_standardized = [find_id(name, re_name) for name in vietteloption]
dfviettel = pd.DataFrame({'Old Name': vietteloption, 'Standardized Name': viettel_standardized, 'Price' : viettelprice})
dfviettel


# In[57]:


dfviettel2 = pd.DataFrame({'Ten san pham': viettel_standardized, 'Viettel' : viettelprice})
dfhoangha2 = pd.DataFrame({ 'Ten san pham': hoangha_standardized, 'Hoang Ha' : hoanghaprice})
dfshopdunk2 = pd.DataFrame({ 'Ten san pham': shopdunk_standardized, 'Shop Dunk' : shopdunkprice})
dftopzone2 = pd.DataFrame({'Ten san pham': topzone_standardized, 'Top Zone' : topzoneprice})
dffpt2 = pd.DataFrame({ 'Ten san pham': fpt_standardized, 'FPT' : fptprice})
dfcellphones2 = pd.DataFrame({ 'Ten san pham': cellphones_standardized, 'Cellphones' : cellphonesprice})

merged_df = pd.merge(dfviettel2, dfcellphones2, on='Ten san pham', how='outer')
merged_df = pd.merge(merged_df, dftopzone2, on='Ten san pham', how='outer')
merged_df = pd.merge(merged_df, dfhoangha2, on='Ten san pham', how='outer')
merged_df = pd.merge(merged_df, dffpt2, on='Ten san pham', how='outer')
#merged_df = pd.merge(merged_df, dfshopdunk2, on='Ten san pham', how='outer')


# In[78]:


finaldf = pd.DataFrame(data = merged_df).set_index('Ten san pham')
finaldf


# In[84]:


finaldf.loc[['iPhone 15 Pro Max 256GB','iPhone 15 128GB']]


# In[ ]:





# In[ ]:




