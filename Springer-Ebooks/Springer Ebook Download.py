# -*- coding: utf-8 -*-
"""
Created on Tue May 12 2020

@author: Yadnesh

https://www.stuffbyyc.com/
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import sys 

data =  pd.read_csv("Data/Springer Ebooks.csv") 
Book_Title = data.Book_Title.tolist()
OpenURL = data.OpenURL.tolist()

for i in range(len(Book_Title)):
    print(i)
    url = str(OpenURL[i])
    filename= Book_Title[i]
    print(url)
    print(filename)
    
    r = requests.get(url)
    download_lnk=""
    soup = BeautifulSoup(r.content, 'html.parser')
    
    #Getting Download link
    for link in soup.findAll("a",class_ = "c-button c-button--blue c-button__icon-right test-download-book-options test-bookpdf-link", attrs={'href': re.compile("content/pdf/")}):
        download_lnk=link.get('href')
    
    
    if (str(download_lnk) == ""):
        for link in soup.findAll("a",class_ = "c-button c-button--blue c-button__icon-right test-bookpdf-link", attrs={'href': re.compile("content/pdf/")}):
            download_lnk=link.get('href')
      
    print(download_lnk)
    
    
    if(str(download_lnk) == ""):
        print("Empty")
        
    if(str(download_lnk) != ""):
        file_url = "https://link.springer.com"+str(download_lnk)
        myfile = requests.get(file_url)
        open("Downloads/"+str(i)+". "+filename+".pdf", 'wb').write(myfile.content)    
    
    
